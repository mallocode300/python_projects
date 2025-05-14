#!/usr/bin/env python3

import argparse
import os
from pypdf import PdfReader
from gtts import gTTS
import pyttsx3

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    try:
        pdf_reader = PdfReader(pdf_path)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None

def text_to_speech_online(text, output_path="output.mp3", language="en"):
    """Convert text to speech using Google's TTS API (requires internet)."""
    try:
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(output_path)
        print(f"Audio saved to {output_path}")
        return True
    except Exception as e:
        print(f"Error in online TTS conversion: {e}")
        return False

def text_to_speech_offline(text, output_path="output.mp3"):
    """Convert text to speech using offline TTS engine."""
    try:
        engine = pyttsx3.init()
        
        # Save to file
        engine.save_to_file(text, output_path)
        engine.runAndWait()
        print(f"Audio saved to {output_path}")
        return True
    except Exception as e:
        print(f"Error in offline TTS conversion: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Convert PDF to speech")
    parser.add_argument("pdf_file", help="Path to the PDF file")
    parser.add_argument("-o", "--output", default="output.mp3", help="Output audio file path")
    parser.add_argument("-l", "--language", default="en", help="Language code for TTS (online only)")
    parser.add_argument("--offline", action="store_true", help="Use offline TTS engine")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.pdf_file):
        print(f"Error: PDF file '{args.pdf_file}' not found")
        return
    
    print(f"Extracting text from {args.pdf_file}...")
    text = extract_text_from_pdf(args.pdf_file)
    
    if not text:
        print("No text extracted. Exiting.")
        return
    
    print(f"Converting text to speech...")
    
    if args.offline:
        success = text_to_speech_offline(text, args.output)
    else:
        success = text_to_speech_online(text, args.output, args.language)
        
    if success:
        print("Conversion complete!")
    else:
        print("Conversion failed.")

if __name__ == "__main__":
    main() 