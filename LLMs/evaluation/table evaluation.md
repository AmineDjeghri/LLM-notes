## News and updates
- item 1
## Easy guides

- https://medium.com/@anshoo.jani/benchmarking-large-language-models-on-tabular-data-a-comprehensive-evaluation-ed3c3c6523a0
	- **Markdown Format Data:** Highest accuracy due to lower token consumption.
	- **Key-Value List Format Data:** Improved accuracy due to structured metadata.
	- **JSON Format Data:** Increased context length, making it infeasible for some models.
	- **Comma-Separated Format Data:** Moderate efficiency but prone to misinterpretation.
	- **Pipe-Separated Format Data:** Similar to Markdown, better than CSV.
	- The accuracy of the key-value list format improved more than any other format when providing metadata.
Type of queries:
- Retrieved directly from the table
- Requires computation

Different table formatting structures:
- MD, Piped, comma-separated, json, key-value, Latex, HTML,
- Not taking into account: Image 

Metadata about the table schema such as which column contains which value and the datatype of each column increases the accuracy.

- **WikiTableQuestions**: Wikipedia tables with natural language questions  
- **TableVQA**: Visual table question answering  
- **TableBench**: Comprehensive table understanding benchmark  
- **TableEval**: Multi-dimensional table evaluation  
- **TableQAKit/SQA**: Sequential question answering on tables  
- **Geoquery-TableQA**: Geographic data tables


### **Primary Metrics for Table QA**

1. **Answer Correctness** (End-to-end)
    - Evaluates exact match or semantic equivalence between predicted and ground truth answers
    - Essential for structured data queries
    
2. **BLEU Score** (Generation)
    - Useful when answers are longer text spans
    - Measures n-gram overlap with reference answers
    - Good for TableVQA where answers may be descriptive
    
3. **ROUGE Score** (Generation)
    - Particularly ROUGE-L for longer answers
    - Captures recall of key information from tables
    - Useful for TableBench and TableEval
    
4. **BERTScore** (Generation)
    - Semantic similarity using contextual embeddings
    - Better than BLEU/ROUGE for paraphrased correct answers
    - Handles synonyms and semantic equivalence well
    
5. **F1 Score** (Retrieval/IR - adapted for QA)
    - Token-level F1 between prediction and ground truth
    - Standard metric for SQuAD-style QA (relevant for TableQAKit/SQA)
    - Balances precision and recall
- 

### **Secondary Metrics**

6. **Faithfulness / Hallucination Rate** (Generation)
    - Critical for ensuring answers come from the table
    - Detects when model fabricates information not in the table
    - Important for trustworthiness
    
7. **Relevance** (End-to-end)
    - Assesses if the answer addresses the question
    - Can use LLM-as-judge for evaluation
    
8. **Fluency** (End-to-end)
    - For natural language answers (TableVQA)
    - Less critical for short factual answers
    
9. **Human Evaluation** (End-to-end)
    - Gold standard for complex reasoning tasks
    - Useful for TableBench which tests complex operations
    

### **Task-Specific Considerations**

- **WikiTableQuestions**: Exact match + F1 (standard benchmarks)
- **TableQAKit/SQA**: F1 Score, Exact Match (follows SQuAD format)
- **TableVQA**: BERTScore, BLEU, Answer Correctness
- **Geoquery-TableQA**: Exact Match, Semantic Parsing Accuracy
- **TableBench/TableEval**: Answer Correctness, BERTScore, Faithfulness


## Tools / libraries 
- item 1

## Papers and research
- item 1

## Other resources 
- item 1


