# Multi-Agent Document Classification & Routing System

## Overview
This project implements a multi-agent AI system that accepts PDF, JSON, or Email inputs, classifies their format and intent (Invoice, RFQ, Complaint, Regulation), routes to the correct agent, extracts relevant info, and stores it in shared memory (SQLite).

## Features
- Format classification: PDF, JSON, Email
- Intent detection: Invoice, RFQ, Complaint, Regulation (via OpenAI GPT-3.5)
- JSON agent: Extracts and validates structured data
- Email agent: Extracts sender, urgency, and intent from email text
- PDF agent: Extracts and summarizes PDF text
- Shared SQLite memory accessible across agents
- Streamlit UI for file uploads and results display

## Setup Instructions

### Prerequisites
- Python 3.8+
- OpenAI API Key

### Install dependencies
```bash
pip install -r requirements.txt
```

### Set your OpenAI API Key
Linux/macOS:
```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```
Windows PowerShell:
```powershell
$env:OPENAI_API_KEY="your_openai_api_key_here"
```

### Run the Streamlit app
```bash
streamlit run app.py
```

## Folder Structure
```
Flowbit_assignment/
├── agents/
├── memory/
├── samples/
├── app.py
├── requirements.txt
└── README.md
```

## Sample Inputs
- `samples/sample_invoice.json` – Sample JSON invoice document
- `samples/sample_complaint_email.txt` – Sample complaint email text
- `samples/sample_regulation.pdf` – Sample regulation PDF

## Sample Outputs
- Extracted data and detected intents are saved in SQLite `memory.db`
- Logs are printed in the Streamlit UI and console
