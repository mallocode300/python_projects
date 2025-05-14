# PDF to Speech Converter

A simple Python script that extracts text from PDF files and converts it to speech.

## Features

- Extract text from PDF documents
- Convert text to speech using Google's Text-to-Speech API (requires internet)
- Alternatively use offline text-to-speech with pyttsx3
- Customize output audio file name and language

## Requirements

- Python 3.6+
- Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Basic usage:

```bash
python pdf_to_speech.py your_pdf_file.pdf
```

Options:

```bash
python pdf_to_speech.py your_pdf_file.pdf -o output_filename.mp3 -l en
```

Use offline TTS engine:

```bash
python pdf_to_speech.py your_pdf_file.pdf --offline
```

## Arguments

- `pdf_file`: Path to the PDF file (required)
- `-o, --output`: Output audio file path (default: "output.mp3")
- `-l, --language`: Language code for TTS (online only, default: "en")
- `--offline`: Use offline TTS engine instead of Google's online service 