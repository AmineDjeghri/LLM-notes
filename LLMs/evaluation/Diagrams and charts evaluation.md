## News and updates
- item 1
## Easy guides

  
- [Overview](#overview)  
- [Chart and Diagram Types](#chart-and-diagram-types)  
- [Task Categories](#task-categories)  
- [Evaluation Metrics](#evaluation-metrics)  
- [Data Format Requirements](#data-format-requirements)  
- [Metadata Schema](#metadata-schema)  
- [Evaluation Pipeline](#evaluation-pipeline)  
- [Best Practices](#best-practices)  
- [Benchmarks and Datasets](#benchmarks-and-datasets)  
  
---  
  
### Overview  
  
This guide provides a standardized framework for evaluating vision-language models on chart and diagram understanding tasks. Charts and diagrams present unique challenges compared to natural images or text-only data:  
  
- **Visual-numerical reasoning**: Extracting precise numerical values from visual representations  
- **Spatial understanding**: Interpreting axes, legends, labels, and spatial relationships  
- **Multi-modal integration**: Combining visual perception with quantitative reasoning  
- **Domain-specific conventions**: Understanding chart types, symbols, and visual encodings  
  
#### Key Challenges  
  
1. **OCR and Text Recognition**: Reading labels, axis values, legends, and annotations  
2. **Visual Perception**: Identifying chart elements (bars, lines, points, shapes)  
3. **Numerical Extraction**: Precise value reading from visual scales  
4. **Reasoning**: Performing calculations, comparisons, and trend analysis  
5. **Robustness**: Handling variations in style, quality, and complexity  
  
---  
  
### Chart and Diagram Types  
  
#### 1. Statistical Charts  
  
##### Bar Charts  
- **Vertical/Horizontal bars**  
- **Grouped/Stacked bars**  
- **Use cases**: Categorical comparisons, distributions  
  
**Evaluation Focus:**  
- Value extraction accuracy  
- Category identification  
- Comparison reasoning  
  
##### Line Charts  
- **Single/Multiple lines**  
- **Time series data**  
- **Use cases**: Trends, changes over time  
  
**Evaluation Focus:**  
- Trend identification  
- Point value extraction  
- Slope/rate of change reasoning  
  
##### Pie Charts  
- **Proportional segments**  
- **Percentage distributions**  
- **Use cases**: Part-to-whole relationships  
  
**Evaluation Focus:**  
- Percentage accuracy  
- Segment identification  
- Proportional reasoning  
  
##### Scatter Plots  
- **Point distributions**  
- **Correlation patterns**  
- **Use cases**: Relationships between variables  
  
**Evaluation Focus:**  
- Pattern recognition  
- Outlier identification  
- Correlation reasoning  
  
#### 2. Scientific Diagrams  
  
##### Flowcharts  
- **Process flows**  
- **Decision trees**  
- **Use cases**: Workflows, algorithms  
  
**Evaluation Focus:**  
- Node identification  
- Edge/connection understanding  
- Sequential reasoning  
  
##### Network Diagrams  
- **Graph structures**  
- **Relationships**  
- **Use cases**: Systems, connections  
  
**Evaluation Focus:**  
- Node/edge extraction  
- Path finding  
- Connectivity reasoning  
  
##### Technical Diagrams  
- **Engineering drawings**  
- **Circuit diagrams**  
- **Architectural plans**  
  
**Evaluation Focus:**  
- Component identification  
- Spatial relationships  
- Domain-specific symbol recognition  
  
#### 3. Infographics  
  
- **Mixed visual elements**  
- **Text + charts + icons**  
- **Use cases**: Data storytelling  
  
**Evaluation Focus:**  
- Multi-element integration  
- Information extraction  
- Hierarchical understanding  
  
---  
  
### Task Categories  
  
#### 1. Direct Value Extraction  
  
**Description:** Reading explicit values from the chart  
  
**Examples:**  
```  
Chart: Bar chart showing sales by quarter  
Q: "What is the sales value for Q2?"  
A: "$45,000"  
  
Chart: Line chart of temperature over time  
Q: "What was the temperature at 3 PM?"  
A: "72°F"  
```  
  
**Difficulty Factors:**  
- Scale granularity  
- Label visibility  
- Overlapping elements  
  
#### 2. Comparative Reasoning  
  
**Description:** Comparing values or trends  
  
**Examples:**  
```  
Chart: Bar chart of product sales  
Q: "Which product had the highest sales?"  
A: "Product A"  
  
Chart: Multi-line chart  
Q: "Which line shows the steepest increase?"  
A: "The blue line (Revenue)"  
```  
  
**Difficulty Factors:**  
- Number of elements to compare  
- Visual similarity  
- Implicit vs explicit comparisons  
  
#### 3. Compositional Reasoning  
  
**Description:** Calculations or aggregations  
  
**Examples:**  
```  
Chart: Stacked bar chart  
Q: "What is the total value across all categories?"  
A: "250"  
  
Chart: Pie chart  
Q: "What percentage do the top 3 segments represent?"  
A: "75%"  
```  
  
**Difficulty Factors:**  
- Number of operations  
- Precision requirements  
- Multi-step reasoning  
  
#### 4. Trend Analysis  
  
**Description:** Identifying patterns and changes  
  
**Examples:**  
```  
Chart: Line chart over time  
Q: "Describe the trend from 2020 to 2023"  
A: "Steady increase with a dip in 2022"  
  
Chart: Scatter plot  
Q: "Is there a positive or negative correlation?"  
A: "Positive correlation"  
```  
  
**Difficulty Factors:**  
- Temporal complexity  
- Pattern subtlety  
- Descriptive precision  
  
#### 5. Structural Understanding  
  
**Description:** Understanding chart components and layout  
  
**Examples:**  
```  
Chart: Complex multi-panel chart  
Q: "What does the legend indicate?"  
A: "Blue represents revenue, red represents costs"  
  
Diagram: Flowchart  
Q: "How many decision nodes are in the diagram?"  
A: "3"  
```  
  
**Difficulty Factors:**  
- Layout complexity  
- Element density  
- Domain conventions  
  
---  
  
### Evaluation Metrics  
  
### Core Metrics  
  
#### 1. Exact Match (EM) Accuracy  
  
```python  
def exact_match(prediction, ground_truth):  
    """Strict string matching"""    return 1 if prediction.strip().lower() == ground_truth.strip().lower() else 0  
```  
  
**When to use:** Baseline for categorical answers  
  
**Limitations:** Too strict for numerical answers with formatting variations  
  
#### 2. Relaxed Accuracy  
  
```python  
def relaxed_match(prediction, ground_truth):  
    """Handles common variations"""    pred_norm = normalize_answer(prediction)    gt_norm = normalize_answer(ground_truth)    return pred_norm == gt_norm  
def normalize_answer(text):  
    """Normalize numbers, units, formatting"""    # Remove currency symbols: "$45,000" -> "45000"    # Normalize units: "45k" -> "45000"    # Handle decimals: "3.14" = "3.1400"    # Case insensitive    return normalized_text  
```  
  
**When to use:** Numerical answers, formatted values  
  
#### 3. Numerical Accuracy with Tolerance  
  
```python  
def numerical_accuracy(pred, gt, tolerance=0.05):  
    """    Allow small deviations for visual estimation        Args:  
        tolerance: Relative tolerance (5% default)    """    try:        pred_num = parse_number(pred)        gt_num = parse_number(gt)                # Relative error  
        rel_error = abs(pred_num - gt_num) / abs(gt_num)        return rel_error <= tolerance    except:        return False  
def parse_number(text):  
    """Extract numerical value from text"""    # Handle: "45,000", "$45k", "45%", "45.5M"    return float_value  
```  
  
**When to use:** Value extraction from charts (accounts for visual estimation errors)  
  
**Tolerance levels:**  
- **Strict (±1%)**: High-precision charts with clear scales  
- **Standard (±5%)**: Typical charts with reasonable scales  
- **Relaxed (±10%)**: Low-resolution or complex charts  
  
#### 4. Ranking Accuracy  
  
```python  
def ranking_accuracy(pred_list, gt_list):  
    """    For ordered comparisons (e.g., "rank products by sales")    """    from scipy.stats import kendalltau        # Kendall's Tau correlation  
    tau, p_value = kendalltau(pred_list, gt_list)    return tau  
def top_k_accuracy(pred_list, gt_list, k=3):  
    """Check if top-k items match"""    pred_top_k = set(pred_list[:k])    gt_top_k = set(gt_list[:k])    return len(pred_top_k & gt_top_k) / k  
```  
  
**When to use:** Ranking/ordering tasks  
  
#### 5. F1 Score (for multi-label answers)  
  
```python  
def f1_score(pred_set, gt_set):  
    """For answers with multiple elements"""    if len(gt_set) == 0:        return 1.0 if len(pred_set) == 0 else 0.0        tp = len(pred_set & gt_set)  
    fp = len(pred_set - gt_set)    fn = len(gt_set - pred_set)        precision = tp / (tp + fp) if (tp + fp) > 0 else 0  
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0        if precision + recall == 0:  
        return 0        return 2 * (precision * recall) / (precision + recall)  
```  
  
**When to use:** Multi-element answers (e.g., "List all categories above 50")  
  
### LLM-as-Judge Metrics  
  
#### 6. Correctness (LLM-judged)  
  
**Prompt Template:**  
```  
You are evaluating a vision-language model's answer to a question about a chart/diagram.  
  
Question: {question}  
Ground Truth Answer: {ground_truth}  
Model's Answer: {prediction}  
  
Evaluate if the model's answer is correct. Consider:  
- Semantic equivalence (e.g., "45000" = "$45k" = "45 thousand")  
- Reasonable approximations for visual estimates (±5% tolerance)  
- Correct units and formatting  
  
Respond with:  
- "CORRECT" if the answer is factually correct  
- "INCORRECT" if the answer is wrong  
- "PARTIAL" if partially correct (e.g., right trend but wrong magnitude)  
  
Justification: [brief explanation]  
```  
  
**Scoring:**  
- CORRECT = 1.0  
- PARTIAL = 0.5  
- INCORRECT = 0.0  
  
#### 7. Reasoning Quality (LLM-judged)  
  
**Prompt Template:**  
```  
Question: {question}  
Model's Answer: {prediction}  
Model's Reasoning: {reasoning_trace}  
  
Evaluate the quality of reasoning on a scale of 1-5:  
1 = No reasoning or completely wrong logic  
2 = Flawed reasoning with major errors  
3 = Partially correct reasoning with gaps  
4 = Mostly sound reasoning with minor issues  
5 = Excellent, complete reasoning  
  
Consider:  
- Correct identification of chart elements  
- Appropriate operations/calculations  
- Logical flow  
- Handling of edge cases  
  
Score: [1-5]  
Justification: [brief explanation]  
```  
  
### Stratified Metrics  
  
#### 8. Accuracy by Chart Type  
  
```python  
results = {  
    "bar_chart": {"accuracy": 0.85, "count": 200},    "line_chart": {"accuracy": 0.78, "count": 180},    "pie_chart": {"accuracy": 0.82, "count": 150},    "scatter_plot": {"accuracy": 0.71, "count": 120},    "flowchart": {"accuracy": 0.68, "count": 100},    "network_diagram": {"accuracy": 0.65, "count": 80}}  
```  
  
#### 9. Accuracy by Task Type  
  
```python  
results = {  
    "value_extraction": {"accuracy": 0.88, "count": 300},    "comparison": {"accuracy": 0.82, "count": 250},    "composition": {"accuracy": 0.71, "count": 200},    "trend_analysis": {"accuracy": 0.68, "count": 180},    "structural": {"accuracy": 0.75, "count": 150}}  
```  
  
#### 10. Accuracy by Visual Complexity  
  
```python  
results = {  
    "simple": {"accuracy": 0.89, "num_elements": "<5"},    "moderate": {"accuracy": 0.76, "num_elements": "5-15"},    "complex": {"accuracy": 0.62, "num_elements": ">15"}}  
```  
  
### Robustness Metrics  
  
#### 11. Style Variation Robustness  
  
**Test Scenarios:**  
- Different color schemes  
- Various fonts and sizes  
- Grid vs no-grid  
- 3D vs 2D rendering  
  
```python  
def evaluate_style_robustness(model, question, chart_variants):  
    """Test consistency across visual style variations"""    answers = []    for variant in chart_variants:        answer = model.predict(variant, question)        answers.append(answer)        # All answers should be consistent  
    consistency = len(set(answers)) == 1    return {        "consistent": consistency,        "unique_answers": len(set(answers)),        "answers": answers    }  
```  
  
#### 12. Resolution Robustness  
  
**Test Scenarios:**  
- High resolution (1920x1080)  
- Medium resolution (800x600)  
- Low resolution (400x300)  
  
```python  
def evaluate_resolution_robustness(model, question, resolutions):  
    """Test performance across different image resolutions"""    results = {}    for res, image in resolutions.items():        answer = model.predict(image, question)        results[res] = answer    return results  
```  
  
#### 13. Occlusion Robustness  
  
**Test Scenarios:**  
- Partial legend occlusion  
- Missing axis labels  
- Cropped regions  
  
```python  
def evaluate_occlusion_robustness(model, dataset_with_occlusions):  
    """Test handling of partially visible charts"""    results = {        "full_chart": [],        "partial_occlusion": [],        "significant_occlusion": []    }    # Evaluate degradation with increasing occlusion    return results  
```  
  
---  
  
## Data Format Requirements  
  
### Input Data Schema  
  
```json  
{  
  "question_id": "chart_qa_001",  
  "dataset_source": "ChartQA",  
  "image_path": "/path/to/chart.png",  
  "image_url": "https://example.com/chart.png",  
  "chart_type": "bar_chart",  
  "question": "What is the value for Category A?",  
  "ground_truth": "45",  
  "answer_type": "numerical",  
  "metadata": {  
    "task_type": "value_extraction",  
    "difficulty": "easy",  
    "visual_complexity": "simple",  
    "num_elements": 5,  
    "requires_calculation": false,  
    "chart_source": "synthetic",  
    "image_resolution": [800, 600],  
    "has_legend": true,  
    "has_title": true  
  }  
}  
```  
  
### Output Format  
  
```json  
{  
  "question_id": "chart_qa_001",  
  "prediction": "45",  
  "confidence": 0.92,  
  "reasoning": "Located bar for Category A, read value from y-axis scale at approximately 45",  
  "extracted_elements": {  
    "chart_type": "bar_chart",  
    "categories": ["A", "B", "C", "D"],  
    "values": [45, 32, 58, 41],  
    "axis_labels": {"x": "Categories", "y": "Values"}  
  },  
  "processing_time_ms": 1250,  
  "timestamp": "2025-01-12T09:00:00Z"  
}  
```  
  
---  
  
## Metadata Schema  
  
### Required Fields  
  
```json  
{  
  "question_id": "string (unique)",  
  "dataset_source": "string",  
  "image_path": "string",  
  "chart_type": "string",  
  "question": "string",  
  "ground_truth": "string"  
}  
```  
  
### Recommended Metadata  
  
```json  
{  
  "task_type": "value_extraction | comparison | composition | trend_analysis | structural",  
  "answer_type": "numerical | categorical | boolean | descriptive | list",  
  "difficulty": "easy | medium | hard",  
  "visual_complexity": "simple | moderate | complex",  
  "num_elements": "integer (bars, lines, nodes, etc.)",  
  "num_reasoning_steps": "integer",  
  "requires_calculation": "boolean",  
  "requires_ocr": "boolean",  
  "chart_source": "synthetic | real_world | screenshot",  
  "image_resolution": "[width, height]",  
  "image_quality": "high | medium | low",  
  "has_legend": "boolean",  
  "has_title": "boolean",  
  "has_grid": "boolean",  
  "color_scheme": "string",  
  "domain": "business | scientific | educational | general"  
}  
```  
  
### Optional Fields  
  
```json  
{  
  "chart_title": "string",  
  "axis_labels": {"x": "string", "y": "string"},  
  "data_source": "string",  
  "annotation_confidence": "float (0-1)",  
  "human_verified": "boolean",  
  "edge_cases": ["list of special considerations"],  
  "related_questions": ["list of question_ids"]  
}  
```  
  
---  
  
## Best Practices  
  
### 1. Handling Multi-Element Answers  
  
**For list-type answers:**  
```python  
# Question: "List all categories with values above 50"  
# Ground truth: ["A", "C", "E"]  
# Prediction: ["A", "C"]  
  
# Use F1 score, not exact match  
f1 = f1_score(pred_set={"A", "C"}, gt_set={"A", "C", "E"})  
# F1 = 0.80 (partial credit)  
```  
  

### 2. Stratified Evaluation Priority  
  
**Always stratify by:**  
1. **Chart type** (most important for understanding model capabilities)  
2. **Task type** (identifies reasoning strengths/weaknesses)  
3. **Visual complexity** (reveals scalability limits)  
4. **Difficulty level** (standard practice)  
  
### 3. LLM-as-Judge Best Practices  
- Provide clear evaluation criteria  
- Use numerical tolerance guidelines in prompts  
- Include ground truth for anchoring  
- Log judge reasoning for debugging  
- Validate with human annotations periodically  

### 4. Error Categorization  
  
**Standard error types:**  
  
1. **OCR Errors**: Failed to read text labels  
2. **Value Extraction Errors**: Wrong numerical value read  
3. **Chart Element Misidentification**: Confused bars/lines/points  
4. **Reasoning Errors**: Wrong operation or logic  
5. **Calculation Errors**: Correct values but wrong computation  
6. **Legend/Label Confusion**: Mismatched categories  
  
```python  
def classify_error(prediction, ground_truth, metadata):  
    """Automatically categorize error type"""    # Implement heuristics or use LLM to classify    return error_type  
```  
  
### 9. Handling Edge Cases  
  
**Common edge cases:**  
  
- **Overlapping elements**: Multiple bars/lines at same position  
- **Log scales**: Non-linear axis scales  
- **Dual axes**: Charts with two y-axes  
- **Missing legends**: Implicit category identification  
- **Rotated labels**: Vertical or angled text  
- **Scientific notation**: Values like "1.5e6"  
  
**Mitigation:**  
```python  
# Flag edge cases in metadata  
metadata["edge_cases"] = [  
    "log_scale",    "dual_axis",    "rotated_labels"]  
  
# Use specialized evaluation for flagged cases  
if "log_scale" in metadata["edge_cases"]:  
    # Apply log-scale aware tolerance    pass  
```  
  

## Example Evaluation Results  
  
```json  
{  
  "experiment_id": "chart_qa_eval_001",  
  "timestamp": "2025-01-12T09:00:00Z",  
  "model": "gpt-4-vision-preview",  
  "dataset": "ChartQA",  
  "overall_metrics": {  
    "exact_match": 0.68,  
    "relaxed_accuracy": 0.76,  
    "numerical_accuracy_5pct": 0.82,  
    "llm_correctness": 0.85,  
    "llm_reasoning_quality": 4.2,  
    "total_questions": 1000  
  },  
  "by_chart_type": {  
    "bar_chart": {"accuracy": 0.84, "count": 350},  
    "line_chart": {"accuracy": 0.78, "count": 280},  
    "pie_chart": {"accuracy": 0.81, "count": 220},  
    "scatter_plot": {"accuracy": 0.72, "count": 150}  
  },  
  "by_task_type": {  
    "value_extraction": {"accuracy": 0.88, "count": 300},  
    "comparison": {"accuracy": 0.82, "count": 250},  
    "composition": {"accuracy": 0.71, "count": 200},  
    "trend_analysis": {"accuracy": 0.68, "count": 150},  
    "structural": {"accuracy": 0.75, "count": 100}  
  },  
  "by_visual_complexity": {  
    "simple": {"accuracy": 0.89, "count": 400},  
    "moderate": {"accuracy": 0.76, "count": 400},  
    "complex": {"accuracy": 0.62, "count": 200}  
  },  
  "robustness_metrics": {  
    "style_consistency": 0.85,  
    "resolution_degradation": {  
      "high_res": 0.85,  
      "medium_res": 0.82,  
      "low_res": 0.71  
    },  
    "occlusion_robustness": {  
      "no_occlusion": 0.85,  
      "partial": 0.73,  
      "significant": 0.52  
    }  
  },  
  "error_analysis": {  
    "ocr_errors": {"count": 45, "percentage": 4.5},  
    "value_extraction_errors": {"count": 82, "percentage": 8.2},  
    "reasoning_errors": {"count": 58, "percentage": 5.8},  
    "calculation_errors": {"count": 35, "percentage": 3.5}  
  },  
  "performance": {  
    "avg_processing_time_ms": 1850,  
    "median_processing_time_ms": 1620,  
    "p95_processing_time_ms": 3200  
  }  
}  
```  
  
---  
  
## Quick Start Checklist  
  
- [ ] Prepare dataset in standardized format  
- [ ] Validate all images load correctly  
- [ ] Add required metadata (chart type, task type, difficulty)  
- [ ] Implement core metrics (EM, relaxed accuracy, numerical accuracy)  
- [ ] Set appropriate numerical tolerance (typically 5%)  
- [ ] Configure LLM-as-judge evaluation  
- [ ] Set up stratified evaluation (by chart type, task type)  
- [ ] Implement robustness tests (resolution, style, occlusion)  
- [ ] Run baseline evaluation  
- [ ] Perform error analysis with categorization  
- [ ] Generate comprehensive report with visualizations  
- [ ] Document configuration and results  

## Appendix: Common Pitfalls  
  
### 1. Over-reliance on Exact Match  
❌ **Problem**: "45000" ≠ "$45k" ≠ "45,000"    
✅ **Solution**: Use relaxed accuracy with normalization  
  
### 2. Ignoring Visual Estimation Errors  
❌ **Problem**: Penalizing "44.8" when ground truth is "45" (from visual reading)    
✅ **Solution**: Use numerical tolerance (±5%)  
  
### 3. Not Stratifying by Chart Type  
❌ **Problem**: Overall accuracy hides chart-specific weaknesses    
✅ **Solution**: Always report per-chart-type metrics  
  
### 4. Inadequate Error Analysis  
❌ **Problem**: Only reporting aggregate accuracy    
✅ **Solution**: Categorize errors (OCR, reasoning, calculation, etc.)  
  
### 5. Missing Robustness Tests  
❌ **Problem**: Model works on high-res synthetic charts but fails on real screenshots    
✅ **Solution**: Test across resolutions, styles, and quality levels  
  
### 6. Inconsistent Preprocessing  
❌ **Problem**: Different image sizes/formats across evaluation runs    
✅ **Solution**: Document and fix preprocessing pipeline  
  
### 7. Ignoring Cost Considerations  
❌ **Problem**: Using expensive vision models for every evaluation    
✅ **Solution**: Balance between automated metrics and LLM-as-judge  


  
### The Evaluation Pipeline  
  
```  
┌─────────────────────────────────────────────────────────────┐  
│                    1. DATASET CREATION                      │  
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │  
│  │ Collect      │→ │ Annotate     │→ │ Extract      │     │  
│  │ Images       │  │ Questions    │  │ Metadata     │     │  
│  └──────────────┘  └──────────────┘  └──────────────┘     │  
│                           ↓                                 │  
│                  ┌──────────────────┐                       │  
│                  │ Validate & QC    │                       │  
│                  └──────────────────┘                       │  
└─────────────────────────────────────────────────────────────┘  
                            ↓┌─────────────────────────────────────────────────────────────┐  
│                    2. MODEL INFERENCE                       │  
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │  
│  │ Load Image   │→ │ Run Model    │→ │ Extract      │     │  
│  │ + Question   │  │              │  │ Prediction   │     │  
│  └──────────────┘  └──────────────┘  └──────────────┘     │  
└─────────────────────────────────────────────────────────────┘  
                            ↓┌─────────────────────────────────────────────────────────────┐  
│                  3. METRIC CALCULATION                      │  
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │  
│  │ Overall      │  │ Stratified   │  │ Robustness   │     │  
│  │ Metrics      │  │ by Metadata  │  │ Tests        │     │  
│  └──────────────┘  └──────────────┘  └──────────────┘     │  
└─────────────────────────────────────────────────────────────┘  
                            ↓┌─────────────────────────────────────────────────────────────┐  
│                    4. ERROR ANALYSIS                        │  
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │  
│  │ Categorize   │→ │ Pattern      │→ │ Root Cause   │     │  
│  │ Errors       │  │ Discovery    │  │ Analysis     │     │  
│  └──────────────┘  └──────────────┘  └──────────────┘     │  
└─────────────────────────────────────────────────────────────┘  
                            ↓┌─────────────────────────────────────────────────────────────┐  
│                   5. REPORT GENERATION                      │  
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │  
│  │ Aggregate    │→ │ Visualize    │→ │ Generate     │     │  
│  │ Results      │  │ Findings     │  │ Report       │     │  
│  └──────────────┘  └──────────────┘  └──────────────┘     │  
└─────────────────────────────────────────────────────────────┘  
```  
  
### Why Metadata Matters at Each Stage  
  
**Stage 1 - Dataset Creation:**  
- Balance dataset across chart types, difficulties  
- Ensure coverage of edge cases  
- Document data provenance  
  
**Stage 2 - Model Inference:**  
- Select appropriate preprocessing  
- Configure model parameters  
- Track computational costs  
  
**Stage 3 - Metric Calculation:**  
- Choose metrics based on answer type  
- Apply appropriate tolerances  
- Enable stratified analysis  
  
**Stage 4 - Error Analysis:**  
- Group errors by metadata attributes  
- Identify systematic failures  
- Prioritize improvements  
  
**Stage 5 - Reporting:**  
- Generate comprehensive breakdowns  
- Compare across dimensions  
- Track progress over time  
  
---  
  
## Complete Metadata Schema  
  
### Level 1: Core Identifiers (REQUIRED)  
  
```json  
{  
  "question_id": "chart_qa_001",  
  "dataset_source": "ChartQA",  
  "dataset_version": "v2.0",  
  "split": "train",  
  "created_at": "2025-01-12T09:00:00Z",  
  "annotator_id": "annotator_001"  
}  
```  
  
**Purpose:** Unique identification and tracking  
  
### Level 2: Image Metadata (REQUIRED)  
  
```json  
{  
  "image_metadata": {  
    "image_path": "/data/charts/chart_001.png",  
    "image_url": "https://example.com/chart_001.png",  
    "image_hash": "sha256:abc123def456...",  
    "image_format": "PNG",  
    "image_size_bytes": 245678,  
    "image_resolution": [800, 600],  
    "image_aspect_ratio": 1.33,  
    "image_quality": "high",  
    "dpi": 150,  
    "color_mode": "RGB",  
    "has_transparency": false,  
    "file_created_at": "2025-01-10T14:30:00Z"  
  }  
}  
```  
  
**Purpose:** Image validation, preprocessing decisions, quality assessment  
  
### Level 3: Chart Structure Metadata (REQUIRED)  
  
```json  
{  
  "chart_metadata": {  
    "chart_type": "bar_chart",  
    "chart_subtype": "vertical_grouped",  
    "chart_source": "synthetic",  
    "chart_title": "Quarterly Sales by Product",  
    "has_title": true,  
    "has_legend": true,  
    "legend_position": "top_right",  
    "legend_entries": ["Product A", "Product B", "Product C", "Product D"],  
    "has_grid": true,  
    "grid_type": "horizontal",  
    "has_annotations": false,  
    "color_scheme": "default",  
    "num_colors": 4,  
    "is_3d": false,  
    "background_color": "white",  
    "domain": "business",  
    "data_source_attribution": "Synthetic data generator v1.0"  
  }  
}  
```  
  
**Purpose:** Chart type stratification, domain-specific evaluation  
  
**Chart Type Taxonomy:**  
```  
Statistical Charts:  
  - bar_chart (vertical, horizontal, grouped, stacked)  - line_chart (single, multiple, area)  - pie_chart (standard, donut, exploded)  - scatter_plot (standard, bubble, with_regression)  - histogram  - box_plot  - heatmap  
Scientific Diagrams:  
  - flowchart  - network_diagram  - tree_diagram  - venn_diagram  - organizational_chart  - circuit_diagram  - molecular_diagram  
Specialized:  
  - map_chart  - gantt_chart  - candlestick_chart  - radar_chart  - sankey_diagram```  
  

  
```  
  
**Purpose:** Complexity assessment, visual perception evaluation  
  
**Complexity Scoring:**  

### Level 5: Question & Answer Metadata (REQUIRED)  
  
```json  
{  
  "question_metadata": {  
    "question": "What is the sales value for Product A in Q2?",  
    "question_type": "specific_value",  
    "question_length_chars": 45,  
    "question_length_tokens": 11,  
    "ground_truth": "45",  
    "ground_truth_type": "numerical",  
    "ground_truth_unit": "$1000s",  
    "answer_format": "number",  
    "acceptable_answers": ["45", "45000", "$45k", "45 thousand"],  
    "answer_extraction_method": "visual_reading",  
    "numerical_precision_required": 2  
  }  
}  
```  
  
**Answer Type Taxonomy:**  
```  
- numerical (integer, float, percentage, currency)  
- categorical (single_choice, multiple_choice)  
- boolean (yes/no, true/false)  
- ordinal (ranking, ordering)  
- list (unordered_set, ordered_list)  
- descriptive (short_text, long_text)  
- comparative (greater_than, less_than, equal)  
- temporal (date, time, duration)  
```  
  
### Level 6: Task Metadata (REQUIRED)  
  
```json  
{  
  "task_metadata": {  
    "task_type": "value_extraction",  
    "task_category": "direct_reading",  
    "difficulty": "easy",  
    "difficulty_score": 2.5,  
    "num_reasoning_steps": 1,  
    "reasoning_types": ["visual_perception", "value_reading"],  
    "requires_calculation": false,  
    "calculation_type": null,  
    "requires_comparison": false,  
    "requires_aggregation": false,  
    "requires_ocr": true,  
    "ocr_difficulty": "easy",  
    "requires_domain_knowledge": false,  
    "time_estimate_seconds": 15  
  }  
}  
```  
  
**Task Type Taxonomy:**  
```  
Direct Tasks:  
  - value_extraction (single_value, multiple_values)  - element_identification (category, series, label)  - structure_understanding (layout, components)  
Reasoning Tasks:  
  - comparison (pairwise, ranking, extrema)  - composition (sum, average, percentage)  - trend_analysis (direction, magnitude, pattern)  - correlation_analysis (positive, negative, none)  - outlier_detection  
Complex Tasks:  
  - multi_hop_reasoning (2+ steps)  - cross_chart_reasoning (multiple charts)  - temporal_reasoning (time series analysis)  - spatial_reasoning (position, distance, area)```  
  
**Difficulty Scoring:**  
```python  
def calculate_difficulty_score(task_metadata, visual_elements):  
    """    Calculate difficulty score (1-10)    """    score = 1  # Base difficulty        # Reasoning steps (0-3 points)  
    score += min(task_metadata['num_reasoning_steps'] - 1, 3)        # Calculation required (+2 points)  
    if task_metadata['requires_calculation']:        score += 2        # Visual complexity (0-2 points)  
    complexity = visual_elements['visual_complexity']    if complexity == 'moderate':        score += 1    elif complexity == 'complex':        score += 2        # OCR difficulty (0-2 points)  
    ocr_diff = task_metadata.get('ocr_difficulty', 'easy')    if ocr_diff == 'medium':        score += 1    elif ocr_diff == 'hard':        score += 2        # Domain knowledge (+1 point)  
    if task_metadata['requires_domain_knowledge']:        score += 1        return min(score, 10)  
```  
  
### Level 7: Evaluation Configuration (RECOMMENDED)  
  
```json  
{  
  "evaluation_config": {  
    "primary_metric": "numerical_accuracy",  
    "numerical_tolerance": 0.05,  
    "tolerance_type": "relative",  
    "use_llm_judge": true,  
    "llm_judge_model": "gpt-4",  
    "normalization_rules": [  
      "remove_currency_symbols",      "normalize_units",      "case_insensitive"    ],  
    "acceptable_formats": ["number", "number_with_unit", "formatted_number"],  
    "evaluation_notes": "Standard numerical extraction with 5% tolerance"  
  }  
}  
```  
  
**Purpose:** Specify how to evaluate this specific question  
  
### Level 8: Quality & Provenance (RECOMMENDED)  
  
```json  
{  
  "quality_metadata": {  
    "annotation_confidence": 0.95,  
    "human_verified": true,  
    "verification_count": 2,  
    "inter_annotator_agreement": 1.0,  
    "has_ambiguity": false,  
    "ambiguity_notes": null,  
    "edge_cases": [],  
    "known_issues": [],  
    "review_status": "approved",  
    "last_reviewed_at": "2025-01-11T16:00:00Z"  
  },  
  "provenance": {  
    "original_source": "Synthetic generator",  
    "generation_method": "rule_based",  
    "generation_parameters": {  
      "template_id": "bar_chart_001",  
      "seed": 42  
    },  
    "modifications": [],  
    "license": "CC-BY-4.0",  
    "citation": "ChartQA Dataset v2.0"  
  }  
}  
```  
  
### Level 9: Relationships & Context (OPTIONAL)  
  
```json  
{  
  "relationships": {  
    "related_questions": ["chart_qa_002", "chart_qa_003"],  
    "question_group": "quarterly_sales_group",  
    "variant_of": null,  
    "parent_chart_id": "chart_001",  
    "sibling_questions": 5  
  },  
  "context": {  
    "scenario": "Business analytics dashboard",  
    "user_intent": "Performance monitoring",  
    "expected_use_case": "Executive reporting",  
    "background_info": "Q2 2024 sales data across product lines"  
  }  
}  
```  
  
## Summary  
  
### Critical Metadata Fields  
  
**Minimum Required (Level 1-3):**  
- Question ID, dataset source, split  
- Image path, resolution, format  
- Chart type, has_legend, has_title  
- Question, ground truth, answer type  
  
**Recommended (Level 4-6):**  
- Visual complexity score  
- Task type, difficulty score  
- Number of reasoning steps  
- Evaluation configuration  
  
**Optional but Valuable (Level 7-9):**  
- Quality metrics, verification status  
- Provenance and licensing  
- Relationships to other questions  
  
### Key Takeaways  
  
1. **Automate where possible** - Use ML models and CV techniques for metadata extraction  
2. **Validate rigorously** - Check completeness, consistency, balance, quality  
3. **Document thoroughly** - Include provenance, generation methods, known issues  
4. **Balance carefully** - Ensure representation across chart types, tasks, difficulties  
5. **Version control** - Track dataset versions and changes over time  
  
---  
  


## Tools / libraries 
- item 1

## Papers and research
- item 1

## Other resources 
- item 1


