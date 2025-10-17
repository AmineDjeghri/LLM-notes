Author : Amine DJEGHRI

## LLM Tools
- **LLM platforms (observability**_,_ **evaluation, monitoring) :** 
	- langsmith,
	- langfuse (my selection) 
	- Pheonix Arize,
	- langtrace
	- Helicone
	- MLFlow
- **LLMs testing frameworks** :
	- promptfoo, 
	- giskard, 
	- deep-eval / deepteam (contains G-Eval and Ragas) (my selection) 
	- ragas
	- G-eval
- **Guardrails frameworks** 
	- [guardrails](https://github.com/guardrails-ai/guardrails)

I chose to build a new library based on DeepEval with the logic of config files of promptfoo .
The results will be automatically sent to langsmith if you want after each evaluation.
DeepEval / Promptfoo both provide evaluation and red-teaming features.

## Papers and sources

- [ ] https://medium.com/@heyamit10/langsmith-vs-langfuse-ef3d493ea74e
- [ ] https://github.com/huggingface/evaluation-guidebook
