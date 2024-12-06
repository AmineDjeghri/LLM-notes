Author : Amine DJEGHRI

There are two typle of LLM tools :
- **LLM platform (observability**_,_ **evaluation, monitoring) :** langsmith, langfuse, Pheonix Arize, langtrace, Helicone
- **LLMs testing frameworks** : promptfoo, giskard, deep-eval,  ragas

- [[#Promptfoo|Promptfoo]]
- [[#LangSmith (by LangChain)|LangSmith (by LangChain)]]
- [[#Langfuse|Langfuse]]
- [[#Langfuse#Giskard (by Giskard-AI)|Giskard (by Giskard-AI)]]
- [[#Langfuse#DeepEval (by ConfidentAI)|DeepEval (by ConfidentAI)]]
- [[#Langfuse#Prompt-flow Tracing (by Azure)|Prompt-flow Tracing (by Azure)]]
- [[#Langfuse#Validate (by Tonic)|Validate (by Tonic)]]
- [[#Langfuse#AutoRAG|AutoRAG]]


## Summary 

### comparaison table 

| Features                  | Promptfoo                    | Langsmith                                                  | Langfuse                                                 | Giskard                                       |
| ------------------------- | ---------------------------- | ---------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------- |
| **review date**           | 21/11/2024                   | 27/11/2024                                                 | 29/11/2024                                               | 2/12/2024                                     |
| **reviewed** **version**  | 0.99                         | 0.8                                                        | 2.93                                                     | 2.16.0                                        |
| **Price**                 | NA                           | Free , 39$, Custom                                         | -cloud :free,59,499<br>-self-host:free,100,custom        | Free or ==NM==                                |
| **Licence**               | Free/ entreprise/ on-premise | Developer/Plus/ Entreprise                                 | -Cloud: hobby, pro, team<br>-Self-Host : os, pro, custom | Opensource or Entreprise                      |
| **usage**                 | yaml, code, web(light)       | web, code                                                  | web, code                                                | code, web (extremely light (free))            |
| **deployment**            | local, cloud                 | cloud                                                      | local , cloud(paid)                                      | local or                                      |
| **viz tool**              | cli, web                     | web                                                        | web                                                      | web (extremely light free version)            |
| **local runtime **        | NodeJS or Docker             | N/A                                                        | Docker, cloud: ==NM==                                    | Python                                        |
| **Updates frequency**     | 3 days                       | 2 months                                                   | 3 days                                                   | 2 weeks                                       |
| **Maturity**              | New, evolving                | Beta                                                       | New, evolving                                            | evolving                                      |
| **Popularity**            | +40k devs, 5k github stars   | +250k devs, Langchain community                            | 3m installs /month, 7K stars<br>1.8m docker pulls        | 4k stars GH                                   |
| **Privacy/Data**          | ✅ (local or in cloud)        | -US servers if cloud<br>-On-premise:for entreprise version | ✅ (local or in cloud)                                    | -cloud : ==NM==<br>-on-premise:<br>entreprise |
| **Evaluation**            |                              |                                                            |                                                          |                                               |
| - Custom/override models  | ✅                            | ✅                                                          | ✅                                                        | ✅                                             |
| - Pre-implemented metrics | ✅                            | ⚠️                                                         | ?                                                        | ✅                                             |
| - Custom metrics          | ✅                            | ✅                                                          |                                                          | ✅                                             |
| - Annotate/Human feedback | ✅                            | ✅                                                          | ✅                                                        | ==NM==                                        |
| - Real time evaluation    |                              | ✅                                                          | ✅                                                        | To confirm                                    |
| - export format           | json                         |                                                            |                                                          | json,csv, df,html                             |
| **Redteaming**            |                              |                                                            |                                                          |                                               |
| - Custom/override mmodels | ✅ (3/4)                      | ✅                                                          | ✅                                                        | ✅                                             |
| - Pre-implemented         | ✅ (+30)                      | ⚠️                                                         | ⚠️                                                       | ✅                                             |
| - custom metric           | ✅                            | ✅                                                          | ✅                                                        | ✅                                             |
| - Annotate/Human feedback | ✅                            | ✅                                                          | ✅                                                        | ==NM==                                        |
| **Dataset**               |                              |                                                            |                                                          |                                               |
| - Construct dataset       | ⚠️ (config. only)            | ✅                                                          | ✅                                                        | ✅                                             |
| - Generate dataset        | ❌                            | ✅                                                          | ✅                                                        | ✅                                             |
| **Prompt generation**     | ❌                            | ✅                                                          | ?                                                        | ==NM==                                        |
| **Monitoring**            | ⚠️ (paid)                    | ✅                                                          | ✅                                                        | ✅                                             |
| **CI/CD**                 | ✅                            | ✅                                                          | ✅                                                        | ✅                                             |
| **Difficulty to use**     | easy                         | very easy                                                  | very easy                                                | easy                                          |
| **Difficulty to learn**   | medium                       | easy                                                       | easy                                                     | medium (bugs)                                 |
|                           |                              |                                                            |                                                          |                                               |
### Pre-implemented metrics :

|                    | promptfoo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | giskard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | langfuse                        | langsmith                                                                                                                                                       |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Deterministic      | equals    <br>contains  <br>icontains  <br>regex  <br>starts-with   <br>contains-any  <br>contains-all  <br>icontains-any  <br>icontains-all  <br>is-json   <br>contains-json  <br>is-sql    <br>contains-sql  <br>is-xml  <br>contains-xml  <br>javascript  <br>python    <br>webhook   <br>rouge-n   <br>bleu      <br>levenshtein  <br>latency  <br>perplexity  <br>perplexity-score  <br>cost  <br>is-valid-openai-function-call  <br>is-valid-openai-tools-call                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Metamorphic tests  <br>test_metamorphic_invariance  <br>test_metamorphic_increasing  <br>test_metamorphic_decreasing  <br>test_metamorphic_invariance_t_test  <br>test_metamorphic_increasing_t_test  <br>test_metamorphic_decreasing_t_test  <br>test_metamorphic_invariance_wilcoxon  <br>test_metamorphic_increasing_wilcoxon  <br>test_metamorphic_decreasing_wilcoxon  <br>  <br>Statistical tests  <br>test_right_label  <br>test_output_in_range  <br>test_disparate_impact  <br>test_nominal_association  <br>test_cramer_v  <br>test_mutual_information  <br>test_theil_u  <br>  <br>Performance tests  <br>test_recall  <br>test_auc  <br>test_accuracy  <br>test_precision  <br>test_f1  <br>test_diff_recall  <br>test_diff_accuracy  <br>test_diff_precision  <br>test_diff_f1  <br>test_brier  <br>test_mae  <br>test_rmse  <br>test_diff_rmse  <br>test_r2  <br>  <br>Drift tests  <br>test_drift_psi  <br>test_drift_chi_square  <br>test_drift_ks  <br>test_drift_earth_movers_distance  <br>test_drift_prediction_psi  <br>test_drift_prediction_chi_square  <br>test_drift_prediction_ks  <br>test_drift_prediction_earth_movers_distance  <br>  <br>Stability tests - test_smoothness - test_monotonicity |                                 | -Embedding distance  <br>-String Distance  <br>-Exact Match  <br>-Regex Match  <br>-Json Validity  <br>-Json Equality  <br>-Json Edit Distance <br>-Json Schema |
| LLM as a judge     | -similar  <br>classifier    <br>llm-rubric  <br>answer-relevance      <br>context-faithfulness  <br>context-recall    <br>context-relevance  <br>factuality  <br>model-graded-closedqa     <br>select-best                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Injections  <br>test_llm_char_injection  <br>test_llm_single_output_against_strings  <br>test_llm_output_against_strings  <br>  <br>LLM-as-ajudge  <br>test_llm_output_coherency  <br>test_llm_output_plausibility  <br>test_llm_output_against_requirement_per_row  <br>test_llm_single_output_against_requirement  <br>test_llm_output_against_requirement  <br>  <br>Ground Truth  <br>test_llm_ground_truth  <br>test_llm_ground_truth_similarity  <br>test_llm_as_a_judge_ground_truth_similarity                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                 | conciseness  <br>relevance  <br>correctness  <br>coherence  <br>helpfulness  <br>QA  <br>Contextual Q&A  <br>Chain of Thought Q&A<br>-prompts HUB               |
| Custom             | python, js                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                 |                                                                                                                                                                 |
| Redteam & security | ASCII Smuggling    <br>Broken Function Level Authorization (BFLA)     <br>Broken Object Level Authorization (BOLA)       <br>Chemical & Biological Weapons      <br>Child Exploitation     <br>Competitors    <br>Context Window Overflow    <br>Copyright Violations       <br>Cybercrime and Hacking     <br>Data Exfiltration      <br>Data Poisoning    <br>Excessive Agency       <br>Graphic Content    <br>Hallucination      <br>Harassment and Bullying    <br>Hate and Discrimination    <br>Hijacking      <br>Illegal Drugs      <br>Indiscriminate Weapons     <br>Misinformation and Disinformation      <br>Non-Violent Crimes     <br>Overreliance       <br>PII Exposure       <br>Politics  <br>Prompt extraction  <br>Prompt Injection       <br>Prompt Leak    <br>RAG Poisoning  <br>Religion  <br>Role-Based Access Control (RBAC)       <br>Self-Harm      <br>Server-Side Request Forgery (SSRF)     <br>Sex Crimes     <br>Sexual Content  <br>Shell Injection  <br>Specialized Advice  <br>SQL Injection  <br>Tool/API Manipulation  <br>Unauthorized Access   <br>Unsafe Practices  <br>Violent Crimes | LLMCharsInjectionDetector  <br>LLMPromptInjectionDetector  <br>  <br>LLMBasicSycophancyDetector  <br>LLMImplausibleOutputDetector  <br>  <br>LLMHarmfulContentDetector  <br>  <br>LLMStereotypesDetector  <br>  <br>LLMInformationDisclosureDetector  <br>  <br>LLMOutputFormattingDetector                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                 | maliciousness  <br>controversiality  <br>misogyny  <br>criminality<br>harmfulness  <br>                                                                         |
| Integrations       | -LlamaGuard<br>-Guardrails<br>and more<br>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | -DSPy<br>-Promptfoo<br>and more |                                                                                                                                                                 |
| multi-modal        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                 |                                                                                                                                                                 |
|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                 |                                                                                                                                                                 |
|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                 |                                                                                                                                                                 |
|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                 |                                                                                                                                                                 |
|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                 |                                                                                                                                                                 |
|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                 |                                                                                                                                                                 |
|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                 |                                                                                                                                                                 |
|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                 |                                                                                                                                                                 |
|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                 |                                                                                                                                                                 |
|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                 |                                                                                                                                                                 |
|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                 |                                                                                                                                                                 |
|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                 |                                                                                                                                                                 |
|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                 |                                                                                                                                                                 |
|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                 |                                                                                                                                                                 |
|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                 |                                                                                                                                                                 |
|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                 |                                                                                                                                                                 |

## Promptfoo 
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
- **Usage** : Configuration file, code (py, js), web(light)
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
		- **Regression testing** : Yes
		- **Annotate/Human feedback**: Yes (vote, set score, comment)
			- **Use Human Feedback** : No
		- **Online/ Real time / Dynamic Evaluation**: No
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
	- **Dataset**:  
		-  **Construct Datasets** : 
			- In web platform : No
			- Programmatically ; Yes 
		- **Generate datasets** : No. 
		- **Export Formats**:  Yaml
		- **Visualization Tools**: web based
	- **Prompt engineering** :  
		- Test multiple prompts : Yes
		- Generate prompts : ?
		- Prompt playground : No
		- Visualization Tools: yaml file, web(light)
	- **Difficulty to Use**: Easy
	- **Difficulty to learn** : Medium
        
		

## LangSmith (by LangChain)
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
- **Usage** :  web platform , code (python, JS)
- **Deployment**: 
	- Cloud 
	- Self-Host (paid)
- **Type/runtime** : NA
- **Updates & Maintenance**: Regular updates as features are improved and expanded.
	- **Support Channel**: Same as langchain
	- **Frequency of Updates**: every two months
	- **Community Support**: Langchain community
	- **Popularity/GitHub Stars**: +250k users, +25k monthly active teams, Langchain has 100K stars.
	- **Maturity**: In beta but is enough mature in terms of features. A langchain company product.
	- **Used by** : Many CAC40 and other entreprises
	- **Team** : 20-60 ?
-
- **Privacy & Security**: 
	- **Data Handling**: - Cloud or self-host(paid). If cloud, we will not train on your data, and you own all rights to your data. See LangSmith [Terms of Service](https://www.langchain.com/terms-of-service) for more information.
	- **Compliance / Data Location**: cloud : Traces are stored in GCP us-central-1. Organizations' traces are logically separated from each other in a Clickhouse database and encrypted in transit and at rest.
	- **Telemetry** :  NA
	   
- **Features**:
	- **Evaluation** :
		- **Generator  & Evaluator models** : used to generate, evaluate an output
			- **Model Compatibility**:  Yes. 
			- **Custom/override models**: Yes
		- **Metrics**: Yes. https://www.promptfoo.dev/docs/configuration/expected-outputs/
			- **pre-implemented metrics** : yes. But very few 
				- deterministic metrics : contains, equals, exact-match Yes
				- model-graded metrics : using LLM to evaluate Yes
					- override prompts : yes
					- override Evaluator/grader : yes. 
			- **Qualitative & Quantitative Metrics**: both (score or llm-based)
			- **Custom Metrics**: Yes. 
		- **Regression testing** : Yes
		- **Annotate/Human feedback**: Yes (set score, comment) (inline, or queues)
			- **Use Human Feedback** : Yes. https://docs.smith.langchain.com/evaluation/concepts#human
		- **Online/ Real time / Dynamic Evaluation**: Yes https://docs.smith.langchain.com/evaluation/how_to_guides#online-evaluation
		- **Easy Unit Test (like pytest)**: Yes.
		- **Pre-implemented Dataset Benchmarks**: 
		- **Export Formats**:  
		- **Visualization Tools**: Web-based interface
	- **Redteam**: No. Used like an evaluation feature
		- **Doc** : NA
		- **Models** :  
			- **model compatibility** Yes
			- **Custom/override models** : Yes
		- **Metrics** : 
			- **Pre-implemented metrics** : NA
			- **Custom Metrics** : Yes
		-  **Annotate/Human feedback**: Yes
		- **Use Human Feedback** : Yes
		- **Export Formats**:  ?
		- **Visualization Tools**: web
	- **Monitoring**:  Yes. https://docs.smith.langchain.com/old/monitoring
	- **CI/CD**: Yes. https://docs.smith.langchain.com/evaluation/tutorials/evaluation#set-up-automated-testing-to-run-in-cicd
	- **Dataset**:  
		- https://docs.smith.langchain.com/old/evaluation/faq/manage-datasets
		- **Construct Datasets** : 
			- In web platform : Yes
			- Programmatically ; Yes
		- **Generate datasets** : Yes
			- https://docs.smith.langchain.com/old/evaluation/faq/synthetic-data
		- **Visualization Tools**: web, export to files ..etc
	- **Prompt engineering** : 
		- Test multiple prompts : Yes
		- Generate prompts : Yes
		- Prompt playground : Yes
		- Visualization Tools: web
	- **Difficulty to Use**: very Easy
	- **Difficulty to learn** : Easy


## Langfuse
Langfuse is an **open-source LLM engineering platform** ([GitHub](https://github.com/langfuse/langfuse)) that helps teams collaboratively debug, analyze, and iterate on their LLM applications. All platform features are natively integrated to accelerate the development workflow.

- **Site** : https://www.langchain.com/langsmith
- **Review date** : 29/11/2024
- **version** : 2.93
- **Description**: An all in one platform : 
	- Most used open-source LLMOps platform ([blog post](https://langfuse.com/blog/2024-11-most-used-oss-llmops))
	- Model and framework agnostic
	- Built for production
	- Incrementally adoptable, start with one feature and expand to the full platform over time
	- API-first, all features are available via API for custom integrations
	- Optionally, Langfuse can be easily self-hosted
	- User tracking: Add your own identifiers to inspect traces from specific users
	- Cost tracking: Monitor model usage and costs across your application
	- Quality insights: Collect user feedback and identify low-quality outputs
	- Multi-modal: Support for tracing text, images and other modalities
- **FAQ** : 
- **Docs**: [docs](https://docs.smith.langchain.com/)
- **GitHub**: https://github.com/promptfoo/promptfoo
- **Price**  
	- Free for all features 
	- price site :https://www.langchain.com/pricing-langsmith
	- **Self-host**  
		- **Free**: Self-host all core Langfuse features without any limitations
			- MIT License
			- All core platform features and APIs (observability, evaluation, prompt management, datasets, etc.)
			- Unlimited usage
			- Deployment docs & Helm chart
			- Community support
		- **Pro**: $100/user billed monthly
			- All Open Source features
			- LLM Playground
			- Human annotation queues
			- LLM as a judge evaluators (soon)
			- Chat & Email support
		- **Enterprise**: Custom pricing 
			- All Open Source / Pro features
			- SSO and fine-grained RBAC
			- SOC2, ISO27001, and InfoSec reviews
			- Dedicated support engineer and SLAs
			- Billing via AWS Marketplace
	- **Cloud**
		- **Hobby**: Free
		    - All platform features (with limits)
		    - 50k observations/month included
		    - 30 days data access
		    - 2 users included
		    - Community support (Discord & GitHub)
		- **Pro**: $59/user billed monthly
		    - 100k observations/month included, additional $10/100k observations
		    - Unlimited data access
		    - Unlimited users
		    - Support via Email/Chat
		- **Team**: $499/user billed monthly
		    - 100k observations/month included, additional $10/100k observations
		    - SSO enforcement, fine-grained RBAC
		    - SOC2, ISO27001, InfoSec reviews
		    - Dedicated support channel
		    - Add-ons: Enterprise support & SLAs, Billing via AWS Marketplace
    
- **Usage** :  web platform , code (python, JS)
- **Deployment**: 
	- Cloud 
	- Self-Host 
- **Type/runtime** : if self-host : docker
- **Updates & Maintenance**: 
	- **Support Channel**: Discord Github
	- **Frequency of Updates**: every 3 days
	- **Community Support**: Yes
	- **Popularity/GitHub Stars**:  6k stars, 3m installs /month, 7K stars
1.8m docker pulls,  https://langfuse.com/blog/2024-11-most-used-oss-llmops#detailed-metrics
	- **Maturity**: new, evolving , looks stable
	- **Used by** : 
	- **Team** : 5, raised 4m 
- **Privacy & Security**: 
	- https://langfuse.com/docs/data-security-privacy
	- **Data Handling**: -
	- **Compliance / Data Location**: cloud : Traces are stored in GCP us-central-1. Organizations' traces are logically separated from each other in a Clickhouse database and encrypted in transit and at rest.
	- **Telemetry** :  NA
	   
- **Features**:
	- **Evaluation** :
		- **Generator  & Evaluator models** : used to generate, evaluate an output
			- **Model Compatibility**:  Yes. 
			- **Custom/override models**: Yes
		- **Metrics**: Yes. https://www.promptfoo.dev/docs/configuration/expected-outputs/
			- **pre-implemented metrics** : 
				- deterministic metrics : 
				- model-graded metrics : using LLM to evaluate Yes
					- override prompts : 
					- override Evaluator/grader : 
			- **Qualitative & Quantitative Metrics**: both (score or llm-based)
			- **Custom Metrics**: 
		- **Regression testing** : 
		- **Annotate/Human feedback**: 
			- **Use Human Feedback** : 
		- **Online/ Real time / Dynamic Evaluation**: 
		- **Easy Unit Test (like pytest)**: 
		- **Pre-implemented Dataset Benchmarks**: ·
		- **Export Formats**:  json, csv
		- **Visualization Tools**: Web
	- **Redteam**: Used like an evaluation feature
		- **Doc** : https://langfuse.com/docs/security/overview
		- **Models** :  
			- **model compatibility** Yes
			- **Custom/override models** : Yes
		- **Metrics** : 
			- **Pre-implemented metrics** : 
			- **Custom Metrics** : Yes
		-  **Annotate/Human feedback**: Yes
		- **Use Human Feedback** : Yes
		- **Export Formats**:  json, csv
		- **Visualization Tools**: web
	- **Monitoring**:  Yes. 
	- **CI/CD**: Yes. 
	- **Dataset**:  
		- 
		- **Construct Datasets** : 
			- In web platform : Yes
			- Programmatically : Yes
		- **Generate datasets** : Yes
		- **Visualization Tools**: web, export to files ..etc
	- **Prompt engineering** : 
		- Test multiple prompts : 
		- Generate prompts : 
		- Prompt playground : yes (paid)
		- Visualization Tools: web
	- **Difficulty to Use**: very Easy
	- **Difficulty to learn** : Easy

	##### What are the main differences between Langfuse and Langsmith
	
	- Langfuse is open source while LangSmith is a closed source project.
	- LangSmith is developed by the LangChain team and integrates very well with the LangChain framework. Langfuse also maintains [Langchain integrations](https://langfuse.com/docs/integrations/langchain/tracing).
	- Langfuse maintains a [large number of integrations](https://langfuse.com/docs/integrations/overview) into many frameworks and libraries. Langsmith focuses on its Langchain integration.
	- Langfuse can be [freely self hosted](https://langfuse.com/docs/deployment/self-host) at no cost while LangSmith needs to be purchased to be self hosted.
	- Comparaison with langsmith : https://astralinsights.ai/wp-content/uploads/2024/06/AI-Comparison-White-Paper-June-2024.pdf


## Giskard (by Giskard-AI)
Giskard is a **holistic Testing platform for AI models** to control all 3 types of AI risks: Quality, Security & Compliance.
It contains 3 products : Open-Source AI testing library, LLM Evaluation Hub, AI Compliance Hub

This is the evaluation of the free open-source library
- **Site** : https://www.giskard.ai/
- **Review date** : 02/12/2024
- **version** : 2.16.0
- **Description**: It contains 3 products : 
	- Open-Source AI testing library : Automatically run exhaustive test suites to identify risks on your ML models and LLMs.
	- LLM Evaluation Hub : Collaborative Hub for GenAI Product Owners, Data Scientists & QA teams to control Al Quality & Security risks in one place.
	- AI Compliance Hub : Continuously track AI compliance with tailored risk mitigation recommendations, and collaborate for AI Governance at scale.
- **FAQ** : 
- **Docs**: [docs](https://docs.giskard.ai/)
- **GitHub**: https://github.com/Giskard-AI/giskard
- **Price**  
	- Free (open-source library) or paid (for the hub)
	- price site: https://www.giskard.ai/pricing
	- **open-source**  :
		- Testing AI systems in Python code
		- Deployment : Python library
		- Support channels : Discord
	- **Enterprise**
		- Testing AI systems in Python code
		- LLM Evaluation Hub
		- AI Compliance Hub
		- Secure collaboration
		- Deployment : On-premise, Private Cloud, SaaS
		- User authentification
		- Role-Based Access Control
		- Single-Sign-On (SSO)
		- Support channels : Dedicated email & ticketing platform
		- AI Red-Teaming audit
		- AI Quality & Security training
    
- **Usage** :  code (python)
- **Deployment**: 
	-  python package:  On-premise (Free)
	- Hub : On-premise, Private Cloud, SaaS (paid)
- **Type/runtime** : Python
- **Updates & Maintenance**: 
	- **Support Channel**: Discord, Github
	- **Frequency of Updates**: every 2 weeks
	- **Community Support**: Yes
	- **Popularity/GitHub Stars**:  4k stars
	- **Maturity**: evolving , looks stable
	- **Used by** : Axa, Canal+, Etam (using paid entreprise version)
	- **Team** : 14, raised 7.5 M€ (BPI, EC, HF)
- **Privacy & Security**: 
	- **Data Handling**: Website collects data. ==NM==
	- **Compliance / Data Location**: ==NM==
	- **Telemetry** :  ==NM==
	   
- **Features**:
	- **Evaluation** :
		- **Generator  & Evaluator models** : used to generate, evaluate an output
			- **Model Compatibility**:  Yes. 
			- **Custom/override models**: Yes
		- **Metrics**: Yes. 
			- **pre-implemented metrics** : yes.
				- https://docs.giskard.ai/en/stable/reference/tests/index.html
				- https://docs.giskard.ai/en/stable/knowledge/catalogs/test-catalog/index.html
				- deterministic metrics : yes
				- model-graded metrics : yes
			- **Qualitative & Quantitative Metrics**: both (score or llm-based)
			- **Custom Metrics**: Yes. 
		- **Annotate/Human feedback**: 
			- **Use Human Feedback** : No.
		- **Online/ Real time / Dynamic Evaluation**: ==To confirm==.
		- **Easy Unit Test (like pytest)**: Yes.
		- **Pre-implemented Dataset Benchmarks**: No
		- **Export Formats**:  json, html, mlflow, wandb, markdown, dataframe,
		- **Visualization Tools**: web(free: extremely light)
	- **Redteam**: Yes
		- **Doc** : https://docs.giskard.ai/en/stable/knowledge/llm_vulnerabilities/index.html
		- **Models** :  
			- **model compatibility** Yes
			- **Custom/override models** : Yes
		- **Metrics** : 
			- **Pre-implemented metrics** : Yes https://docs.giskard.ai/en/stable/knowledge/key_vulnerabilities/index.html
				- Traditional detectors (generator and adversarial)
				- LLM as a judge detectors (generator, adversarial and evaluator)
			- **Custom Metrics** : 
		-  **Annotate/Human feedback**: ==To confirm==
		- **Use Human Feedback** : ==To confirm==
		- **Export Formats**:  json, html, mlflow, wandb, markdown, dataframe,
		- **Visualization Tools**: web(free: extremely light)
	- **Monitoring**:  Paid.
	- **CI/CD**: Yes. 
	- **Dataset**:  
		- https://www.giskard.ai/products/llm-evaluation-hub
		- **Construct Datasets** : 
			- In web platform : Yes
			- Programmatically : ==To confirm==
		- **Generate datasets** : Yes
		- **Visualization Tools**: web
	- **Prompt engineering** : 
		- Test multiple prompts : 
		- Generate prompts : 
		- Prompt playground : 
		- Visualization Tools: 
	- **Difficulty to Use**: easy
	- **Difficulty to learn** : medium (due to bugs)

## DeepEval (by ConfidentAI)
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
## Prompt-flow Tracing (by Azure)

## Validate (by Tonic)
## AutoRAG

