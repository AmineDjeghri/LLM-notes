## JSON mode and structured outputs
#### Azure OpenAI and Azure AI Foundry: 

All Azure models and details : https://github.com/MicrosoftDocs/azure-ai-docs/blob/main/articles/ai-foundry/model-inference/concepts/models.md#azure-openai

From openAI documentation : 
- When JSON mode is turned on, the model's output is ensured to be valid JSON, except for in some edge cases that you should detect and handle appropriately.
- Structured Outputs is the evolution of JSON mode. **While both ensure valid JSON is produced, only Structured Outputs ensure schema adherance.** 
-  While JSON mode ensures that model output is valid JSON, Structured Outputs reliably matches the model's output to the schema you specify. We recommend you use Structured Outputs if it is supported for your use case.
- When using JSON mode, you must always instruct the model to produce JSON via some message in the conversation, for example via your system message. If you don't include an explicit instruction to generate JSON, the model may generate an unending stream of whitespace and the request may run continually until it reaches the token limit.
- JSON mode will not guarantee the output matches any specific schema, only that it is valid and parses without errors. You should use Structured Outputs to ensure it matches your schema, or if that is not possible, you should use a validation library and potentially retries to ensure that the output matches your desired schema.
- The new version of the SDK introduces a `parse` helper to provide your own Pydantic model instead of having to define the JSON schema. We recommend using this method if possible.

Azure OpenAI json_mode : 
```python
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": "Who won the world series in 2020? Please respond in the format {winner: ...}"}
        ],
        response_format={"type": "json_object"}
    )
```


AzureOpenAI Structured outputs: using pydantic or json_schema with schema
```python
class MathReasoning(BaseModel):
    steps: list[Step]
    final_answer: str

completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "You are a helpful math tutor. Guide the user through the solution step by step."},
        {"role": "user", "content": "how can I solve 8x + 7 = -23"}
    ],
    response_format=MathReasoning,
)
```
LiteLLM has the same logic.

Instructor : different modes. https://python.useinstructor.com/modes-comparison/#json-mode

**sources**
- https://platform.openai.com/docs/guides/structured-outputs
- https://cookbook.openai.com/examples/structured_outputs_intro

![[Pasted image 20250305081735.png]]

**Example**
Schema : Person (age and name)
prompt : John is 30 years old

| Name                   | Azure AI Inference | LiteLLM       | LiteLLM+ Instructor instructor.Mode.JSON | Azure OpenAI (parse) | Azure OpenAI |     |
| ---------------------- | ------------------ | ------------- | ---------------------------------------- | -------------------- | ------------ | --- |
| gpt-4o-mini-2024-07-18 | N/A                | ✅             | ✅                                        | ✅                    | ✅            |     |
| gpt-4o-2024-05-13      | N/A                | ✅ (json only) | ✅                                        | ❌                    | ✅            |     |
| o1-2024-12-17          | N/A                | ✅             | ✅                                        | ✅                    | ✅            |     |
| o1-mini-2024-09-12     | N/A                | ❌             | ✅                                        | ❌                    | ❌            |     |
| o3-mini-2025-01-31     | N/A                | ✅             | ✅                                        | ✅                    | ✅            |     |

- Structured Outputs with `response_format: {type: "json_schema", ...}` /pydantic is only supported with the `gpt-4o-mini`, `gpt-4o-mini-2024-07-18`, and `gpt-4o-2024-08-06` model snapshots and later.
- Models like o1-mini do not support structured output. See [link](https://github.com/MicrosoftDocs/azure-ai-docs/blob/main/articles/ai-foundry/model-inference/concepts/models.md#azure-openai) 
Notes : 
- You should always deploy the latest models to get the latest features.
- You should always use the latest version of azure openai.
- I recommend calling gpt4o/mini after the result to extract json as structured output as this is supported from 08/09 model versions
- (azure) To verify : using Structured ouputs with azure may raise content_filtering and false positives ? 
	- Someone with the same issue : https://learn.microsoft.com/en-us/answers/questions/2103254/azure-openai-gpt-4o-structured-response-format-tri


- If you want to use `ollama`, you need to specify `ollama_chat/model_name` instead of `ollama/model_name`. If a model doesn’t support structured_output, pass `instructor.mode.json` to the client : 

```
client = instructor.from_litellm(acompletion, mode=instructor.Mode.JSON)
```


| Name                                          | Azure AI Inference | LiteLLM | LiteLLM + Instructor (json mode) |
| --------------------------------------------- | ------------------ | ------- | -------------------------------- |
| azure_ai/Mistral-Large-2411                   | ✅ (json only)      |         | ✅                                |
| azure_ai/Mistral-Small                        | ✅ (json only)      |         | ✅                                |
| azure_ai/Phi-4                                | ❌(Timeout)         |         | ❌(Timeout)                       |
| azure_ai/DeepSeek-R1                          |                    |         | ✅                                |
| azure_ai/phi35-mini-instruct                  | ❌ (Timeout)        |         | ❌(Timeout)                       |
| ollama_chat/phi-3.5-uncensored                | N/A                |         | ✅ (mode=instructor.Mode.JSON)    |
| ollama_chat/qwen2.5:0.5b                      | N/A                |         | ✅(mode=instructor.Mode.JSON)     |
| ollama_chat/phi3:3.8b-mini-4k-instruct-q4_K_M | N/A                |         | ✅(mode=instructor.Mode.JSON)     |


#### example of LLM class

```python
import ast  
import asyncio  
import json  
import os  
import re  
from typing import Any, Type, List  
from typing import Optional, Sequence  
  
import instructor  
import litellm  
import pandas as pd  
from deepeval.models import DeepEvalBaseLLM, DeepEvalBaseEmbeddingModel  
from instructor.exceptions import InstructorError  
from langfuse import observe  
from litellm import (  
    completion,  
    acompletion,  
    supports_response_schema,  
    embedding,  
    aembedding,  
)  
from pandas import DataFrame  
from pydantic import BaseModel  
from pydantic import SecretStr, ConfigDict, field_validator, model_validator  
from typing_extensions import Self  
  
from genai_model_assessment.backend.langfuse_utils import update_langfuse_cost  
from genai_model_assessment.backend import logger, settings  
from langfuse import get_client  
  
from tenacity import (  
    retry,  
    stop_after_attempt,  
    wait_fixed,  
    retry_if_exception,  
)  
  
  
def should_retry_on_exception(e):  
    """Given an exception, should we retry it? If yes, return True. Otherwise, return False."""  
    # Unwrap the exception to get to the root cause    if isinstance(e, InstructorError):  
        root_exception = e  
        while hasattr(root_exception, "__cause__") and root_exception.__cause__ is not None:  
            root_exception = root_exception.__cause__  
    else:  
        root_exception = e  
  
    # Check if the root cause is a litellm exception we should retry on  
    if hasattr(root_exception, "status_code"):  
        if litellm._should_retry(status_code=root_exception.status_code):  
            logger.warning(f"Retrying due to error: {root_exception}. Status code:{root_exception.status_code}")  
            return True  
    logger.error(f"Failed to generate response. Not retrying. Error: {root_exception}")  
    return False  
  
  
class ChatMessage(BaseModel):  
    role: str  
    content: Optional[str] = None  
  
  
class AbstractLLMConfig(BaseModel):  
    """Configuration for the inference model.  
  
    Attributes:        model_name (str): The name of the inference model.        base_url (str): The base URL of the inference model.        api_key (SecretStr): The API key for the inference model.  
    """  
    model_name: str  
    base_url: str  
    api_key: SecretStr  
    api_version: str = "2025-03-01-preview"  # used only if model is from azure openai  
    model_config = ConfigDict(arbitrary_types_allowed=True)  
  
    @field_validator("model_name", "base_url", "api_key", mode="after")  
    @classmethod  
    def resolve_model_name(cls, value: str) -> str:  
        if isinstance(value, SecretStr):  
            value_str = value.get_secret_value()  
        else:  
            value_str = value  
        if "{{env" in value_str:  
            pattern = r"\{\{env\.(.*?)\}\}"  
            match = re.search(pattern, value_str)  
            if match:  
                env_var = match.group(1)  
                env_var_value = os.getenv(env_var)  
                # VertexAI and Gemini for example don't need base_url with litellm.  
                if not "BASE_URL" in env_var and not env_var_value:  
                    logger.exception(f"Environment variable {env_var} is not set")  
                    raise ValueError(f"Environment variable {env_var} is not set")  
                # replace the .env with the evaluated string in the original value  
  
                env_var_name = value_str.split(":")[-1]  
                value_str = value_str.replace(env_var_name, env_var_value)  
  
                if isinstance(value, SecretStr):  
                    value_str = SecretStr(value_str)  
                return value_str  
  
            else:  
                logger.error(f"Invalid deployment name: {value}")  
                raise ValueError(f"Invalid deployment name: {value}")  
        else:  
            return value  
  
  
class InferenceLLMConfig(AbstractLLMConfig, DeepEvalBaseLLM):  
    """Configuration for the inference model.  
  
    Attributes:        id (str): The ID of the inference model.        model_name (str): The name of the inference model.        base_url (str): The base URL of the inference model.        api_key (SecretStr): The API key for the inference model.  
    """  
    supports_response_schema: bool = False  
  
    temperature: float = 0.7  
    seed: Optional[int] = None  
    max_completion_tokens: Optional[int] = None  
    reasoning_effort: Optional[str] = None  # e.g., "low" | "medium" | "high"  
  
    # Helper to extract the model's core params directly    @staticmethod  
    def core_params(model) -> str:  
        return str(  
            {  
                "temperature": getattr(model, "temperature", None),  
                "seed": getattr(model, "seed", None),  
                "max_completion_tokens": getattr(model, "max_completion_tokens", None),  
                "reasoning_effort": getattr(model, "reasoning_effort", None),  
            }  
        )  
  
    @model_validator(mode="after")  
    def init_client(self) -> Self:  
        litellm.drop_params = True  
        self.supports_response_schema = supports_response_schema(  
            model=self.model_name.split("/")[-1], custom_llm_provider=self.model_name.split("/")[-2]  
        )  
        # logger.warning(f" supports_response_schema for {self.model_name}: {self.supports_response_schema}")  
        return self  
  
    def _build_effective_params(  
        self,  
        *,  
        temperature: Optional[float] = None,  
        max_completion_tokens: Optional[int] = None,  
        seed: Optional[int] = None,  
        reasoning_effort: Optional[str] = None,  
    ) -> dict:  
        """Return effective litellm params, preferring function args over self defaults.  
  
        Only emits keys supported by litellm natively:        - temperature        - max_completion_tokens        - seed        - reasoning (maps effort if provided)        """        eff_temp = self.temperature if temperature is None else temperature  
        eff_mct = self.max_completion_tokens if max_completion_tokens is None else max_completion_tokens  
        eff_seed = self.seed if seed is None else seed  
        eff_reff = self.reasoning_effort if reasoning_effort is None else reasoning_effort  
  
        out: dict[str, Any] = {}  
        if eff_temp is not None:  
            out["temperature"] = eff_temp  
        if eff_mct is not None:  
            out["max_completion_tokens"] = eff_mct  
        if eff_seed is not None:  
            out["seed"] = eff_seed  
        if eff_reff is not None:  
            out["reasoning"] = {"effort": eff_reff}  
        return out  
  
    def _split_effective_kwargs(self, kwargs: dict) -> tuple[dict, dict]:  
        """Build effective model params and filter them out of kwargs to avoid duplicates.  
  
        Returns (model_parameters, remaining_kwargs).        """        model_parameters = self._build_effective_params(  
            temperature=kwargs.get("temperature"),  
            max_completion_tokens=kwargs.get("max_completion_tokens"),  
            seed=kwargs.get("seed"),  
            reasoning_effort=kwargs.get("reasoning_effort"),  
        )  
        remaining = dict(kwargs)  
        for k in ("temperature", "max_completion_tokens", "seed", "reasoning_effort", "reasoning"):  
            remaining.pop(k, None)  
        return model_parameters, remaining  
  
    def _check_finish_reason(self, res) -> None:  
        finish_reason = None  
        try:  
            finish_reason = res.choices[0].finish_reason  
        except (AttributeError, IndexError, KeyError) as e:  
            logger.warning(f"Could not read finish_reason." f"\nres: {res}" f"\nERROR: {e}")  
        if finish_reason == "content_filter":  
            raise ValueError(f"Response filtered by content filter. Complete response: {res}")  
        if finish_reason == "refusal":  
            raise ValueError(f"Response filtered by content filter. Complete response: {res}")  
  
    def _extract_message_content(self, res) -> str:  
        try:  
            content = res.choices[0].message.content  
        except (AttributeError, IndexError, KeyError) as e:  
            raise ValueError(  
                f"No usable content in response (missing choices/message/content).\nres: {res}\nERROR: {e}"  
            )  
        return content  
  
    def _update_generation_cost(self, res, *, model_parameters: dict, include_model_parameters: bool = True) -> None:  
        payload = {  
            "model": self.model_name,  
            **update_langfuse_cost(  
                num_input_tokens=res.usage.prompt_tokens,  
                num_output_tokens=res.usage.completion_tokens,  
                total_tokens=res.usage.total_tokens,  
                total_cost=res._hidden_params["response_cost"],  
                model=self.model_name,  
            ),  
        }  
        if include_model_parameters:  
            payload["model_parameters"] = model_parameters  
        get_client().update_current_generation(**payload)  
  
    def _handle_schema_response(  
        self,  
        res,  
        *,  
        schema: Type[BaseModel],  
        raw_response: bool,  
        model_parameters: dict,  
        include_model_parameters: bool,  
    ):  
        self._check_finish_reason(res)  
        content_str = self._extract_message_content(res)  
        try:  
            dict_res = json.loads(_trim_json(content_str))  
        except json.JSONDecodeError:  
            dict_res = ast.literal_eval(content_str)  
  
        self._update_generation_cost(  
            res,  
            model_parameters=model_parameters,  
            include_model_parameters=include_model_parameters,  
        )  
  
        if raw_response:  
            return res  
        return schema(**dict_res)  
  
    def _handle_raw_response(  
        self,  
        res,  
        *,  
        raw_response: bool,  
        model_parameters: dict,  
    ):  
        self._update_generation_cost(res, model_parameters=model_parameters)  
        self._check_finish_reason(res)  
        if raw_response:  
            return res  
        return self._extract_message_content(res)  
  
    # Removed: _build_generation_model_parameters; we rely only on _build_effective_params  
  
    def load_model(self, prompt: str, schema: Type[BaseModel] | None = None, *args, **kwargs):  
        pass  
  
    @observe  
    async def a_generate(  
        self,  
        prompt: str,  
        schema: Type[BaseModel] | None = None,  
        raw_response: bool = False,  
        *args,  
        **kwargs,  
    ):  
        # Split effective params from remaining kwargs to avoid duplicates downstream  
        params_dict, remaining_kwargs = self._split_effective_kwargs(kwargs)  
  
        messages = [{"role": "user", "content": prompt}]  
        get_client().update_current_generation(input=messages, model_parameters=params_dict)  
        return await self.a_generate_from_messages(  
            messages=messages,  
            schema=schema,  
            raw_response=raw_response,  
            *args,  
            **params_dict,  
            **remaining_kwargs,  
        )  
  
    @observe(as_type="generation")  
    @retry(  
        wait=wait_fixed(settings.WAIT_DELAY),  
        stop=stop_after_attempt(settings.STOP_AFTER_ATTEMPT),  
        retry=retry_if_exception(should_retry_on_exception),  
    )  
    async def a_generate_from_messages(  
        self,  
        messages: list,  
        schema: Type[BaseModel] = None,  
        raw_response: bool = False,  
        *args,  
        **kwargs,  
    ):  
        # Build model parameters from provided kwargs and keep the rest for provider-specific options  
        model_parameters, remaining_kwargs = self._split_effective_kwargs(kwargs)  
        get_client().update_current_generation(input=messages, model_parameters=model_parameters)  
        # check if model supports structured output  
        if schema:  
            if self.supports_response_schema:  
                res = await litellm.acompletion(  
                    model=self.model_name,  
                    api_key=self.api_key.get_secret_value(),  
                    base_url=self.base_url,  
                    messages=messages,  
                    response_format=schema,  
                    api_version=self.api_version,  
                    *args,  
                    **model_parameters,  
                    **remaining_kwargs,  
                )  
                return self._handle_schema_response(  
                    res,  
                    schema=schema,  
                    raw_response=raw_response,  
                    model_parameters=model_parameters,  
                    include_model_parameters=True,  
                )  
  
            else:  
                # if the model doesn't support structured output, use Instructor with json_mode  
                client = instructor.from_litellm(acompletion, mode=instructor.Mode.JSON)  
                output, raw_completion = await client.chat.completions.create_with_completion(  
                    model=self.model_name,  
                    api_key=self.api_key.get_secret_value(),  
                    base_url=self.base_url,  
                    messages=messages,  
                    response_model=schema,  
                    api_version=self.api_version,  
                    *args,  
                    **model_parameters,  
                    **remaining_kwargs,  
                )  
                get_client().update_current_generation(  
                    model=self.model_name,  
                    model_parameters=model_parameters,  
                    **update_langfuse_cost(  
                        num_input_tokens=raw_completion.usage.prompt_tokens,  
                        num_output_tokens=raw_completion.usage.completion_tokens,  
                        total_tokens=raw_completion.usage.total_tokens,  
                        total_cost=raw_completion._hidden_params["response_cost"],  
                        model=self.model_name,  
                    ),  
                )  
                if raw_response:  
                    return raw_completion  
                return output  
  
        else:  
            res = await litellm.acompletion(  
                model=self.model_name,  
                api_key=self.api_key.get_secret_value(),  
                base_url=self.base_url,  
                messages=messages,  
                api_version=self.api_version,  
                *args,  
                **model_parameters,  
                **remaining_kwargs,  
            )  
            return self._handle_raw_response(  
                res,  
                raw_response=raw_response,  
                model_parameters=model_parameters,  
            )  
  
    @observe  
    def generate(  
        self,  
        prompt: str,  
        schema: Type[BaseModel] = None,  
        raw_response: bool = False,  
        *args,  
        **kwargs,  
    ):  
        # Split effective params from remaining kwargs to avoid duplicates downstream  
        params_dict, remaining_kwargs = self._split_effective_kwargs(kwargs)  
        messages = [{"role": "user", "content": prompt}]  
        get_client().update_current_generation(input=messages, model_parameters=params_dict)  
  
        return self.generate_from_messages(  
            messages=messages,  
            schema=schema,  
            raw_response=raw_response,  
            *args,  
            **params_dict,  
            **remaining_kwargs,  
        )  
  
    @observe(  
        as_type="generation",  
    )  
    @retry(  
        wait=wait_fixed(settings.WAIT_DELAY),  
        stop=stop_after_attempt(settings.STOP_AFTER_ATTEMPT),  
        retry=retry_if_exception(should_retry_on_exception),  
    )  
    def generate_from_messages(  
        self,  
        messages: list,  
        schema: Type[BaseModel] = None,  
        raw_response: bool = False,  
        *args,  
        **kwargs,  
    ):  
        # Build and attach model parameters once (only effective LLM params)  
        model_parameters, remaining_kwargs = self._split_effective_kwargs(kwargs)  
        get_client().update_current_generation(input=messages, model_parameters=model_parameters)  
  
        # check if model supports structured output  
        if schema:  
            if self.supports_response_schema:  
                res = litellm.completion(  
                    model=self.model_name,  
                    api_key=self.api_key.get_secret_value(),  
                    base_url=self.base_url,  
                    messages=messages,  
                    response_format=schema,  
                    api_version=self.api_version,  
                    *args,  
                    **model_parameters,  
                    **remaining_kwargs,  
                )  
                return self._handle_schema_response(  
                    res,  
                    schema=schema,  
                    raw_response=raw_response,  
                    model_parameters=model_parameters,  
                    include_model_parameters=False,  
                )  
  
            else:  
                client = instructor.from_litellm(completion, mode=instructor.Mode.JSON)  
                res, raw_completion = client.chat.completions.create_with_completion(  
                    model=self.model_name,  
                    api_key=self.api_key.get_secret_value(),  
                    base_url=self.base_url,  
                    messages=messages,  
                    response_model=schema,  
                    api_version=self.api_version,  
                    *args,  
                    **model_parameters,  
                    **remaining_kwargs,  
                )  
                get_client().update_current_generation(  
                    model=self.model_name,  
                    model_parameters=model_parameters,  
                    **update_langfuse_cost(  
                        num_input_tokens=raw_completion.usage.prompt_tokens,  
                        num_output_tokens=raw_completion.usage.completion_tokens,  
                        total_tokens=raw_completion.usage.total_tokens,  
                        total_cost=raw_completion._hidden_params["response_cost"],  
                        model=self.model_name,  
                    ),  
                )  
                if raw_response:  
                    return raw_completion  
                return res  
        else:  
            res = litellm.completion(  
                model=self.model_name,  
                api_key=self.api_key.get_secret_value(),  
                base_url=self.base_url,  
                messages=messages,  
                api_version=self.api_version,  
                *args,  
                **model_parameters,  
                **remaining_kwargs,  
            )  
            return self._handle_raw_response(  
                res,  
                raw_response=raw_response,  
                model_parameters=model_parameters,  
            )  
  
    def get_model_name(self, *args, **kwargs) -> str:  
        return self.model_name  
  
  
# todo: rename this  
class JudgeLLMConfig(InferenceLLMConfig):  
    """Configuration for the Judge LLM. This class is a subclass of InferenceLLMConfig.  
  
    Doesn't need description and prompts in the config file. Deepeval will use this class.    """  
    # These fields are not used    temperature: float = 0  
    description: str = None  
    prompts: list[str] = None  
  
  
class EmbeddingLLMConfig(AbstractLLMConfig, DeepEvalBaseEmbeddingModel):  
    """Configuration for the embedding model."""  
  
    def load_model(self, prompt: str, schema: Type[BaseModel] = None, *args, **kwargs):  
        pass  
  
    def embed_text(self, text: str) -> List[float]:  
        response = embedding(  
            model=self.model_name,  
            api_base=self.base_url,  
            api_key=self.api_key.get_secret_value(),  
            input=[text],  
        )  
        return response.data[0]["embedding"]  
  
    def embed_texts(self, texts: List[str]) -> List[List[float]]:  
        response = embedding(  
            model=self.model_name,  
            api_base=self.base_url,  
            api_key=self.api_key.get_secret_value(),  
            input=texts,  
        )  
        return [data.embedding for data in response.data]  
  
    async def a_embed_text(self, text: str) -> List[float]:  
        response = await aembedding(  
            model=self.model_name,  
            api_base=self.base_url,  
            api_key=self.api_key.get_secret_value(),  
            input=[text],  
        )  
        return response.data[0]["embedding"]  
  
    async def a_embed_texts(self, texts: List[str]) -> List[List[float]]:  
        response = await aembedding(  
            model=self.model_name,  
            api_base=self.base_url,  
            api_key=self.api_key.get_secret_value(),  
            input=texts,  
        )  
        return [data.embedding for data in response.data]  
  
    def get_model_name(self):  
        return self.model_name  
  
  
@observe(name="generate actual outputs")  
async def fetch_responses(inputs, llm, schema=None, *args):  
    # logger.exception(f" langfuse_context is {langfuse_context}")  
    tasks = [llm.a_generate(user_prompt, schema=schema) for user_prompt in inputs]  
    return await asyncio.gather(*tasks)  
  
  
# @observe(name="generate actual outputs")  
# async def fetch_responses_with_cache(inputs, llm, schema=None, *args):  
#     logger.info(f" Fetching responses from {llm.model_name}")  
#     # Cache to store results of inference  
#     cache = {}  
#  
#     async def get_response(user_prompt):  
#         if user_prompt in cache:  
#             return cache[user_prompt]  
#         else:  
#             try:  
#                 response = await llm.a_generate(user_prompt, schema=schema)  
#             except (  
#                 litellm.exceptions.ContentPolicyViolationError,  
#                 AttributeError,  
#                 ValueError,  
#             ) as e:  
#                 logger.error(e)  
#                 return e  
#  
#             cache[user_prompt] = response  
#             return response  
#  
#     tasks = [get_response(user_prompt) for user_prompt in inputs]  
#     return await tqdm_asyncio.gather(*tasks)  
  
  
class NewDataset(BaseModel):  
    inputs: list[Any]  
  
  
class SynthesizerLLMConfig(JudgeLLMConfig):  
    """Configuration for the Synthesizer LLM.  
  
    This LLM is responsible for generating a dataset following a given prompt    """  
    sys_prompt: str  
    prompt_template: str  
    user_prompt_example: str  
    assistant_response_example: str  
    prompt: Optional[str] = None  # will be generated  
  
    disable_structured_output: bool = False  
    completion_params: dict = dict()  
    languages: Sequence[str] = ("en",)  
    temperature: float = 0.7  
    # not required for synthesizer  
    prompts: list[dict] = None  
  
    # Uses parent _build_effective_params from InferenceLLMConfig  
  
    async def generate_dataset_json_mode(self) -> DataFrame:  
        messages = [  
            ChatMessage(role="system", content=self.sys_prompt),  
            ChatMessage(role="user", content=self.user_prompt_example),  
            ChatMessage(role="assistant", content=self.assistant_response_example),  
            ChatMessage(role="user", content=self.prompt),  
        ]  
        # todo: add async  
        try:  
            out = await litellm.acompletion(  
                model=self.model_name,  
                messages=[{"role": message.role, "content": message.content} for message in messages],  
                api_version=self.api_version,  
                api_key=self.api_key.get_secret_value(),  
                base_url=self.base_url,  
                **self._build_effective_params(  
                    temperature=self.temperature,  
                    max_completion_tokens=self.max_completion_tokens,  
                    seed=self.seed,  
                    reasoning_effort=self.reasoning_effort,  
                ),  
                response_format=_get_response_format("json_object"),  
                # **self.completion_params,  
            )  
            if out.choices[0].finish_reason != "stop":  
                response_message = None  
                logger.error(f"Synthetic data generation did not finish correctly: {out.choices[0].finish_reason}")  
            else:  
                response_message = out.choices[0].message  
                if format in ("json", "json_object"):  
                    # Max 3 attempts to parse the JSON output  
                    for i in range(3):  
                        try:  
                            json_dict = _parse_json_output(  
                                response_message.content,  
                                self,  
                            )  
                            response_message.content = json.dumps(json_dict)  
                            break  
                        except ValueError as e:  
                            if i == 2:  
                                raise e  
                            response_message = out.choices[i + 1].message  
                            continue  
  
                response_message = ChatMessage(role=response_message.role, content=response_message.content)  
            if response_message:  
                generated = _parse_output(response_message.content)  
                df = pd.DataFrame(generated)  
            else:  
                df = pd.DataFrame()  
  
        except TypeError:  
            logger.error(f"Error in generating dataset. The returned output is probably not a valid json object.")  
            df = pd.DataFrame()  
  
        except Exception:  
            logger.exception(f"Error in generating dataset")  
            df = pd.DataFrame()  
  
        return df  
  
    async def generate_dataset_instructor(  
        self,  
    ) -> DataFrame:  
        """Generates a test dataset for the model.The client is wrapped in Instructor."""  
        messages = [  
            {"role": "system", "content": self.sys_prompt},  
            {"role": "user", "content": self.user_prompt_example},  
            {"role": "assistant", "content": self.assistant_response_example},  
            {"role": "user", "content": self.prompt},  
        ]  
        # todo: add async  
        # todo: use generate method  
        try:  
            logger.debug(f"Generating dataset using Instructor library for model: {self.model_name}")  
            out = await self.a_generate_from_messages(  
                messages=messages,  
                schema=NewDataset,  
                **self._build_effective_params(  
                    max_completion_tokens=self.max_completion_tokens,  
                    seed=self.seed,  
                    reasoning_effort=self.reasoning_effort,  
                ),  
            )  
            df = pd.DataFrame(out.inputs)  
        except (AttributeError, litellm.BadRequestError, instructor.exceptions.InstructorRetryException):  
            # If the model fails to generate the dataset using Instructor, it will fallback to the original method  
            try:  
                df = await self.generate_dataset_json_mode()  
            except Exception as e:  
                logger.exception(f"Error in generating dataset: {e}")  
                df = pd.DataFrame()  
  
        except Exception as e:  
            logger.exception(f"Error in generating dataset: {e}")  
            df = pd.DataFrame()  
  
        finally:  
            return df  
  
  
def _get_response_format(format):  
    if format is None:  
        return None  
  
    if format in ("json", "json_object"):  
        return {"type": format}  
  
    logger.warning(f"Unsupported format '{format}', ignoring.")  
    return None  
  
  
def _trim_json(response_message: str):  
    if "{" not in response_message or "}" not in response_message:  
        return response_message  
  
    json_start = response_message.index("{")  
    json_end = len(response_message) - response_message[::-1].index("}")  
  
    return response_message if json_start > json_end else response_message[json_start:json_end]  
  
  
def _parse_json_output(  
    raw_json: str,  
    llm_client: SynthesizerLLMConfig,  
    keys: Optional[Sequence[str]] = None,  
) -> dict:  
    try:  
        return json.loads(_trim_json(raw_json), strict=False)  
    except json.JSONDecodeError:  
        logger.debug("JSON decoding error, trying to fix the JSON string.")  
  
    logger.debug("Raw output: %s", raw_json)  
    # if it's just a matter of markdown format (```json ... ```)  
    match = re.search(r"```json\s{0,5}(.*?)\s{0,5}```", raw_json, re.DOTALL)  
    if match:  
        try:  
            return json.loads(match.group(1), strict=False)  
        except json.JSONDecodeError:  
            logger.debug("String matching didn't fix the format, trying to fix it with the LLM itself.")  
  
    # Final attempt, fix the JSON with the LLM itself  
    out = llm_client.generate(  
        prompt=raw_json,  
        temperature=0,  
    )  
    logger.warning(f" outt is {out}")  
    # generate() returns a string when raw_response=False  
    parsed_dict = json.loads(_trim_json(out), strict=False)  
  
    if keys is not None and any([k not in parsed_dict for k in keys]):  
        raise ValueError(f"Keys {keys} not found in the JSON output: {parsed_dict}")  
  
    return parsed_dict  
  
  
def _parse_output(raw_output: str, output_key="inputs"):  
    try:  
        # Remove trailing commas from the raw output  
        raw_output_cleaned = re.sub(r",(\s*[}\]])", r"\1", raw_output)  
        data = json.loads(raw_output_cleaned)  
        if output_key:  
            data = data[output_key]  
    except (json.JSONDecodeError, KeyError) as err:  
        logger.error(f"Parsing the output failed: {err}")  
        logger.error(f"Raw output: {raw_output}")  
  
        return []  
    return data

```

### pricing

```python
  
LITELLM_PRICING_URL = (  
    "https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json"  
)  
  
_LITELLM_PRICES_CACHE: Optional[dict[str, Any]] = None  
  
  
def fetch_litellm_prices(url: str = LITELLM_PRICING_URL) -> dict[str, Any]:  
    global _LITELLM_PRICES_CACHE  
    if _LITELLM_PRICES_CACHE is not None:  
        return _LITELLM_PRICES_CACHE  
    r = requests.get(url, timeout=30)  
    r.raise_for_status()  
    data: Any = r.json()  
    if not isinstance(data, dict):  
        raise ValueError("Unexpected LiteLLM pricing JSON format (expected a JSON object)")  
    _LITELLM_PRICES_CACHE = data  
    return _LITELLM_PRICES_CACHE  
  
  
def lookup_litellm_model_entry(prices: dict[str, Any], name: str) -> Optional[dict[str, Any]]:  
    if not prices or not name:  
        return None  
    name = str(name).strip()  
    if not name:  
        return None  
  
    if name in prices:  
        entry = prices.get(name)  
        return entry if isinstance(entry, dict) else None  
  
    key_map = {str(k).lower(): k for k in prices.keys()}  
    key = key_map.get(name.lower())  
    if key is not None:  
        entry = prices.get(key)  
        return entry if isinstance(entry, dict) else None  
  
    parts = name.split("/")  
    suffix = parts[-1] if parts else name  
    suffix_lower = suffix.lower()  
  
    candidates: list[str] = []  
    for k in prices.keys():  
        k_str = str(k)  
        if suffix_lower in k_str.lower():  
            candidates.append(k_str)  
  
    if not candidates:  
        return None  
  
    candidates.sort(key=lambda x: (len(x), x.lower()))  
    entry = prices.get(candidates[0])  
    return entry if isinstance(entry, dict) else None

```
