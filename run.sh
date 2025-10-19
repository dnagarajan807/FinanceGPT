#!/bin/bash
export OPENAI_API_KEY=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
uvicorn app.main:app --host 0.0.0.0 --port 8000
