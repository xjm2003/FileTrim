# FileTrim

FileTrim is a Python library for content-aware file renaming and organization.

## Overview

FileTrim helps users rename files based on extracted content rather than only filenames or extensions.  
The project is designed as a Python library with a thin CLI wrapper, so the core business logic remains modular, testable, and reusable.

Our MVP focuses on:
- detecting supported file types
- extracting text from files
- processing extracted content
- generating safe, readable filenames
- previewing rename results with a dry-run mode

## Motivation

Many downloaded or scanned files have vague names such as:
- `scan001.pdf`
- `document(3).docx`
- `IMG_4821.jpg`

This makes local file organization difficult. FileTrim aims to improve this by using file content to propose more meaningful filenames.

## Project Goals

- Build a reusable Python package for content-aware file renaming
- Separate core logic from the command-line interface
- Follow good software engineering practices
- Provide automated tests and documentation
- Support safe usage through preview before execution

## MVP Scope

Included in the MVP:
- file type detection
- text extraction for:
  - `.txt`
  - `.md`
  - `.pdf` with text layer
  - `.docx`
- text cleaning
- simple signal extraction:
  - title
  - date
- rule-based document classification
- filename generation
- filename sanitization
- dry-run rename preview

Not included in the MVP:
- OCR for scanned PDFs or images
- real-time file watching
- GUI
- advanced machine learning or LLM-based naming

## Architecture

The project is organized into several layers:

### 1. Extraction layer
Responsible for identifying supported file types and extracting raw text from files.

Examples:
- text extractor
- PDF extractor
- DOCX extractor

### 2. Processing layer
Responsible for cleaning extracted text and extracting useful signals such as title and date.

Examples:
- text normalization
- title extraction
- date extraction
- rule-based document classification

### 3. Naming layer
Responsible for converting extracted signals into safe, readable filenames.

Examples:
- filename templates
- filename builder
- filename sanitizer
- conflict handling

### 4. Execution layer
Responsible for planning and performing rename operations.

Examples:
- dry-run mode
- actual rename execution
- integration with CLI

### 5. CLI wrapper
A thin command-line interface that calls the library without duplicating business logic.

## Repository Structure


```text
FileTrim/
├── README.md
├── pyproject.toml
├── src/
│   └── fileTrim/
│       ├── __init__.py
│       ├── cli.py
│       ├── models.py
│       ├── orchestrator.py
│       ├── file_types.py
│       ├── extractor/
│       ├── processing/
│       ├── naming/
│       └── execution/
├── tests/
└── .github/
    └── workflows/
```
## Current Issue 2 Status

The current filename-generation MVP includes:
- text normalization
- title extraction
- date extraction
- rule-based document classification
- filename template selection
- filename sanitization

Example input text:

```text
BIOSTAT 821
Final Project
Due: April 24, 2026
```

Example output filename:
- 2026-04-24-assignment-final-project.pdf

Development

Run tests
- python -m pytest

Run linting and formatting
- python -m ruff check .
- python -m ruff format .