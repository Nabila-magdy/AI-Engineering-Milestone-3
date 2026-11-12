# Milestone 3 - Deterministic Schema Extraction Engine

## Project Overview
This project implements a schema-constrained generation engine to extract structured information from text using a local Large Language Model (LLM).

The goal is to compare unconstrained generation with schema-constrained generation and evaluate their performance and output reliability.

## Model and Tools
- **Model:** Qwen 2.5 - 1.5B
- **Runtime:** Ollama
- **Programming Language:** Python
- **Validation Library:** Pydantic
- **API:** Ollama Generate API

## Project Structure
- `schema.py` - Defines the Pydantic data model.
- `unconstrained.py` - Generates JSON without schema constraints and validates the output.
- `constrained.py` - Uses JSON Schema to guide structured output generation.
- `benchmark.py` - Compares latency, token generation speed, and schema validation errors.
- `results.txt` - Contains benchmark results.

## Data Schema
The project extracts the following water station information:

- `station_name`: String
- `governorate`: String
- `water_level`: Float
- `date`: Date

## Evaluation Metrics
1. **Latency:** Average time required to generate a response.
2. **Tokens per Second:** Measures generation throughput.
3. **Schema Validation Error Rate:** Percentage of generated outputs that fail Pydantic schema validation.

## Benchmark Results

| Metric | Unconstrained | Constrained |
|---|---:|---:|
| Average Latency | 14.44 sec | 8.35 sec |
| Tokens/sec | 9.74 | 9.02 |
| Schema Validation Error Rate | 100% | 0% |

## Results Analysis
- Unconstrained generation produced outputs with incorrect or missing field names.
- Constrained generation consistently followed the required Pydantic schema in the three tested generations.
- Constrained generation achieved lower average latency in this experiment.
- Unconstrained generation achieved slightly higher token throughput.

## Conclusion
The experiment shows that schema-constrained generation can improve output consistency and reliability when extracting structured data.

Using JSON Schema with Ollama helped the model generate outputs that matched the required Pydantic structure.

## Implementation Note
This project uses Ollama's JSON Schema structured output feature through the `format` parameter. This demonstrates schema-constrained generation; explicit FSM decoding has not been independently verified.
# AI-Engineering-Milestone-3
