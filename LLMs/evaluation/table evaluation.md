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


**Different table formatting structures:**
- MD, Piped, comma-separated, json, key-value, Latex, HTML,
- Not taking into account: Image 

### Query Type Classification  
  
#### 1. Direct Retrieval Queries  
  
Questions where the answer exists directly in a table cell.  
  
**Characteristics:**  
- Single cell lookup  
- No computation required  
- Direct mapping from question to cell  
  
**Examples:**  
```  
Q: "What is Alice's age?"  
Table: | Name  | Age |  
       | Alice | 25  |A: "25" (direct lookup)  
  
Q: "Which country is Bob from?"  
Table: | Name | Country |  
       | Bob  | UK      |A: "UK" (direct lookup)  
```  
  
**Evaluation Metrics:**  
- Exact Match Accuracy  
- Cell Accuracy  
- Retrieval Precision  
  
**Difficulty Factors:**  
- Table size (number of rows/columns)  
- Ambiguous column names  
- Multiple matching entities

### 2. Computation-Required Queries  
  
Questions requiring operations on table data.  
  
> **Research Finding** (Wolff & Hulsebos, 2025): LLMs show significant performance degradation on aggregation and complex calculation queries compared to simple lookup tasks. Evaluation revealed that traditional metrics (BLEU, BERTScore) fail to reliably distinguish correct from incorrect answers for analytical queries.  
  
#### 2.1 Aggregation Queries  
  
**Operations:** COUNT, SUM, AVG, MAX, MIN  
  
**Examples:**  
```  
Q: "How many players are from Australia?"  
Operation: COUNT(rows WHERE Country = 'Australia')  
A: "3"  
  
Q: "What is the total score?"  
Operation: SUM(Score column)  
A: "245"  
  
Q: "What is the average age?"  
Operation: AVG(Age column)  
A: "27.5"  
```  
  
**Evaluation Metrics:**  
- Numerical Accuracy (with tolerance)  
- Type-Aware Accuracy  
- Operation Accuracy  
  
#### 2.2 Comparison Queries  
  
**Operations:** >, <, =, >=, <=, BETWEEN  
  
**Examples:**  
```  
Q: "Which player has the highest score?"  
Operation: MAX(Score) → find corresponding Name  
A: "Alice"  
  
Q: "List players older than 25"  
Operation: SELECT Name WHERE Age > 25  
A: ["Bob", "Charlie"]  
```  
  
**Evaluation Metrics:**  
- Exact Match  
- Partial Credit (for list answers)  
- Ranking Quality (NDCG for ordered lists)  
  
#### 2.3 Arithmetic Queries  
  
**Operations:** +, -, ×, ÷, %  
  
**Examples:**  
```  
Q: "What is the difference between the highest and lowest score?"  
Operation: MAX(Score) - MIN(Score)  
A: "15"  
  
Q: "What percentage of players are from USA?"  
Operation: (COUNT(Country='USA') / COUNT(*)) × 100  
A: "40%"  
```  
  
**Evaluation Metrics:**  
- Numerical Accuracy (±0.01 tolerance)  
- Unit Consistency  
- Format Matching  
  
#### 2.4 Multi-Hop Queries  
  
**Operations:** Multiple sequential reasoning steps  
  
**Examples:**  
```  
Q: "What is the average age of players from Australia?"  
Steps:  
  1. Filter rows WHERE Country = 'Australia'  2. Calculate AVG(Age) on filtered rowsA: "28.3"  
  
Q: "Which country has the most players over 30?"  
Steps:  
  2. Filter rows WHERE Age > 30  2. GROUP BY Country  3. COUNT per group  4. Find MAX countA: "USA"  
```  
  
**Evaluation Metrics:**  
- End-to-end Accuracy  
- Hop Accuracy (per step)  
- Reasoning Chain Correctness  
  
#### 2.5 Temporal Queries  
  
**Operations:** Date/time comparisons, duration calculations  
  
**Examples:**  
```  
Q: "How many events occurred after 2020?"  
Operation: COUNT(rows WHERE Year > 2020)  
A: "12"  
  
Q: "What is the time difference between first and last event?"  
Operation: MAX(Date) - MIN(Date)  
A: "5 years"  
```  
  
**Evaluation Metrics:**  
- Date Format Normalization  
- Temporal Accuracy  
- Unit Consistency



- **WikiTableQuestions**: Wikipedia tables with natural language questions  
- **TableVQA**: Visual table question answering  
- **TableBench**: Comprehensive table understanding benchmark  
- **TableEval**: Multi-dimensional table evaluation  
- **TableQAKit/SQA**: Sequential question answering on tables  
- **Geoquery-TableQA**: Geographic data tables  
- **TQA-Bench**: Multi-table reasoning with varying complexity levels

### Metadata columns:

Metadata about the table schema such as which column contains which value and the datatype of each column increases the accuracy.
{  
  "difficulty_level": "easy | medium | hard",  
  "reasoning_type": ["lookup", "aggregation", "comparison", "multi_hop", "arithmetic"],  
  "num_reasoning_steps": "integer",  
  ~~"question_type": "factoid | list | boolean | numerical | descriptive",~~  
  "answer_type": "entity | number | date | text | boolean ",  
  "answer_length": "integer (tokens)",  
  "table_num_rows": "integer",  
  "table_num_cols": "integer",  
  "table_size_category": "small | medium | large",  
  "table_domain": "sports | geography | finance | general | ...",  
  "columns_involved": ["column_name1", "column_name2"],  
  "answer_in_table": "boolean (direct cell vs computed)",  
  "requires_numerical_reasoning": "boolean",  
  "has_ground_truth": "boolean",  
  "ambiguity_flag": "boolean",  
  "evaluation_metrics": ["exact_match", "f1", "bertscore"],  
  "context_size_tokens": "integer",  
  "num_tables": "integer",  
  "has_missing_values": "boolean",  
  "has_duplicate_entities": "boolean",  
  "requires_foreign_key_resolution": "boolean"  
}

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


### 7. Error Analysis  
  
**Categorize errors:**  
1. **Retrieval errors**: Wrong cell identified  
2. **Computation errors**: Wrong operation applied  
3. **Type errors**: Wrong answer type  
4. **Hallucinations**: Fabricated information  
5. **Format errors**: Correct value, wrong format  
  
**For each error category:**  
- Calculate frequency  
- Identify patterns  
- Prioritize fixes
## Tools / libraries 
- item 1

## Papers and research
- item 1

## Other resources 
- item 1


