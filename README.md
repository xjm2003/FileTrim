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
- executing real file renames safely

## Motivation

Many downloaded or scanned files have vague names such as:
- `scan001.pdf`
- `document(3).docx`
- `IMG_4821.jpg`

This makes local file organization difficult. FileTrim improves this by using file content to propose more meaningful filenames.

## Project Goals

- Build a reusable Python package for content-aware file renaming
- Separate core logic from the command-line interface
- Follow good software engineering practices
- Provide automated tests and documentation
- Support safe usage through preview before execution

## MVP Scope

### Included in the MVP
- file type detection
- text extraction for:
  - `.txt`
  - `.md`
  - `.pdf` with text layer
  - `.docx`
- text cleaning
- rule-based document classification
- filename generation
- filename sanitization
- dry-run rename preview
- actual rename execution
- conflict-safe rename behavior

### Not included in the MVP
- OCR for scanned PDFs or images
- real-time file watching
- GUI
- advanced machine learning or LLM-based naming

## Architecture

The project is organized into several layers.

### 1. Extraction layer
Responsible for identifying supported file types and extracting raw text from files.

Examples:
- text extractor
- PDF extractor
- DOCX extractor

### 2. Processing layer
Responsible for cleaning extracted text and classifying document content.

Examples:
- text normalization
- rule-based document classification

### 3. Naming layer
Responsible for converting extracted content into safe, readable filenames.

Examples:
- filename builder
- filename sanitizer

### 4. Execution layer
Responsible for planning and performing rename operations.

Examples:
- dry-run mode
- actual rename execution
- conflict handling

### 5. CLI wrapper
A thin command-line interface that calls the library without duplicating business logic.

## Repository Structure

```text
FileTrim/
├── README.md
├── pyproject.toml
├── src/
│   └── filetrim/
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

## Example Workflow

A typical pipeline looks like this:

1. detect file type
2. extract text
3. clean text
4. classify document content
5. build a candidate filename
6. sanitize the filename
7. preview or execute rename

Example:

Input file: `sample.txt`

Input content:

```text
BIOSTAT 821
Final Project
Due: April 24, 2026
```

Possible output:

```text
2026-04-24-assignment-biostat-821.txt
```

## Installation

Clone the repository and install in editable mode:

```bash
pip install -e .[dev]
```

## Usage

Dry-run preview:

```bash
filetrim path/to/file.txt --dry-run
```

Actual rename:

```bash
filetrim path/to/file.txt --execute
```

Example:

```bash
filetrim sample.txt --dry-run
filetrim sample.txt --execute
```

## Testing

Run all tests with:

```bash
pytest
```

Run style checks with:

```bash
ruff check .
```

## Verification

The project has been validated in three ways:
- unit and integration tests pass with `pytest`
- style checks pass with `ruff check .`
- the CLI has been manually tested for:
  - dry-run preview
  - actual rename execution

## Development Workflow

We use the following workflow:
- create an issue for each task
- create a feature branch for each issue
- open a pull request before merging to `main`
- add tests for implemented functionality
- use CI to run checks automatically

## Team

- Member 1 — file type detection and content extraction
- Member 2 — text processing, classification, and filename generation
- Member 3 — execution pipeline, CLI, integration, and final submission

## Generative AI Usage

Generative AI tools were used during this project and documented below.

### Tools used
- ChatGPT

### How we used them
- brainstorming project ideas
- refining project scope
- drafting README text
- suggesting software architecture
- helping debug and refine Python code
- suggesting test cases and CI configuration

### What they produced
- draft project descriptions
- draft issue text
- draft code suggestions for execution pipeline and CLI
- draft unit and integration test examples

All AI-generated content was reviewed, edited, and validated by the team before inclusion in the final repository.

## Submission

This repository is submitted as the final project for BIOSTAT 821.

The repository includes:
- project plan
- implementation code
- tests
- CI configuration
- documentation
- GitHub issues and pull requests