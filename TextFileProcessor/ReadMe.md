# Text File Processor with Ollama
A Python script that uses the Ollama llama3.2 model to process a text file (Cars.txt) containing car details, extracting make, model, year, and price.
formatting them into a bulleted list categorized by car make.

## Features
Reads car details from a text file.
Uses Ollama's llama3.2 model to extract and structure data.
Outputs car details in a bulleted format, grouped by make.
Includes error handling for missing files and model responses.

## Requirements
Python 3.x
Ollama library: pip install ollama
Ollama llama3.2 model: ollama pull llama3.2
Input file (Cars.txt) with car details.

## Notes
Ensure the Ollama service is running and the model is installed.
Modify the prompt for custom output formats.
Handles missing files and empty model responses.
