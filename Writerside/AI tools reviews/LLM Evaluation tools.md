
| Tool name | Description | Hosting | Benchmark | Evaluation | Redteam | monitoring | CLI | UI  | runtime |
| --------- | ----------- | ------- | --------- | ---------- | ------- | ---------- | --- | --- | ------- |
| Promptfoo |             | Local   |           |            | ✅       |            |     |     | nvm     |
| Langsmith |             |         |           |            |         |            |     |     |         |
| Giskard   |             |         |           |            |         |            |     |     | pip     |
| DeepEval  |             |         |           |            | ✅       |            |     |     | pip     |
|           |             |         |           |            |         |            |     |     |         |
|           |             |         |           |            |         |            |     |     |         |



langsmith : 
	- test  
	- est ce que les données sont secure meme si on utilise nos modèles
	- est ce que les données sont dans un tenant

- Giskard feature 
- comparer les features
- Giskard (free vs paid)
- utiliser Giskard avec openai (emulation openai)
- Giskard vs Promptfoo (free vs free)


dspy

Every tool has this fields of comparaison : 
- Package / web platform (separate them if they are different or if they have different prices):
	- description
	- site/github
	- docs
	- price & licencing: free, freemium, paid - pricing page 
	- deployment : local, cloud, container
	- Runtime : python, nodejs …
	- Updates & maintenance
		- Support channel
		- Frequency of updates
		-  Community support (github stars, forums, issues,)
		- Maturity
	- Privacy & security:
		- Data handling
		- Compliance / Data location
	- Output & reporting :
		- formats (csv, json)
		- Visualization tools (web server, cli)
	- Features:
		- found in the docs/website
		- metrics
		- Qualitative & quantitative metrics : Does it provide numerical scores, qualitative feedback, or both?
		- custom metrics
		- Readteam
		- Monitoring
		- CI/CD
		- dataset generation
		- easy unit test (like pytest)
		- benchmarks
		- model compatibility 
		- custom models
		- tasks (rag, chatbot, agents)
		- Human in the loop : Does it allow for human evaluation alongside automated metrics?
		- Static & dynamic evaluation : Can it evaluate models in real-time or only after completion?
		- Easy to use
 
## Dashboard & reporting
### Promptfoo
- **LLM Evaluation tool**: 
	- Type : package
    - **Description**: PromptFoo is a tool designed to help users evaluate and optimize prompts for language models, enabling better performance and results in natural language processing tasks.
    - **GitHub**: https://github.com/promptfoo/promptfoo
    - Site : https://www.promptfoo.dev/
    - **Docs**: [Documentation](https://www.promptfoo.dev/docs)
    - **Price & Licensing**: Free
    - **Deployment**: Local
    - **Runtime**: nodejs
    - **Updates & Maintenance**: Regular updates as features are improved and expanded.
    - **Support Channel**: Email support, community forums.
    - **Frequency of Updates**: Monthly
    - **Community Support**: GitHub repository with active issues, forums for discussions.
        - GitHub Stars: Approximately 150+
    - **Maturity**: Relatively new but rapidly evolving with a growing user base (+40k dev)
    -
	- **Privacy & Security**:
	    - **Data Handling**: User data is handled in accordance with privacy standards; specifics can be found in their privacy policy.
	    - **Compliance / Data Location**: GDPR compliant; data is stored in secure cloud environments.  
	        
	- **Output & Reporting**:
	    - **Formats**: CSV, JSON
	    - **Visualization Tools**: Web-based interface, CLI options available for advanced users.  
	        
	- **Features**:
	    - **Found in the docs/website**: Comprehensive documentation available outlining features and usage.
	    - **Metrics**: Provides insights into prompt effectiveness and model performance.
	    - **Qualitative & Quantitative Metrics**: Offers both numerical scores and qualitative feedback.
	    - **Custom Metrics**: Users can define their own evaluation criteria.
	    - **Readteam**: Support for collaborative evaluation.
	    - **Monitoring**: Real-time monitoring of prompt performance.
	    - **CI/CD**: Integrates with CI/CD pipelines for automated evaluations.
	    - **Dataset Generation**: Capable of generating datasets for testing and evaluation purposes.
	    - **Easy Unit Test (like pytest)**: Supports unit testing of prompts and responses.
	    - **Benchmarks**: Provides benchmarking against standard datasets.
	    - **Model Compatibility**: Compatible with various language models (e.g., GPT-3, etc.).
	    - **Custom Models**: Users can integrate their own models for evaluation.
	    - **Tasks**: Supports various tasks including RAG (Retrieval-Augmented Generation) and chatbots.
	    - **Human in the Loop**: Allows for human evaluation alongside automated metrics.
	    - **Static & Dynamic Evaluation**: Capable of evaluating models in real-time.
	    - **Easy to Use**: User-friendly interface designed for quick adoption.  
          
        
		
### Giskard (by Giskard-AI)

### LangSmith (by LangChain)

### DeepEval (by ConfidentAI)
 - Package :
	- <u>Description</u> : 
		- **DeepEval** is a simple-to-use, open-source LLM evaluation framework, for evaluating and testing large-language model systems. It is similar to Pytest but specialized for unit testing LLM outputs. DeepEval incorporates the latest research to evaluate LLM outputs based on metrics such as G-Eval, hallucination, answer relevancy, RAGAS, etc., which uses LLMs and various other NLP models that runs **locally on your machine** for evaluation. 
		- Whether your application is implemented via RAG or fine-tuning, LangChain or LlamaIndex, DeepEval has you covered. With it, you can easily determine the optimal hyperparameters to improve your RAG pipeline, prevent prompt drifting, or even transition from OpenAI to hosting your own Llama2 with confidence.
	- <u>Github</u> : https://github.com/confident-ai/deepeval
	- <u>Docs</u> : https://docs.confident-ai.com/docs/getting-started
	- python package, pip installable
	- features :
		- Easily "unit test" LLM outputs in a similar way to Pytest.
		- Plug-and-use 14+ LLM-evaluated metrics, most with research backing.
		- Synthetic dataset generation with state-of-the-art evolution techniques.
		- Metrics are simple to customize and covers all use cases.
		- Real-time evaluations in production.
		- integrates natively with [Confident AI](https://app.confident-ai.com/)
- Web platform :
	- Cloud only
	- **evaluate, regression test, and monitor** LLM applications on the cloud.
	- site : https://www.confident-ai.com/
	- docs : https://docs.confident-ai.com/docs/confident-ai-introduction
	- paid, only 7 days trial , pricing : https://www.confident-ai.com/pricing
	- 
	
### Prompt-flow Tracing (by Azure)
### Langfuse
### Validate (by Tonic)
### AutoRAG


## Evaluation benchmarks





