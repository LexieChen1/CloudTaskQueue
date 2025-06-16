# Cloud Task Queue: Document Import Summarizer

A cloud-based task queue system that processes and summarizes imported documents asynchronously. Designed to handle high volumes of file uploads and generate useful summaries from their contents.

## Project Overview

This system allows users to upload documents (e.g., CSV, PDF, DOCX, TXT). Once uploaded, each document is queued as a task. Background workers process the documents and return structured summaries such as:

- Number of rows/entries (CSV)
- Keyword/section extraction (PDF/DOCX)
- Word/character counts (TXT)
- Content overview (via NLP)

## Key Features

- REST API for submitting documents
- File storage and retrieval
- Background processing via task queue
- NLP-based summary generation
- Status tracking and summary retrieval

## Tech Stack

- Backend: Python (FastAPI or Flask) or Node.js (Express)
- Queue: Redis / RabbitMQ / Celery
- File Storage: AWS S3 / local storage
- NLP: spaCy / OpenAI / Transformers
- Deployment: Docker + AWS EC2

## Setup Instructions

```bash
git clone https://github.com/yourusername/document-summarizer.git
cd document-summarizer
cp .env.example .env
docker-compose up --build
