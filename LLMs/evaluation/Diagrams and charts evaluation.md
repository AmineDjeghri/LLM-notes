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
  
## Evaluation Pipeline  
  
### Step 1: Data Preparation  
  
```python  
import json  
from PIL import Image  
  
def prepare_chart_dataset(raw_data, dataset_name):  
    """Standardize chart QA datasets"""    standardized = []        for item in raw_data:  
        # Load and validate image        image = Image.open(item['image_path'])                # Extract metadata  
        metadata = {            "chart_type": detect_chart_type(image),            "visual_complexity": calculate_complexity(image),            "task_type": classify_task(item['question']),            "answer_type": infer_answer_type(item['ground_truth'])        }                standardized.append({  
            "question_id": f"{dataset_name}_{item['id']}",            "dataset_source": dataset_name,            "image_path": item['image_path'],            "question": item['question'],            "ground_truth": item['answer'],            "metadata": metadata        })        return standardized  
```  
  
### Step 2: Model Inference  
  
```python  
def run_chart_qa_inference(model, dataset):  
    """Generate predictions for chart QA"""    predictions = []        for item in dataset:  
        # Load image        image = load_image(item['image_path'])                # Generate prediction  
        result = model.predict(            image=image,            question=item['question'],            return_reasoning=True        )                predictions.append({  
            "question_id": item['question_id'],            "prediction": result['answer'],            "confidence": result.get('confidence', None),            "reasoning": result.get('reasoning', None),            "processing_time_ms": result.get('time_ms', None)        })        return predictions  
```  
  
### Step 3: Metric Calculation  
  
```python  
def evaluate_chart_qa(predictions, ground_truth, metadata):  
    """Calculate comprehensive metrics"""    results = {        "overall": {},        "by_chart_type": {},        "by_task_type": {},        "by_difficulty": {},        "robustness": {}    }        # Overall metrics  
    results["overall"]["exact_match"] = calculate_exact_match(predictions, ground_truth)    results["overall"]["relaxed_accuracy"] = calculate_relaxed_accuracy(predictions, ground_truth)    results["overall"]["numerical_accuracy_5pct"] = calculate_numerical_accuracy(        predictions, ground_truth, tolerance=0.05    )        # Stratified by chart type  
    for chart_type in ["bar_chart", "line_chart", "pie_chart", "scatter_plot"]:        subset = filter_by_chart_type(predictions, ground_truth, metadata, chart_type)        results["by_chart_type"][chart_type] = calculate_metrics(subset)        # Stratified by task type  
    for task_type in ["value_extraction", "comparison", "composition", "trend_analysis"]:        subset = filter_by_task_type(predictions, ground_truth, metadata, task_type)        results["by_task_type"][task_type] = calculate_metrics(subset)        # LLM-as-judge evaluation  
    results["overall"]["llm_correctness"] = llm_judge_correctness(        predictions, ground_truth, metadata    )    results["overall"]["llm_reasoning_quality"] = llm_judge_reasoning(        predictions, metadata    )        return results  
```  
  
### Step 4: Error Analysis  
  
```python  
def analyze_errors(predictions, ground_truth, metadata):  
    """Categorize and analyze errors"""    errors = {        "ocr_errors": [],        "value_extraction_errors": [],        "reasoning_errors": [],        "chart_type_misidentification": [],        "calculation_errors": []    }        for pred, gt, meta in zip(predictions, ground_truth, metadata):  
        if pred['prediction'] != gt:            error_type = classify_error(pred, gt, meta)            errors[error_type].append({                "question_id": pred['question_id'],                "prediction": pred['prediction'],                "ground_truth": gt,                "metadata": meta            })        # Generate error statistics  
    error_stats = {        error_type: {            "count": len(error_list),            "percentage": len(error_list) / len(predictions) * 100        }        for error_type, error_list in errors.items()    }        return errors, error_stats  
```  
  
### Complete Pipeline  
  
```python  
def evaluate_chart_understanding(model, datasets, output_dir):  
    """Full evaluation pipeline for chart understanding"""    all_results = {}        for dataset_name, dataset_path in datasets.items():  
        print(f"Evaluating on {dataset_name}...")                # Load and prepare data  
        raw_data = load_dataset(dataset_path)        prepared_data = prepare_chart_dataset(raw_data, dataset_name)                # Run inference  
        predictions = run_chart_qa_inference(model, prepared_data)                # Calculate metrics  
        results = evaluate_chart_qa(            predictions=predictions,            ground_truth=[item['ground_truth'] for item in prepared_data],            metadata=[item['metadata'] for item in prepared_data]        )                # Error analysis  
        errors, error_stats = analyze_errors(            predictions,            [item['ground_truth'] for item in prepared_data],  
            [item['metadata'] for item in prepared_data]        )                results['error_analysis'] = error_stats  
        all_results[dataset_name] = results                # Save results  
        save_json(results, f"{output_dir}/{dataset_name}_results.json")        save_error_examples(errors, f"{output_dir}/{dataset_name}_errors.json")        # Generate report  
    generate_report(all_results, f"{output_dir}/evaluation_report.html")        return all_results  
```  
  
---  
  
## Best Practices  
  
### 1. Image Quality Considerations  
  
✅ **Do:**  
- Test across multiple resolutions  
- Validate image loading and preprocessing  
- Check for corrupted or invalid images  
- Normalize image formats (PNG, JPG, SVG)  
  
❌ **Don't:**  
- Assume all images are high quality  
- Ignore resolution effects on performance  
- Skip validation of image dimensions  
  
### 2. Numerical Tolerance Selection  
  
**Guidelines:**  
  
| Chart Quality | Recommended Tolerance | Use Case |  
|---------------|----------------------|----------|  
| High-res, clear scales | ±1-2% | Scientific charts, precise data |  
| Standard quality | ±5% | Business charts, typical use |  
| Low-res, unclear | ±10% | Screenshots, compressed images |  
  
**Implementation:**  
```python  
def adaptive_tolerance(image_quality, chart_type):  
    """Select tolerance based on image characteristics"""    if image_quality == "high" and chart_type in ["bar_chart", "line_chart"]:        return 0.02  # 2%    elif image_quality == "medium":        return 0.05  # 5%    else:        return 0.10  # 10%  
```  
  
### 3. Handling Multi-Element Answers  
  
**For list-type answers:**  
```python  
# Question: "List all categories with values above 50"  
# Ground truth: ["A", "C", "E"]  
# Prediction: ["A", "C"]  
  
# Use F1 score, not exact match  
f1 = f1_score(pred_set={"A", "C"}, gt_set={"A", "C", "E"})  
# F1 = 0.80 (partial credit)  
```  
  
### 4. Chart Type Detection  
  
**Automated classification:**  
```python  
def detect_chart_type(image):  
    """    Use heuristics or ML classifier to identify chart type    Helps in stratified evaluation    """    # Option 1: Rule-based (check for specific visual patterns)    # Option 2: Train a classifier    # Option 3: Use vision model to classify        return chart_type  # "bar_chart", "line_chart", etc.  
```  
  
### 5. Stratified Evaluation Priority  
  
**Always stratify by:**  
1. **Chart type** (most important for understanding model capabilities)  
2. **Task type** (identifies reasoning strengths/weaknesses)  
3. **Visual complexity** (reveals scalability limits)  
4. **Difficulty level** (standard practice)  
  
### 6. LLM-as-Judge Best Practices  
  
✅ **Do:**  
- Provide clear evaluation criteria  
- Use numerical tolerance guidelines in prompts  
- Include ground truth for anchoring  
- Log judge reasoning for debugging  
- Validate with human annotations periodically  
  
❌ **Don't:**  
- Use vague evaluation criteria  
- Ignore cost considerations (vision + text tokens)  
- Skip validation against human judgments  
  
### 7. Robustness Testing  
  
**Required tests:**  
  
```python  
def comprehensive_robustness_suite(model, dataset):  
    """Test model robustness across variations"""        results = {  
        # Style variations        "style_robustness": test_style_variations(model, dataset),                # Resolution variations  
        "resolution_robustness": test_resolutions(model, dataset),                # Occlusion scenarios  
        "occlusion_robustness": test_occlusions(model, dataset),                # Noise and compression  
        "noise_robustness": test_noise_levels(model, dataset),                # Color scheme variations  
        "color_robustness": test_color_schemes(model, dataset)    }        return results  
```  
  
### 8. Error Categorization  
  
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
  
### 10. Reproducibility  
  
✅ **Ensure:**  
- Fixed random seeds for sampling  
- Version-locked dependencies  
- Saved model checkpoints  
- Image preprocessing documentation  
- Timestamped results  
  
**Configuration file:**  
```json  
{  
  "experiment_id": "chart_qa_eval_001",  
  "timestamp": "2025-01-12T09:00:00Z",  
  "model": {  
    "name": "gpt-4-vision",  
    "version": "v1.0",  
    "parameters": {}  
  },  
  "dataset": {  
    "name": "ChartQA",  
    "version": "v2.0",  
    "split": "test"  
  },  
  "evaluation": {  
    "metrics": ["exact_match", "relaxed_accuracy", "numerical_accuracy"],  
    "numerical_tolerance": 0.05,  
    "llm_judge_model": "gpt-4"  
  },  
  "preprocessing": {  
    "image_resize": [800, 600],  
    "normalization": "standard"  
  }  
}  
```  
  
---  
  
## Benchmarks and Datasets  
  
### Popular Datasets  
  
#### 1. ChartQA  
- **Size**: 9,608 questions on 4,804 charts  
- **Chart types**: Bar, line, pie charts  
- **Source**: Real-world and synthetic  
- **Tasks**: Value extraction, comparison, reasoning  
- **URL**: https://github.com/vis-nlp/ChartQA  
  
#### 2. PlotQA  
- **Size**: 28.9M questions on 224K plots  
- **Chart types**: Bar, line, dot plots  
- **Source**: Synthetic  
- **Tasks**: Structural, data retrieval, reasoning  
- **URL**: https://github.com/NiteshMethani/PlotQA  
  
#### 3. FigureQA  
- **Size**: 100K questions on 100K figures  
- **Chart types**: Bar, line, pie charts  
- **Source**: Synthetic  
- **Tasks**: Binary questions about visual properties  
- **URL**: https://www.microsoft.com/en-us/research/project/figureqa-dataset/  
  
#### 4. DVQA (Data Visualization Question Answering)  
- **Size**: 3M questions on 300K charts  
- **Chart types**: Bar charts  
- **Source**: Synthetic  
- **Tasks**: Structure, data retrieval, reasoning  
- **URL**: https://github.com/kushalkafle/DVQA_dataset  
  
#### 5. Chart-to-Text  
- **Size**: 44,096 charts with summaries  
- **Chart types**: Line, bar, pie charts  
- **Source**: Statista  
- **Tasks**: Chart summarization, captioning  
- **URL**: https://github.com/JasonObeid/Chart2Text  
  
#### 6. Diagram Understanding Datasets  
  
**AI2D (AI2 Diagrams)**  
- **Size**: 5,000 diagrams  
- **Type**: Scientific diagrams  
- **Tasks**: Element identification, relationship extraction  
- **URL**: https://allenai.org/data/diagrams  
  
**FigureNet**  
- **Size**: 1.4M figures from scientific papers  
- **Type**: Mixed (charts, diagrams, plots)  
- **Tasks**: Classification, parsing  
- **URL**: https://github.com/allenai/figurenet  
  
---  
  
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
  
---  
  
## Tools & Libraries  
  
### Image Processing  
```bash  
pip install Pillow opencv-python```  
  
### OCR (if needed for ground truth extraction)  
```bash  
pip install pytesseract easyocr```  
  
### Evaluation Metrics  
```bash  
pip install scikit-learn scipy numpy```  
  
### Visualization  
```bash  
pip install matplotlib seaborn plotly```  
  
### Vision-Language Models  
```bash  
# OpenAI  
pip install openai  
  
# Anthropic  
pip install anthropic  
  
# Open source models  
pip install transformers torch  
```  
  
---  
  
## Additional Resources  
  
### Research Papers  
  
**Chart Understanding:**  
- "ChartQA: A Benchmark for Question Answering about Charts with Visual and Logical Reasoning" (Masry et al., 2022)  
- "PlotQA: Reasoning over Scientific Plots" (Methani et al., 2020)  
- "FigureQA: An Annotated Figure Dataset for Visual Reasoning" (Kahou et al., 2018)  
- "DVQA: Understanding Data Visualizations via Question Answering" (Kafle et al., 2018)  
  
**Vision-Language Models:**  
- "Flamingo: a Visual Language Model for Few-Shot Learning" (Alayrac et al., 2022)  
- "BLIP-2: Bootstrapping Language-Image Pre-training" (Li et al., 2023)  
- "GPT-4V(ision) System Card" (OpenAI, 2023)  
  
**Diagram Understanding:**  
- "AI2D: Diagram Understanding with Artificial Intelligence" (Kembhavi et al., 2016)  
- "Diagram Parse: Generating Textual Descriptions for Diagrams" (Seo et al., 2015)  
  
### Tutorials & Guides  
- Chart QA evaluation notebooks: https://github.com/vis-nlp/ChartQA  
- Vision-language model fine-tuning: https://huggingface.co/docs/transformers/tasks/visual_question_answering  
  
---  
  
## Contact & Support  
  
For questions or contributions to this evaluation framework, please refer to the project documentation or open an issue in the repository.  
  
**Last Updated:** January 2025    
**Version:** 1.0  
  
---  
  
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
  
---  
  
**End of Guide**


## Tools / libraries 
- item 1

## Papers and research
- item 1

## Other resources 
- item 1


