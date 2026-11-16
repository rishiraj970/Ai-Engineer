
# AI Company Intelligence & Brochure Generator

An AI-powered application that analyzes company websites
and automatically generates professional sales brochures.

Users can enter a company website URL, select an LLM provider,
and generate a brochure through an interactive Gradio interface.

## Features

- Website content extraction
- AI-powered company analysis
- Structured company intelligence in JSON
- Automated marketing brochure generation
- Local LLM support using Ollama
- OpenAI API integration
- Streaming AI responses
- Downloadable Markdown brochures
- URL validation and error handling
- Automated tests using Pytest

## Architecture

Company Website
       |
       v
Website Reader
       |
       v
Company Analyzer
       |
       v
Structured Company Data (JSON)
       |
       v
Brochure Generator
       |
       v
Markdown Brochure

## Tech Stack

- Python 3.12
- Ollama
- Qwen 2.5 3B
- OpenAI Python SDK
- Gradio
- Requests
- BeautifulSoup
- Pytest
- UV

## Installation

### 1. Clone the repository

git clone https://github.com/rishiraj970/Ai-Engineer

cd ai-company-brochure

### 2. Install dependencies

uv sync

### 3. Download the local LLM

ollama pull qwen2.5:3b

Make sure Ollama is running.

### 4. Run the application

uv run gradio app.py

Open the local Gradio URL displayed in your terminal.

## AI Provider Configuration

The application supports:

### Ollama

Default local model:

qwen2.5:3b

Ollama runs locally and does not require an OpenAI API key.

### OpenAI

Set your API key in the OPENAI_API_KEY environment variable.

PowerShell example:

$env:OPENAI_API_KEY="your_api_key"

Never commit API keys to GitHub.

## Running Tests

uv run pytest -v

## Output

Generated brochures are saved in the outputs directory
as Markdown files.

## Future Improvements

- Retrieval-Augmented Generation (RAG)
- AI agent-based company research
- More robust website crawling
- Brochure PDF export
- LLM evaluation
- Cloud deployment

## Disclaimer

AI-generated company information may be incomplete or inaccurate.
Always verify important business claims against their original sources.
