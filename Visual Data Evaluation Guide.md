| Data Type    | Input Modality |
| ------------ | -------------- |
| **Charts**   | Image          |
| **Diagrams** | Image          |
| **Tables**   | Text/Image     |

| Aspect                    | Charts                       | Diagrams                                 | Tables                                    |     |
| ------------------------- | ---------------------------- | ---------------------------------------- | ----------------------------------------- | --- |
| **Format**                | Image (PNG, JPG, SVG)        | Image (PNG, JPG, SVG)                    | Text (Markdown, CSV, JSON, HTML) or Image |     |
### Task Complexity  
  
| Task Type | Charts | Diagrams | Tables |  
|-----------|--------|----------|--------|  
| **Direct Lookup** | Medium (visual reading) | Easy (text identification) | Easy (cell access) |  
| **Comparison** | Medium (visual comparison) | Medium (relationship tracing) | Easy (value comparison) |  
| **Aggregation** | Hard (multiple value extraction) | Hard (counting components) | Medium (SQL-like operations) |  
| **Multi-hop Reasoning** | Very Hard (cross-element reasoning) | Hard (path finding) | Medium (join operations) |  
| **Trend Analysis** | Medium (pattern recognition) | Medium (flow understanding) | Hard (temporal patterns) |  
  
### Evaluation Metrics Priority  
  
| Metric | Charts | Diagrams | Tables |  
|--------|--------|----------|--------|  
| **Exact Match** | Low priority (formatting varies) | Medium priority | High priority (structured answers) |  
| **Numerical Accuracy (±5%)** | **Primary** | Low priority | **Primary** |  
| **F1 Score** | Medium (multi-element answers) | **Primary** (component lists) | Medium (list answers) |  
| **LLM-as-Judge** | **Primary** (semantic equivalence) | **Primary** (structural understanding) | **Primary** (analytical queries) |  
| **BERTScore** | ⚠️ Unreliable (Wolff & Hulsebos 2025) | Medium (descriptive answers) | ⚠️ Unreliable for numerical |  
| **Ranking Accuracy** | Medium (ordered comparisons) | Low priority | Medium (ordered results) |  
  
### Common Error Types  
  
| Error Category | Charts | Diagrams | Tables |  
|----------------|--------|----------|--------|  
| **OCR Errors** | 15-25% of failures | 10-20% of failures | 5-10% (image tables only) |  
| **Value Extraction** | 30-40% of failures | 15-20% of failures | 10-15% of failures |  
| **Reasoning Errors** | 20-30% of failures | 40-50% of failures | 40-50% of failures |  
| **Calculation Errors** | 10-15% of failures | 5-10% of failures | 20-30% of failures |  
| **Hallucinations** | 5-10% of failures | 10-15% of failures | 5-10% of failures |  
  
---  
  
## Evaluation Metrics by Data Type  
  
### 📊 Charts: Visual-Numerical Reasoning  
  
#### Primary Metrics  
  
**1. Numerical Accuracy with Tolerance**  
```python  
def numerical_accuracy(pred, gt, tolerance=0.05):  
    """    Accounts for visual estimation errors    Tolerance: 5% for standard charts, 10% for low-res    """    pred_num = parse_number(pred)  # "45k" → 45000    gt_num = parse_number(gt)    rel_error = abs(pred_num - gt_num) / abs(gt_num)    return rel_error <= tolerance  
```  
  
**When to use:** Value extraction, aggregation tasks    
**Typical accuracy:** 75-85% for bar/line charts, 65-75% for complex charts  
  
**2. LLM-as-Judge Correctness**  
```  
Prompt: Evaluate if "{prediction}" matches "{ground_truth}" considering visual estimation (±5% tolerance) and format variations.  
Response: CORRECT | PARTIAL | INCORRECT  
```  
  
**When to use:** All chart tasks (validated by Wolff & Hulsebos 2025)  **Typical accuracy:** 80-90% correlation with human judgment  
  
**3. Relaxed Accuracy**  
- Normalizes currency symbols, units, formatting  
- "45000" = "$45k" = "45 thousand"  
  
#### Stratified Metrics  
  
| Chart Type | Avg Accuracy | Primary Challenge |  
|------------|--------------|-------------------|  
| Bar Charts | 85% | Value reading precision |  
| Line Charts | 78% | Point interpolation |  
| Pie Charts | 82% | Percentage calculation |  
| Scatter Plots | 71% | Pattern recognition |  
| Heatmaps | 68% | Color-to-value mapping |  
  
---  
  
### 🔀 Diagrams: Structural Understanding  
  
#### Primary Metrics  
  
**1. F1 Score (Component Extraction)**  
```python  
def f1_score(pred_components, gt_components):  
    """    For multi-element answers like node lists, connections    """    tp = len(pred_components & gt_components)    precision = tp / len(pred_components)    recall = tp / len(gt_components)    return 2 * (precision * recall) / (precision + recall)  
```  
  
**When to use:** Component identification, relationship extraction    
**Typical F1:** 0.70-0.85 for flowcharts, 0.60-0.75 for complex diagrams  
  
**2. LLM-as-Judge Structural Correctness**  
```  
Prompt: Evaluate if the model correctly identified:  
1. All key components (nodes, edges, labels)  
2. Relationships between components  
3. Sequential/hierarchical structure  
  
Response: CORRECT | PARTIAL | INCORRECT + reasoning  
```  
  
**3. Exact Match (for counting tasks)**  
- "How many decision nodes?" → Exact integer match  
- Typical accuracy: 75-85%  
  
#### Stratified Metrics  
  
| Diagram Type | Avg Accuracy | Primary Challenge |  
|--------------|--------------|-------------------|  
| Flowcharts | 78% | Sequential reasoning |  
| Network Diagrams | 72% | Connectivity understanding |  
| Organizational Charts | 82% | Hierarchical structure |  
| Technical Diagrams | 65% | Domain-specific symbols |  
| Venn Diagrams | 80% | Set relationships |  
  
---  
  
### 📋 Tables: Logical Reasoning  
  
#### Primary Metrics  
  
**1. Exact Match**  
```python  
def exact_match(prediction, ground_truth):  
    """Strict matching for structured answers"""    return normalize(prediction) == normalize(ground_truth)  
```  
  
**When to use:** Direct lookup, categorical answers    
**Typical accuracy:** 85-95% for lookup, 60-75% for reasoning  
  
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
  
**⚠️ Critical Finding** (Wolff & Hulsebos 2025):  
- **BERTScore is unreliable** for table QA (inseparable distributions)  
- **BLEU fails** to distinguish correct from incorrect analytical answers  
- **LLM-as-judge is validated**: 93.75% accuracy for correct answers  
  
#### Stratified Metrics  
  
| Query Type | Avg Accuracy | Primary Challenge |  
|------------|--------------|-------------------|  
| Direct Lookup | 95% | Cell identification |  
| Aggregation (SUM, AVG) | 68% | Multi-cell operations |  
| Comparison (MAX, MIN) | 82% | Value comparison |  
| Multi-hop Reasoning | 55% | Sequential operations |  
| Arithmetic Operations | 71% | Calculation accuracy |  
  
---  
  
## Metadata Requirements  
  
### 🎯 Universal Metadata (All Data Types)  
  
```json  
{  
  "question_id": "unique_identifier",  
  "dataset_source": "ChartQA | AI2D | WikiTableQuestions",  
  "dataset_version": "v2.0",  
  "split": "train | validation | test",  
  "created_at": "2025-01-14T16:40:00Z",  
  "question": "What is the value for Category A?",  
  "ground_truth": "45",  
  "answer_type": "numerical | categorical | boolean | list | descriptive",  
  "task_metadata": {  
    "task_type": "value_extraction | comparison | composition | trend_analysis | structural",  
    "difficulty": "easy | medium | hard",  
    "difficulty_score": 2.5,  
    "num_reasoning_steps": 1,  
    "requires_calculation": false,  
    "requires_comparison": false,  
    "requires_ocr": true  
  },  
  "evaluation_config": {  
    "primary_metric": "numerical_accuracy | exact_match | f1_score",  
    "numerical_tolerance": 0.05,  
    "use_llm_judge": true,  
    "normalization_rules": ["remove_currency", "normalize_units"]  
  }  
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
    "has_grid": true,  
    "num_data_series": 4,  
    "num_data_points": 16,  
    "domain": "business | scientific | educational"  
  },  
  "visual_elements": {  
    "visual_complexity": "simple | moderate | complex",  
    "complexity_score": 6.5,  
    "has_overlapping_elements": false,  
    "has_small_text": false,  
    "axis_info": {  
      "x_axis": {"label": "Products", "type": "categorical"},  
      "y_axis": {"label": "Sales ($)", "type": "numerical", "scale": "linear"}  
    }  
  }  
}  
```  
  
**Complexity Scoring (0-10):**  
- Elements count: <5 (+1), 5-15 (+2), >15 (+3)  
- Multiple series: +1-2 points  
- Overlapping elements: +2 points  
- Small text: +1 point  
- Dual axes: +1 point  
  
---  
  
### 🔀 Diagram-Specific Metadata  
  
```json  
{  
  "image_metadata": {  
    "image_path": "/data/diagrams/flowchart_001.png",  
    "image_resolution": [1200, 900],  
    "image_quality": "high"  
  },  
  "diagram_metadata": {  
    "diagram_type": "flowchart | network_diagram | organizational_chart | technical_diagram",  
    "has_annotations": true,  
    "num_nodes": 12,  
    "num_edges": 15,  
    "num_decision_points": 3,  
    "layout_type": "hierarchical | circular | grid",  
    "domain": "business_process | software_architecture | organizational"  
  },  
  "structural_elements": {  
    "structural_complexity": "simple | moderate | complex",  
    "has_cycles": false,  
    "max_depth": 4,  
    "branching_factor": 2.5,  
    "has_color_coding": true  
  }  
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
    "has_numerical_columns": true,  
    "has_temporal_columns": true,  
    "requires_foreign_key_resolution": false,  
    "columns_involved": ["name", "score", "country"]  
  },  
  "query_metadata": {  
    "reasoning_type": ["lookup", "aggregation", "comparison", "multi_hop"],  
    "num_reasoning_steps": 2,  
    "requires_numerical_reasoning": true,  
    "answer_in_table": false  
  }  
}  
```  
  
**Key Research Finding** (Medium article):  
- **Markdown format**: Highest accuracy (lower token consumption)  
- **Key-value format**: Improved accuracy with metadata  
- **JSON format**: Increased context length (infeasible for some models)  
- **Metadata impact**: Key-value format improved most with schema metadata  
  
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
  
| Task | Description | Example | Difficulty |  
|------|-------------|---------|------------|  
| **Direct Lookup** | Single cell access | "What is Alice's age?" → "25" | Easy |  
| **Aggregation** | COUNT, SUM, AVG, MAX, MIN | "How many players from Australia?" → "3" | Medium |  
| **Comparison** | Find extrema | "Which player has highest score?" → "Alice" | Easy-Medium |  
| **Arithmetic** | Calculations | "Difference between max and min?" → "15" | Medium |  
| **Multi-hop** | Sequential operations | "Average age of Australian players?" → "28.3" | Hard |  
| **Temporal** | Date/time operations | "Events after 2020?" → "12" | Medium |  
  
---  
  
## Best Practices  
  
### 🎯 Metric Selection by Data Type  
  
| Scenario | Charts | Diagrams | Tables |  
|----------|--------|----------|--------|  
| **Baseline Evaluation** | Numerical Accuracy (±5%), LLM-as-Judge | F1 Score, LLM-as-Judge | Exact Match, LLM-as-Judge |  
| **Production Monitoring** | LLM-as-Judge, Latency | F1 Score, Latency | Exact Match, Numerical Accuracy |  
| **Research Analysis** | All metrics + robustness tests | F1 + stratified breakdowns | LLM-as-Judge + stratified |  
| **Error Analysis** | OCR accuracy, Value extraction | Component recall, Relationship precision | Cell accuracy, Operation correctness |  
  
### ⚠️ Critical Warnings  
  
**❌ DO NOT USE:**  
- **BERTScore for numerical answers** (charts, tables) - Unreliable per Wolff & Hulsebos 2025  
- **BLEU for analytical queries** (tables) - Cannot distinguish correct from incorrect  
- **Exact Match for charts** - Too strict for visual estimation  
- **Single overall metric** - Always stratify by task type  
  
**✅ DO USE:**  
- **LLM-as-judge** as primary metric (validated with 93.75% accuracy)  
- **Numerical tolerance** (±5%) for visual data  
- **Stratified evaluation** by data type, task type, difficulty  
- **Robustness tests** (resolution, style, occlusion for images)  
  
---  
  
### 🔧 Handling Edge Cases  
  
#### Charts  
- **Overlapping elements**: Increase tolerance to ±10%  
- **Log scales**: Apply log-scale aware normalization  
- **Dual axes**: Specify which axis in metadata  
- **3D charts**: Higher tolerance (±10-15%)  
  
#### Diagrams  
- **Ambiguous connections**: Use LLM-as-judge for partial credit  
- **Missing labels**: OCR confidence scoring  
- **Complex layouts**: Break into sub-components  
  
#### Tables  
- **Missing values**: Evaluate both accuracy and acknowledgement  
- **Duplicate rows**: Test deduplication capability  
- **Structural variations**: Column/row permutation consistency  
- **Multi-table queries**: Foreign key resolution accuracy  
  
  
  
## Real-World Examples  
  
### 📊 Chart Examples (from provided data)  
  
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
  
### 🔀 Diagram Examples (from provided data)  
  
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
  
### 📋 Table Examples (from provided data)  
  
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