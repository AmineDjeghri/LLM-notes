


# LLM Evaluation


https://arxiv.org/pdf/2306.05685

## RAG Evaluation

RAG systems are composed of a retrieval and an LLM based generation module, and provide LLMs with knowledge from a reference textual database, which enables them to act as a natural language layer between a user and textual databases, reducing the risk of hallucinations.

- Awesome list of rag eval tools: https://github.com/YHPeter/Awesome-RAG-Evaluation

- Recommanded tools
	- RAGAS : 
		- GitHub : https://github.com/explodinggradients/ragas
		- Paper : https://arxiv.org/abs/2309.15217

| Metric                                       | Stage              | Description                                                                            |     |     |
| -------------------------------------------- | ------------------ | -------------------------------------------------------------------------------------- | --- | --- |
| Precision@k                                  | Retrieval (IR)     | Calculates the proportion of relevant documents in the top k results                   |     |     |
| Recall@k                                     | Retrieval (IR)     | Measures the proportion of relevant documents retrieved in the top k results           |     |     |
| F1 Score                                     | Retrieval (IR)     | Harmonic mean of precision and recall                                                  |     |     |
| Mean Reciprocal Rank (MRR)                   | Retrieval (IR)     | Measures the rank of the first relevant document in the search results                 |     |     |
| Mean Average Precision (MAP)                 | Retrieval (IR)     | Evaluates the precision of retrieval at multiple recall levels                         |     |     |
| Normalized Discounted Cumulative Gain (NDCG) | Retrieval (IR)     | Measures the quality of ranking, considering the position of relevant documents        |     |     |
| Cosine Similarity                            | Embeddings         | Measures the similarity between query and document embeddings                          |     |     |
| Perplexity                                   | Generation         | Evaluates how well the model predicts a sample, lower is better                        |     |     |
| BLEU Score                                   | Generation         | Measures the similarity between generated text and reference text                      |     |     |
| ROUGE Score                                  | Generation         | Evaluates the quality of generated summaries                                           |     |     |
| METEOR Score                                 | Generation         | Assesses the quality of machine translation or text generation                         |     |     |
| BERTScore                                    | Generation         | Computes the similarity of two sentences using contextual embeddings                   |     |     |
| MoverScore                                   | Generation         |                                                                                        |     |     |
| Faithfulness / Hallucination Rate            | Generation         | Measures how accurately the generated text reflects the retrieved information          |     |     |
| Relevance                                    | End-to-end         | Assesses how relevant the generated response is to the input query                     |     |     |
| Coherence                                    | End-to-end         | Evaluates the logical flow and consistency of the generated text                       |     |     |
| Fluency                                      | End-to-end         | Measures the grammatical correctness and naturalness of the generated text             |     |     |
| Answer Correctness                           | End-to-end         | Evaluates the factual accuracy of the generated answers                                |     |     |
| Human Evaluation                             | End-to-end         | Subjective assessment of overall quality, relevance, and usefulness                    |     |     |
| Latency                                      | System Performance | Measures the time taken to generate a response                                         |     |     |
| Throughput                                   | System Performance | Evaluates the number of queries the system can handle per unit time                    |     |     |
| RAGAS Faithfulness                           | Generation         | Measures how factually consistent the generated answer is with the retrieved context   |     |     |
| RAGAS Answer Relevancy                       | End-to-end         | Evaluates how relevant the generated answer is to the given question                   |     |     |
| RAGAS Context Relevancy                      | Retrieval (IR)     | Assesses how relevant the retrieved context is to the given question                   |     |     |
| RAGAS Context Precision                      | Retrieval (IR)     | Measures the proportion of relevant information in the retrieved context               |     |     |
| RAGAS Context Recall                         | Retrieval (IR)     | Evaluates how much of the necessary information from the context is used in the answer |     |     |
| RAGAS Harmfulness                            | End-to-end         | Detects potential harmful content in the generated answers                             |     |     |

**Information Extraction Metrics**
------------------------------------- |
| Mean Average Precision (MAP) | Measures the average precision at different recall levels. Higher values indicate better performance.                       |
| Mean Reciprocal Rank (MRR)   | Measures the average rank of the first correctly extracted piece of information. Higher values indicate better performance. |

| Metric                            | Stage                  | Description                                                                                                  |
|-----------------------------------|------------------------|--------------------------------------------------------------------------------------------------------------|
| Precision                         | Information Extraction | Measures the proportion of correctly extracted entities or information among all extracted items             |
| Recall                            | Information Extraction | Evaluates the proportion of correctly extracted entities or information among all relevant items in the text |
| F1 Score                          | Information Extraction | Harmonic mean of precision and recall, providing a single metric that balances both                          |
| Exact Match (EM)                  | Information Extraction | Measures the proportion of extractions that exactly match the ground truth                                   |
| Entity-Level Precision            | Information Extraction | Evaluates the accuracy of entity extraction, focusing on whether the correct entities are identified         |
| Entity-Level Recall               | Information Extraction | Measures the ability to identify all relevant entities in the text                                           |
| Entity-Level F1 Score             | Information Extraction | Combines entity-level precision and recall into a single metric                                              |
| Slot-Filling Accuracy             | Information Extraction | Assesses how accurately the system fills in predefined slots with the correct information                    |

NER Metrics :

| Metric                     | Description                                                                                                |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| **Precision**              | The proportion of correctly identified entities out of all identified entities.                            |
| **Recall**                 | The proportion of actual entities that were correctly identified.                                          |
| **F1 Score**               | The harmonic mean of precision and recall, balancing the two metrics.                                      |
| **Entity-Level Precision** | Precision calculated separately for each entity type (e.g., PERSON, ORGANIZATION).                         |
| **Entity-Level Recall**    | Recall calculated separately for each entity type.                                                         |
| **Entity-Level F1 Score**  | F1 Score calculated separately for each entity type.                                                       |
| **Token-Level Precision**  | Precision measured at the token level, assessing the accuracy of entity boundaries.                        |
| **Token-Level Recall**     | Recall measured at the token level, assessing the ability to capture all tokens that are part of entities. |
| **Token-Level F1 Score**   | F1 Score measured at the token level.                                                                      |
| **Exact Match**            | The proportion of entities with exact matches to ground truth annotations.                                 |
| **Partial Match**          | Measures how well the model identifies parts of entities that overlap with ground truth.                   |
| **Coverage**               | The proportion of ground truth entities that are captured by the model.                                    |
| **Precision at K (P@K)**   | Precision of the top K predictions.                                                                        |
| **Entity-Level Accuracy**  | The percentage of entities that are correctly identified with correct boundaries and labels.               |
| **Average Precision (AP)** | Average precision across different recall levels, summarizing precision performance.                       |
| **Average Recall (AR)**    | Average recall across different precision levels, summarizing recall performance.                          |
| **Span-Level Precision**   | Precision based on the spans of text identified as entities.                                               |
| **Span-Level Recall**      | Recall based on the spans of text identified as entities.                                                  |
| **Span-Level F1 Score**    | F1 Score based on the spans of text identified as entities.                                                |

This table provides a comprehensive overview of various metrics used to evaluate NER systems, addressing different aspects of performance from entity identification to boundary accuracy and overall classification quality.

These metrics help in understanding how well an information extraction system performs in identifying and classifying relevant entities, relationships, and information from unstructured text.
### RAG Evaluation Metrics Examples 
See source number 3
#### Retrieval (IR) Metrics
- Mean Reciprocal Rank (MRR):
[source](https://www.pinecone.io/learn/offline-evaluation/#Mean-Reciprocal-Rank-(MRR))

- Mean Average Precision (MAP):
It uses Precision@K
[source](https://www.pinecone.io/learn/offline-evaluation/#Mean-Average-Precision-(MAP))

- Normalized Discounted Cumulative Gain (NDCG):
[source](https://www.pinecone.io/learn/offline-evaluation/#Normalized-Discounted-Cumulative-Gain-(NDCG@K))



## RedTeaming metrics : 
- DeepEval redTeaming vulnerabilities :  https://docs.confident-ai.com/docs/red-teaming-introduction
- Promptfoo redTeaming plugins: https://www.promptfoo.dev/docs/red-team/plugins/

#### Generation Metrics
[source](https://aman.ai/primers/ai/evaluation-metrics/#evaluation-metrics-for-generative-text-models)

## Papers and sources
- You need to understand the difference between recall and recall@K. if  K=N in Recall@K, it effectively becomes Recall.
- [RAGAS paper](https://arxiv.org/pdf/2309.15217) 
- [Survey RAG eval tools](https://arxiv.org/pdf/2405.07437)
- https://www.pinecone.io/learn/offline-evaluation/
- https://aman.ai/primers/ai/evaluation-metrics
- [Boolean vs Keyword/Lexical search vs Semantic](https://aarontay.medium.com/boolean-vs-keyword-lexical-search-vs-semantic-keeping-things-straight-95eb503b48f5)
- https://medium.com/@autorag/tips-to-understand-rag-generation-metrics-70dfcd988709

