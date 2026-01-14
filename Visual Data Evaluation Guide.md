| Data Type    | Input Modality |
| ------------ | -------------- |
| **Charts**   | Image          |
| **Diagrams** | Image          |
| **Tables**   | Text/Image     |

| Aspect                    | Charts                       | Diagrams                                 | Tables                                    |     |
| ------------------------- | ---------------------------- | ---------------------------------------- | ----------------------------------------- | --- |
| **Format**                | Image (PNG, JPG, SVG)        | Image (PNG, JPG, SVG)                    | Text (Markdown, CSV, JSON, HTML) or Image |     |

### Evaluation Metrics Priority  
  
| Metric                       | Charts                                | Diagrams                               | Tables                             |     |
| ---------------------------- | ------------------------------------- | -------------------------------------- | ---------------------------------- | --- |
| **Exact Match**              | Low priority (formatting varies)      | Medium priority                        | High priority (structured answers) |     |
| **Numerical Accuracy (±5%)** | **Primary**                           | Low priority                           | **Primary**                        |     |
| **F1 Score**                 | Medium (multi-element answers)        | **Primary** (component lists)          | Medium (list answers)              |     |
| **LLM-as-Judge**             | **Primary** (semantic equivalence)    | **Primary** (structural understanding) | **Primary** (analytical queries)   |     |
| **BERTScore**                | ⚠️ Unreliable (Wolff & Hulsebos 2025) | Medium (descriptive answers)           | ⚠️ Unreliable for numerical        |     |
| **Ranking Accuracy**         | Medium (ordered comparisons)          | Low priority                           | Medium (ordered results)           |     |
  
## Evaluation Metrics by Data Type  
  
### 📊 Charts: Visual-Numerical Reasoning  
  
#### Primary Metrics  
  
**1. Numerical Accuracy with Tolerance**  

→ Value extraction, aggregation tasks    
  
**2. LLM-as-Judge Correctness**  
```  
Prompt: Evaluate if "{prediction}" matches "{ground_truth}" considering visual estimation (±5% tolerance) and format variations.  
Response: CORRECT | PARTIAL | INCORRECT  
```  
  
**When to use:** All chart tasks 
  
### 🔀 Diagrams: Structural Understanding  
  
#### Primary Metrics  
  
**1. F1 Score (Component Extraction)**  

→ Component identification, relationship extraction    
  
**2. LLM-as-Judge Structural Correctness**  

**3. Exact Match (for counting tasks)**  
- "How many decision nodes?" → Exact integer match  
  
### 📋 Tables: Logical Reasoning  
  
#### Primary Metrics  
  
**1. Exact Match**  
→ Direct lookup, categorical answers    
  
**2. Numerical Accuracy (for computed answers)**  
- Same as charts: ±5% tolerance  
- Critical for aggregation queries  
  
**3. LLM-as-Judge (for analytical queries)**  
```  
Prompt: Evaluate table reasoning:  
- Correct cell identification  
- Proper operation (SUM, AVG, COUNT, etc.)  
- Accurate calculation  
- Handling of edge cases (NULL, duplicates)  
  
Response: CORRECT | PARTIAL | INCORRECT  
```  
  
- **BLEU fails** to distinguish correct from incorrect analytical answers  
- **LLM-as-judge is validated**: 93.75% accuracy for correct answers  
  
## Metadata Requirements  
  
### 🎯 Universal Metadata (All Data Types)  
  
```json  
{  
  "question_id": "unique_identifier",  
  "dataset_source": "ChartQA | AI2D | WikiTableQuestions",  
  "dataset_version": "v1.0",  
  "date": "2025-01-14T16:40:00Z",  
  "question": "What is the value for Category A?",  
  "ground_truth": "45",  
  "answer_type": "numerical | categorical | boolean | list | descriptive",  
  "task_metadata": {  
    "task_type": "value_extraction | comparison | composition (aggregation) | trend_analysis | structural ",  
    "difficulty": "easy | medium | hard",  
    "num_reasoning_steps": 1,  
 
}  
```  
  
---  
  
### 📊 Chart-Specific Metadata  
  
```json  
{  
  "image_metadata": {  
    "image_path": "/data/charts/chart_001.png",  
    "image_resolution": [800, 600],  
    "image_quality": "high | medium | low",  
    "dpi": 150,  
    "file_size_bytes": 245678  
  },  
  "chart_metadata": {  
    "chart_type": "bar_chart | line_chart | pie_chart | scatter_plot | heatmap",  
    "chart_subtype": "vertical_grouped | stacked | multi_line",  
    "has_legend": true,  
    "has_title": true,  
    "domain": "business | scientific | educational"  
  } 
}  
```  
  
  
---  
  
### 🔀 Diagram-Specific Metadata  
  
```json  
{  
  "image_metadata": {  
    "image_path": "/data/diagrams/flowchart_001.png",  
    "image_resolution": [1200, 900],  
    "image_quality": "high",
	"dpi": 150,  
    "file_size_bytes": 245678  
  },  
  "diagram_metadata": {  
    "diagram_type": "flowchart | network_diagram | organizational_chart | technical_diagram",  
    "domain": "business_process | software_architecture | organizational"  
  },  
}  
```  
  
---  
  
### 📋 Table-Specific Metadata  
  
```json  
{  
  "table_metadata": {  
    "table_format": "markdown | csv | json | html | latex | image",  
    "table_num_rows": 25,  
    "table_num_cols": 8,  
    "table_size_category": "small | medium | large",  
    "context_size_tokens": 2048,  
    "has_header": true,  
    "has_merged_cells": false,  
    "domain": "sports | geography | finance | general"  
  },  
  "data_characteristics": {  
    "has_missing_values": false,  
    "has_duplicate_entities": false,  
  },  
}  
```  


---  
  
## Task Categories  
  
### 📊 Chart Tasks  
  
| Task | Description | Example | Difficulty |  
|------|-------------|---------|------------|  
| **Value Extraction** | Read explicit values | "What is Q2 sales?" → "$45,000" | Easy-Medium |  
| **Comparison** | Compare visual elements | "Which product has highest sales?" → "Product A" | Medium |  
| **Composition** | Calculate aggregates | "What is total across all quarters?" → "250" | Hard |  
| **Trend Analysis** | Identify patterns | "Describe trend 2020-2023" → "Steady increase with dip in 2022" | Medium-Hard |  
| **Structural** | Understand layout | "What does legend indicate?" → "Blue=Revenue, Red=Costs" | Easy |  
  
---  
  
### 🔀 Diagram Tasks  
  
| Task | Description | Example | Difficulty |  
|------|-------------|---------|------------|  
| **Component Identification** | List elements | "How many decision nodes?" → "3" | Easy |  
| **Relationship Extraction** | Map connections | "What follows Node A?" → "Node B and Node C" | Medium |  
| **Path Finding** | Trace sequences | "Path from Start to End?" → "Start→A→B→End" | Medium-Hard |  
| **Hierarchical Understanding** | Understand structure | "Who reports to CEO?" → "VP Sales, VP Engineering" | Medium |  
| **Process Flow** | Sequential reasoning | "What happens if condition is false?" → "Go to error handler" | Hard |  
  
---  
  
### 📋 Table Tasks  
  
| Task              | Description               | Example                                       | Difficulty  |     |
| ----------------- | ------------------------- | --------------------------------------------- | ----------- | --- |
| **Direct Lookup** | Single cell access        | "What is Alice's age?" → "25"                 | Easy        |     |
| **Aggregation**   | COUNT, SUM, AVG, MAX, MIN | "How many players from Australia?" → "3"      | Medium      |     |
| **Comparison**    | Find extrema              | "Which player has highest score?" → "Alice"   | Easy-Medium |     |
| **Arithmetic**    | Calculations              | "Difference between max and min?" → "15"      | Medium      |     |
| **Multi-hop**     | Sequential operations     | "Average age of Australian players?" → "28.3" | Hard        |     |
| **Temporal**      | Date/time operations      | "Events after 2020?" → "12"                   | Medium      |     |

  
## Data Examples  
  
### 📊 Chart Examples  
  
**Value Extraction:**  
```  
Q: How many pounds did the UK spend on civil defense in 2019/20?  
A: 46  
Task: value_extraction | Difficulty: easy | Metric: numerical_accuracy  
```  
  
**Comparison:**  
```  
Q: Who is the top goal scorer among the listed players, and how many goals did they score?  
A: Thierry Henry with 228 goals  
Task: comparison | Difficulty: medium | Metric: llm_as_judge  
```  
  
**Composition:**  
```  
Q: What's the sum of the highest value of green bars and the median value of green bars?  
A: 63  
Task: composition | Difficulty: hard | Metric: numerical_accuracy  
```  
  
**Trend Analysis:**  
```  
Q: By how much do favorable views of the United States differ from unfavorable views in 2015?  
A: 42  
Task: trend_analysis | Difficulty: medium | Metric: numerical_accuracy  
```  
  
---  
  
### 🔀 Diagram Examples 
  
**Component Identification:**  
```  
Q: According to the diagram, which organisms are found at the 'ZOOPLANKTON' level?  
A: Shrimp, Copepods, and Pteropods  
Task: component_identification | Difficulty: easy | Metric: f1_score  
```  
  
**Hierarchical Understanding:**  
```  
Q: Based on the given organization chart, who is part of the Design Staff?  
A: James King and Thomas Harrison (and possibly Anne Davies)  
Task: hierarchical_understanding | Difficulty: medium | Metric: f1_score  
```  
  
**Process Flow:**  
```  
Q: According to the CEC DRP communications process, what is the fourth step?  
A: Regular updates  
Task: process_flow | Difficulty: medium | Metric: exact_match  
```  
  
**Relationship Extraction:**  
```  
Q: According to the diagram, which department works with both the auditors and the President/CEO?  
A: Internal Audit Department  
Task: relationship_extraction | Difficulty: hard | Metric: llm_as_judge  
```  
  
---  
  
### 📋 Table Examples 
  
**Direct Lookup:**  
```  
Q: What is the highest score achieved by Lionel Palairet in his cricket career?  
A: 100  
Task: direct_lookup | Difficulty: easy | Metric: exact_match  
```  
  
**Aggregation:**  
```  
Q: What is the total amount of winnings for all drivers who drove a Chevrolet car?  
A: 2880210  
Task: aggregation | Difficulty: medium | Metric: numerical_accuracy  
```  
  
**Multi-hop Reasoning:**  
```  
Q: What is the aggregate count of participants spanning every installment of the television program?  
A: 137  
Task: multi_hop | Difficulty: hard | Metric: numerical_accuracy  
```  
  
**Comparison:**  
```  
Q: Which nation ranked with a total of 8 medals, including 3 gold medals?  
A: France  
Task: comparison | Difficulty: medium | Metric: exact_match  
```  
  
**Arithmetic:**  
```  
Q: What is the mean figure for the 2001 nationwide ballot in the entirety of Italy's areas?  
A: 6.16  
Task: arithmetic | Difficulty: hard | Metric: numerical_accuracy  
```