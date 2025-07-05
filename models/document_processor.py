import PyPDF2
import docx
import os
from typing import Optional

def process_document(filepath: str) -> str:
    """Process uploaded documents and extract text content"""
    file_extension = filepath.split('.')[-1].lower()
    
    try:
        if file_extension == 'pdf':
            return extract_pdf_text(filepath)
        elif file_extension in ['docx', 'doc']:
            return extract_docx_text(filepath)
        elif file_extension == 'txt':
            return extract_txt_text(filepath)
        else:
            return "Unsupported file format"
    except Exception as e:
        return f"Error processing document: {str(e)}"

def extract_pdf_text(filepath: str) -> str:
    """Extract text from PDF files"""
    text = ""
    try:
        with open(filepath, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def extract_docx_text(filepath: str) -> str:
    """Extract text from DOCX files"""
    try:
        doc = docx.Document(filepath)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text.strip()
    except Exception as e:
        return f"Error reading DOCX: {str(e)}"

def extract_txt_text(filepath: str) -> str:
    """Extract text from TXT files"""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except Exception as e:
        return f"Error reading TXT: {str(e)}"

def clean_extracted_text(text: str) -> str:
    """Clean and format extracted text"""
    # Remove excessive whitespace
    text = ' '.join(text.split())
    
    # Remove common document artifacts
    text = text.replace('\x00', '')  # Remove null characters
    text = text.replace('\r', '\n')  # Normalize line endings
    
    return text.strip() 