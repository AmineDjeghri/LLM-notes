```table-of-contents
```
## Easy guides
- item 1
- item 2

## Tools / libraries 
### Local 
- Ollama 
- vLLM 
- LM Studio 
- Jan
- GPT4All
- Llama.cpp (llama-serve) 
- MLX 
- text-generation-webui
- localai
- llamafile
- llama-swap 

Best UI :


Best Backend
llama-swap with : 
- 


## Papers and research
- item 1
## News and updates
- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/?tl=fr)
## Other resources 
- item 1
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

