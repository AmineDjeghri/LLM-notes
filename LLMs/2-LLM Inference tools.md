Author : Amine DJEGHRI

**Table of content**
- [[#How to estimate the required VRAM to run your model|How to estimate the required VRAM to run your model]]
- [[#AI Inference tools :|AI Inference tools :]]
- [[#LLM quantizations and format|LLM quantizations and format]]


## AI Inference tools : 
- Ollama (Best choice) : 
- LM Studio
- Jan
- GPT4All
- Llama.cpp
- text-generation-webui
- localai
- llamafile

## LLM quantizations and format
- GGUF
- EXL2
- GPTQ
- AWQ

## How to estimate the required VRAM to run your model 
A basic formula to estimate VRAM usage is: **Number of Parameters × (Precision / 8) × 1.2**
(the idea is to convert from bits to bytes)
Example with llama 7b 4KM :
- Number of parameters : 7b 
- How much does each param takes in bytes ? convert precision bit to bytes : 4 / 8 : 4bits take 0.5 bytes. So each parameter takes 0.5 if it is quantized in 4 bits 
- 7B x 0.5 = 3.5 GB (3.5 billion bytes)
- We multiply by 1.2 to add the required bytes of context (approximatively 20% )

