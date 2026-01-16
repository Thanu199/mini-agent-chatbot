#!/bin/bash

# Create virtual environment

python -m venv venv

# Activate virtual environment

source venv/bin/activate

# Install dependencies

pip install -r requirements.txt

# Run FastAPI server

uvicorn app:app --reload --port 8001
