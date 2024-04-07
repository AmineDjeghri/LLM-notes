from llama_cpp import Llama

# load llm
# llm = Llama('TheBloke_Llama-2-13B-chat-GGML/llama-2-13b-chat.ggmlv3.q4_K_M.bin', n_gpu_layers=23)
# response = llm('Hello, how are you?')
# print(response['choices'][0]['text'])


from langchain import PromptTemplate, LLMChain
from langchain.llms import LlamaCpp
from langchain.vectorstores import Chroma

from langchain.embeddings import LlamaCppEmbeddings

from loader import get_embeddings

model_path = 'TheBloke_Llama-2-13B-chat-GGML/llama-2-13b-chat.ggmlv3.q4_K_M.bin'
n_gpu_layers = 23
texts, embeddings_model = get_embeddings(model_path=model_path, text_path='file.txt', n_gpu_layers=n_gpu_layers)
db = Chroma.from_documents(documents=texts, embedding=embeddings_model)


print("running search with query")
# load template
template = """ 
Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
{context}
Question : {question}
Answer: 
"""
prompt = PromptTemplate.from_template(template=template)
print(f'input variables : {prompt.input_variables}')

question = "Who is abdenour Chaoui ?"
similar_doc = db.similarity_search(question, k=1)
context = similar_doc[0].page_content
print(context)

llm = LlamaCpp(model_path=model_path, n_gpu_layers=23)
llm_chain = LLMChain(llm=llm, prompt=prompt)
response = llm_chain.run({'context': context, 'question': question})
print(response)
