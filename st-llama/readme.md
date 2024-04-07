## To use llama-cpp-python with a gpu
```
install for cuda
needs to have cuda installed and also needs to have an empty environement 
```
pip uninstall llama-cpp-python;
CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python --no-cache;
pip install -r requirements.txt
```



## Langchain with text-generation webui api to run exllama 
Text generation web ui api is similar to openai api. So you can use the same code to run text geenration with exllama.

To use LangChain with Exllama, you can follow the example provided in the LangChain documentation. First, make sure you have the text-generation-webui API integration configured and an LLM (Large Language Model) installed. Then, enable the api option either through the web model configuration tab or by adding the run-time argument --api to your start command.

Next, you can use the LangChain library to interact with LLM models via the text-generation-webui API integration. Here is an example code snippet:
```python
import langchain
from langchain import PromptTemplate, LLMChain
from langchain.llms import TextGen

langchain.debug = True

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm = TextGen(model_url=model_url)
llm_chain = LLMChain(prompt=prompt, llm=llm)
question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"

llm_chain.run(question)
```
Replace model_url with the URL of your LLM model. This code sets up a prompt template with a question variable, creates an LLMChain object with the prompt and LLM, and runs the chain with a specific question.
