# EduRAG-Compose

Unified Hybrid Retrieval–Generation Architecture for Structured Domain Reasoning.

## Install
pip install -r requirements.txt

## Run API
uvicorn api:app --reload

## Evaluate
python experiments/evaluate.py

## Architecture
- LightRAG: hierarchical clustering + FAISS
- GraphRAG: dependency graph traversal
- CAG: caching
- CoAG: recursive sub-queries

