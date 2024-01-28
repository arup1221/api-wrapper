#!/bin/bash

# Start FastAPI server in the background
uvicorn myapi:app --host 0.0.0.0 --port 8000 --reload &

# Run the Python script
python test_threaded_session.py
