Author : Amine DJEGHRI


- [[#Promptfoo|Promptfoo]]
- [[#LangSmith (by LangChain)|LangSmith (by LangChain)]]
- [[#Langfuse|Langfuse]]
		- [[#What are the main differences between Langfuse and Langsmith|What are the main differences between Langfuse and Langsmith]]
- [[#Langfuse#DeepEval (by ConfidentAI)|DeepEval (by ConfidentAI)]]
- [[#Langfuse#Giskard (by Giskard-AI)|Giskard (by Giskard-AI)]]
- [[#Langfuse#Prompt-flow Tracing (by Azure)|Prompt-flow Tracing (by Azure)]]
- [[#Langfuse#Validate (by Tonic)|Validate (by Tonic)]]
- [[#Langfuse#AutoRAG|AutoRAG]]
- [[#Evaluation benchmarks|Evaluation benchmarks]]

| Features                  | Promptfoo                    | Langsmith                 | Langfuse | Giskard |
| ------------------------- | ---------------------------- | ------------------------- | -------- | ------- |
| **review date**           | 21/11/2024                   | 27/11/2024                |          |         |
| **reviewed** **version**  | 0.99                         | 0.8                       |          |         |
| **Price**                 | NA                           | NA / 39$ um / NA          |          |         |
| **Licence**               | Free/ entreprise/ on-premise | Developer/Plus/entreprise |          |         |
| **deployment**            | local, docker, cloud         |                           |          |         |
| **viz tool**              | cli, web                     |                           |          |         |
| **type/runtime**          | Nodejs package               | NA                        |          |         |
| **Updates frequency**     | 3 days                       | 2 months                  | 3 days   |         |
| **Maturity**              | New, evolving                |                           |          |         |
| **Popularity**            | +40k devs, 5k github stars   | +250k devs                |          |         |
| **Privacy/Data**          | ✅                            | ⚠️                        |          |         |
| **Evaluation**            |                              |                           |          |         |
| - Custom/override models  | ✅                            |                           |          |         |
| - Pre-implemented metrics | ✅                            |                           |          |         |
| - Custom metrics          | ✅                            |                           |          |         |
| - Annotate/Human feedback | ✅                            |                           |          |         |
| - Real time evaluation    | ❌                            |                           |          |         |
| - export format           | json                         |                           |          |         |
| **Redteaming**            |                              |                           |          |         |
| - Custom/override models  | 3/4                          |                           |          |         |
| - Pre-implemented metrics | ✅ (+30)                      |                           |          |         |
| - custom metrics          | ✅                            |                           |          |         |
| - Annotate/Human feedback | ✅                            |                           |          |         |
| **Dataset generation**    | ❌                            |                           |          |         |
| - generate dataset        | ⚠️ (config. only)            |                           |          |         |
| - Annotate/Human feedback | ❌                            |                           |          |         |
| - export format           | yaml                         |                           |          |         |
| **Prompt generation**     | ❌                            |                           |          |         |
| **Monitoring**            | ✅ (paid)                     |                           |          |         |
| **CI/CD**                 | ✅                            |                           |          |         |
| **Easy to use**           | easy                         | easy                      |          |         |
| **Easy to learn**         | medium                       | easy                      |          |         |
|                           |                              |                           |          |         |

### Promptfoo 
Provides 2 tools in one npm package : LLM Evaluation tool & Readteam tool

- **Site** : https://www.promptfoo.dev/
- **Review date** : 21/11/2024
- **version** : 0.99
- **Description**: an [open-source](https://github.com/promptfoo/promptfoo) CLI and library for evaluating and red-teaming LLM apps.
  With promptfoo, you can:
	- Build reliable prompts, models, and RAGs with benchmarks specific to your use-case
	- Secure your apps with automated [red teaming](https://www.promptfoo.dev/docs/red-team/) and pentesting
	- Speed up evaluations with caching, concurrency, and live reloading
	- Score outputs automatically by defining [metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)
	- Use as a [CLI](https://www.promptfoo.dev/docs/usage/command-line/), [library](https://www.promptfoo.dev/docs/usage/node-package/), or in [CI/CD](https://www.promptfoo.dev/docs/integrations/github-action/)
	- Use OpenAI, Anthropic, Azure, Google, HuggingFace, open-source models like Llama, or integrate custom API providers for [any LLM API](https://www.promptfoo.dev/docs/providers/)
  Test your prompts, agents, and RAGs. Red teaming, pentesting, and vulnerability scanning for LLMs. Compare performance of GPT, Claude, Gemini, Llama, and more. Simple declarative configs with command line and CI/CD integration.
  It provides 2 main features : 
	- [**Red teaming**](https://www.promptfoo.dev/docs/red-team/quickstart/) - LLM security scans
	- [**Evaluations**](https://www.promptfoo.dev/docs/getting-started/) - LLM quality benchmarks
- **FAQ** : https://www.promptfoo.dev/docs/faq/
- **Docs**: [docs](https://www.promptfoo.dev/docs/intro/)
- **GitHub**: https://github.com/promptfoo/promptfoo
- **Price**  
	- Free for all features 
	- paid  for cloud based support and custom stuff
	- Licensing: Free, Entreprise, On-premise
	- price site : https://www.promptfoo.dev/pricing/
	- Free Forever : 
		- All LLM evaluation features
		- All model providers and integrations
		- No usage limits
		- Custom integration with your own app
		- Run locally or self-host on your own infrastructure
		- Vulnerability scanning
		- Community support
	- Enterprise : For teams that need advanced features and cloud-based support
		- All Community features
		- Team sharing & collaboration
		- Continuous monitoring
		- Centralized security/compliance dashboard
		- Customized red teaming plugins
		- SSO and Access Control
		- Cloud deployment
		- Priority support & SLA guarantees
	- On-Premise : For organizations that require full control over their infrastructure
		- All Enterprise features
		- Deployment on your own infrastructure
		- Complete data isolation
		- Dedicated support team

- **Deployment**: 
	- Local 
	- Cloud 
	- Docker 
	- `share` command creates a publicly accessible URL, which means anyone who knows the URL can view your results. If you don't want anyone to see your results, you should keep your URL secret. After 2 weeks, all data associated with the URL is permanently deleted.
	- **Visualization Tools**: Web-based interface, CLI 
- **Type/runtime** : NodeJS
- **Updates & Maintenance**: Regular updates as features are improved and expanded.
	- **Support Channel**: Discord, Email support, Github , book a time
	- **Frequency of Updates**: 3 times a week
	- **Community Support**: GitHub repository with active issues, forums for discussions.
	- **Popularity/GitHub Stars**: +40k devs, 5k stars
	- **Maturity**: Relatively new but rapidly evolving with a growing user base 
	- **Used by** : Pomptfoo has run 16 million probes this year at companies like Shopify Doordash Anthropic Microsoft Discord
	- **Team** : 4
-
- **Privacy & Security**: 
	- **Data Handling**: Local, if cloud → Check the pricing
	- **Compliance / Data Location**:  Local, if cloud → Check the pricing
	- **Telemetry** :  You can disable all data being sent to Promptfoo by using the following environment variables: 
		- PROMPTFOO_DISABLE_UPDATE=1: Disables version checks (only sends your current version, nothing else). 
		- PROMPTFOO_DISABLE_REDTEAM_REMOTE_GENERATION=1: Disables the inference endpoint used for unaligned models (covers a subset of harmful plugins and some security plugins). 
		- PROMPTFOO_DISABLE_SHARING=1: Requires explicit opt-in when using the promptfoo share command. 
		- PROMPTFOO_DISABLE_TELEMETRY=1: Disables all telemetry data.
	   
- **Features**:
	- **Evaluation** :
		- **Generator  & Evaluator models** : used to generate, evaluate an output
			- **Model Compatibility**:  Yes. https://www.promptfoo.dev/docs/providers/
			- **Custom/override models**: Yes
		- **Metrics**: Yes. https://www.promptfoo.dev/docs/configuration/expected-outputs/
			- **pre-implemented metrics** : yes
				- deterministic metrics : contains, equals, exact-match Yes
				- model-graded metrics : using LLM to evaluate Yes
					- override prompts : yes
					- override Evaluator/grader : yes. https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/#overriding-the-llm-grader
			- **Qualitative & Quantitative Metrics**: both (score or llm-based)
			- **Custom Metrics**: Yes. Either in the config or external .py or .js scripts
		- **Annotate/Human feedback**: Yes (vote, set score, comment)
		- **Use Human Feedback** : No
		- **Real time / Dynamic Evaluation**: No
		- **Easy Unit Test (like pytest)**: Yes. with a command a config script or webui
		- **Pre-implemented Dataset Benchmarks**: ·No default datasets. On your own data only. side-by-side comparison view
		- **Export Formats**:  JSON
		- **Visualization Tools**: Web-based interface, CLI 
	- **Redteam**: 
		- **Doc** : https://www.promptfoo.dev/docs/red-team/quickstart/
		- **Models** :  Generator, evaluator, attacker, unaligned models 
			- **model compatibility** Yes, only 3 models (https://www.promptfoo.dev/docs/red-team/configuration/#providers)
				-  Custom/Override Attacker models (used to generated adversial outputs) https://www.promptfoo.dev/docs/red-team/configuration/#providers
				- Custom/Override Grader/evaluator : https://www.promptfoo.dev/docs/guides/llm-redteaming/#configuring-the-grader
				- Unaligned model : some plugins like the hamrful plugins use promptfoo free models and can not yet be overriden. You need to remove PROMPTFOO_DISABLE_REDTEAM_REMOTE_GENERATION=True from your env to use these plugins.
			- **Custom/override models** :Only the first 3 models.
		- **Metrics** : Yes, called plugins. 
			- https://www.promptfoo.dev/docs/category/red-teaming/ 
			- **Pre-implemented metrics** : Yes. 
				- Scan +30 vulnerabilities type. Some plugins (harmful and security) use promptfoo unaligned  uncensored models and send data to their cloud  but can be deactivated.
			- **Custom Metrics** : Yes . https://www.promptfoo.dev/docs/red-team/configuration/#custom-plugins
		-  **Annotate/Human feedback**: Yes (vote, set score, comment)
		- **Use Human Feedback** : No
		- **Export Formats**:  JSON
		- **Visualization Tools**: Web-based interface, CLI 
	- **Monitoring**:  Continuous monitoring and Comprehensive Scanning & Compliance are paid and only available in entreprise + on-premise tiers (check the pricing page )
	- **CI/CD**: Yes and has also github actions support. https://www.promptfoo.dev/docs/integrations/ci-cd/
	- **Dataset Generation**:  No
		- **Generate datasets** : No. Only generates configs. https://www.promptfoo.dev/docs/configuration/datasets/
		-  **Annotate/Human feedback**: No
		- **Use human feedback** : No
		- **Export Formats**:  Yaml
		- **Visualization Tools**: web base, file
	- **Prompt engineering** :  ??
	- **Easy to Use**: Easy
	- **Easy to learn** : Medium
        
		

### LangSmith (by LangChain)
Provides an all in one platform for every stem of the LLM-powered application lifecycle.

- **Site** : https://www.langchain.com/langsmith
- **Review date** : 27/11/2024
- **version** : 0.8
- **Description**: An all in one platform : 
	    - Traces, hub, annotation, datasets
	    - Collaborate with teammates
	    - Layer in human feedback on runs or use AI-assisted evaluation
	    - Dataset Construction :Quickly save debugging and production traces to datasets. 
	    - Auto-evaluation : Use an LLM and prompt to score your application output, or write your own functional evaluation tests to record different measures of effectiveness.
	    - Regression testing :See how performance of the evaluation criteria that you've defined is affected by changes to your application.
	    - Online evaluation : Continuously track qualitative characteristics of any live application, and spot issues in real-time with LangSmith monitoring.
	    - monitor cost, latency, quality
- **FAQ** : https://www.langchain.com/langsmith (at the bottom)
- **Docs**: [docs](https://docs.smith.langchain.com/)
- **GitHub**: https://github.com/promptfoo/promptfoo
- **Price**  
	- Free for all features 
	- Licensing: Startups, Developer, Plus, Entreprise
	- price site :https://www.langchain.com/pricing-langsmith
    - **Developer**:
        - 1 Developer seat
        - Debugging traces
        - Dataset collection
        - Testing and evaluation
        - Prompt management
        - Monitoring
    - **Plus**: 39$/user/month
        - All features in Developer tier
        - Up to 10 seats
        - Higher rate limits
        - Email support
    - **Enterprise**:
        - All features in Plus tier
        - Custom Single Sign On (SSO)
        - SLA
        - Self-hosted deployment options
        - Custom rate limits
        - Team trainings
        - Shared Slack channel
        - Architectural guidance
        - Dedicated customer success manager

- **Deployment**: 
	- Cloud 
	- Self-Host (paid)
- **Type/runtime** : NA
- **Updates & Maintenance**: Regular updates as features are improved and expanded.
	- **Support Channel**: Discord, Email support, Github , book a time
	- **Frequency of Updates**: every two months
	- **Community Support**: Langchain community
	- **Popularity/GitHub Stars**: +250k users, +25k monthly active teams, Langchain has 100K stars.
	- **Maturity**: In beta but is enough mature in terms of features. A langchain company product.
	- **Used by** : 
	- **Team** : 20-60 ?
-
- **Privacy & Security**: 
	- **Data Handling**: - Cloud or self-host(paid). If cloud, we will not train on your data, and you own all rights to your data. See LangSmith [Terms of Service](https://www.langchain.com/terms-of-service) for more information.
	- **Compliance / Data Location**: cloud : Traces are stored in GCP us-central-1. Organizations' traces are logically separated from each other in a Clickhouse database and encrypted in transit and at rest.
	- **Telemetry** :  NA
	   
- **Features**:
	- **Evaluation** :
		- **Generator  & Evaluator models** : used to generate, evaluate an output
			- **Model Compatibility**:  Yes. https://www.promptfoo.dev/docs/providers/
			- **Custom/override models**: Yes
		- **Metrics**: Yes. https://www.promptfoo.dev/docs/configuration/expected-outputs/
			- **pre-implemented metrics** : yes
				- deterministic metrics : contains, equals, exact-match Yes
				- model-graded metrics : using LLM to evaluate Yes
					- override prompts : yes
					- override Evaluator/grader : yes. https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/#overriding-the-llm-grader
			- **Qualitative & Quantitative Metrics**: both (score or llm-based)
			- **Custom Metrics**: Yes. Either in the config or external .py or .js scripts
		- **Annotate/Human feedback**: Yes (vote, set score, comment)
		- **Use Human Feedback** : No
		- **Real time / Dynamic Evaluation**: No
		- **Easy Unit Test (like pytest)**: Yes. with a command a config script or webui
		- **Pre-implemented Dataset Benchmarks**: ·No default datasets. On your own data only. side-by-side comparison view
		- **Export Formats**:  JSON
		- **Visualization Tools**: Web-based interface, CLI 
	- **Redteam**: 
		- **Doc** : https://www.promptfoo.dev/docs/red-team/quickstart/
		- **Models** :  Generator, evaluator, attacker, unaligned models 
			- **model compatibility** Yes, only 3 models (https://www.promptfoo.dev/docs/red-team/configuration/#providers)
				-  Custom/Override Attacker models (used to generated adversial outputs) https://www.promptfoo.dev/docs/red-team/configuration/#providers
				- Custom/Override Grader/evaluator : https://www.promptfoo.dev/docs/guides/llm-redteaming/#configuring-the-grader
				- Unaligned model : some plugins like the hamrful plugins use promptfoo free models and can not yet be overriden. You need to remove PROMPTFOO_DISABLE_REDTEAM_REMOTE_GENERATION=True from your env to use these plugins.
			- **Custom/override models** :Only the first 3 models.
		- **Metrics** : Yes, called plugins. 
			- https://www.promptfoo.dev/docs/category/red-teaming/ 
			- **Pre-implemented metrics** : Yes. 
				- Scan +30 vulnerabilities type. Some plugins (harmful and security) use promptfoo unaligned  uncensored models and send data to their cloud  but can be deactivated.
			- **Custom Metrics** : Yes . https://www.promptfoo.dev/docs/red-team/configuration/#custom-plugins
		-  **Annotate/Human feedback**: Yes (vote, set score, comment)
		- **Use Human Feedback** : No
		- **Export Formats**:  JSON
		- **Visualization Tools**: Web-based interface, CLI 
	- **Monitoring**:  Continuous monitoring and Comprehensive Scanning & Compliance are paid and only available in entreprise + on-premise tiers (check the pricing page )
	- **CI/CD**: Yes and has also github actions support. https://www.promptfoo.dev/docs/integrations/ci-cd/
	- **Dataset Generation**:  No
		- **Generate datasets** : No. Only generates configs. https://www.promptfoo.dev/docs/configuration/datasets/
		-  **Annotate/Human feedback**: No
		- **Use human feedback** : No
		- **Export Formats**:  Yaml
		- **Visualization Tools**: web base, file
	- **Prompt engineering** :  ??
	- **Easy to Use**: Easy
	- **Easy to learn** : Easy


## Langfuse
##### What are the main differences between Langfuse and Langsmith

- Langfuse is open source while LangSmith is a closed source project.
- LangSmith is developed by the LangChain team and integrates very well with the LangChain framework. Langfuse also maintains [Langchain integrations](https://langfuse.com/docs/integrations/langchain/tracing).
- Langfuse maintains a [large number of integrations](https://langfuse.com/docs/integrations/overview) into many frameworks and libraries. Langsmith focuses on its Langchain integration.
- Langfuse can be [freely self hosted](https://langfuse.com/docs/deployment/self-host) at no cost while LangSmith needs to be purchased to be self hosted.
- Comparaison with langsmith : https://astralinsights.ai/wp-content/uploads/2024/06/AI-Comparison-White-Paper-June-2024.pdf

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
### Giskard (by Giskard-AI)

### Prompt-flow Tracing (by Azure)
### Langfuse
### Validate (by Tonic)
### AutoRAG





