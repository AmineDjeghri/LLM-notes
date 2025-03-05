
## Azure OpenAI and Azure AI Foundry: 

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

| Name                   | Azure AI Inference | LiteLLM | LiteLLM+ Instructor instructor.Mode.JSON | Azure OpenAI (parse) | Azure OpenAI |     |
| ---------------------- | ------------------ | ------- | ---------------------------------------- | -------------------- | ------------ | --- |
| gpt-4o-mini-2024-07-18 | N/A                | ✅       | ✅                                        | ✅                    | ✅            |     |
| gpt-4o-2024-05-13      | N/A                | ❌       | ✅                                        | ❌                    | ✅            |     |
| o1-2024-12-17          | N/A                | ✅       | ✅                                        | ✅                    | ✅            |     |
| o1-mini-2024-09-12     | N/A                | ❌       | ✅                                        | ❌                    | ❌            |     |
| o3-mini-2025-01-31     | N/A                | ✅       | ✅                                        | ✅                    | ✅            |     |

- Structured Outputs with `response_format: {type: "json_schema", ...}` /pydantic is only supported with the `gpt-4o-mini`, `gpt-4o-mini-2024-07-18`, and `gpt-4o-2024-08-06` model snapshots and later.
- Models like o1-mini do not support structured output. See [link](https://github.com/MicrosoftDocs/azure-ai-docs/blob/main/articles/ai-foundry/model-inference/concepts/models.md#azure-openai) 
Commentaires : 
- Il faut déployer les dernières versions des modèles 
- il faut enlever le content filtering
- il faut faire attention à l’api version.
- I recommend calling gpt4o/mini after the result to extract json as structured output as this is supported from 08/09 model versions

Other models : 

| Name                                     | Azure AI Inference | LiteLLM     | LiteLLM + Instructor | ollama + instructor |
| ---------------------------------------- | ------------------ | ----------- | -------------------- | ------------------- |
| Mistral-Large-2411                       |                    |             |                      |                     |
| Mistral-Small                            |                    |             |                      |                     |
| Phi-4                                    | ❌(Timeout)         |             |                      |                     |
| DeepSeek-R1                              |                    |             |                      |                     |
| phi35-mini-instruct                      | ❌ (Timeout)        | ❌ (timeout) |                      |                     |
| ollama/phi-3.5-uncensored                | N/A                |             |                      |                     |
| ollama/qwen2.5:0.5b                      | N/A                |             |                      |                     |
| ollama/phi3:3.8b-mini-4k-instruct-q4_K_M | N/A                |             |                      |                     |
