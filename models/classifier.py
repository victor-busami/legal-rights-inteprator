# models/classifier.py

from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch

# Initialize the classifier pipeline
classifier = None
tokenizer = None
model = None

def initialize_classifier():
    global classifier, tokenizer, model
    try:
        # Use a pre-trained model for text classification
        model_name = "microsoft/DialoGPT-medium"  # We'll use this as base and fine-tune for legal domains
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=5)
        
        # Define legal domains
        legal_domains = ["Labor Law", "Criminal Law", "Civil Law", "Family Law", "Property Law"]
        
        # Create a simple classifier based on keywords and patterns
        classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
    except Exception as e:
        print(f"Error initializing classifier: {e}")
        # Fallback to rule-based classification
        classifier = None

def classify(text):
    """Classify legal text into domains using keyword-based approach"""
    
    # Legal domain keywords and patterns
    domain_keywords = {
        "Labor Law": ["employment", "work", "job", "fired", "terminated", "wage", "salary", "overtime", "discrimination", "harassment", "workplace", "union", "contract", "employer", "employee", "boss", "manager"],
        "Criminal Law": ["arrest", "police", "crime", "criminal", "charges", "bail", "trial", "conviction", "sentence", "prison", "jail", "probation", "parole", "guilty", "innocent", "defendant", "prosecutor"],
        "Civil Law": ["contract", "agreement", "breach", "damages", "compensation", "liability", "negligence", "tort", "lawsuit", "settlement", "plaintiff", "defendant", "court", "judge"],
        "Family Law": ["divorce", "custody", "child support", "alimony", "marriage", "adoption", "prenuptial", "visitation", "guardianship", "spouse", "ex-spouse", "children", "parenting"],
        "Property Law": ["real estate", "property", "landlord", "tenant", "lease", "rent", "eviction", "ownership", "title", "deed", "mortgage", "house", "apartment", "rental"]
    }
    
    text_lower = text.lower()
    
    # Calculate domain scores based on keyword frequency
    domain_scores = {}
    for domain, keywords in domain_keywords.items():
        score = sum(1 for keyword in keywords if keyword in text_lower)
        domain_scores[domain] = score
    
    # Return the domain with highest score
    if max(domain_scores.values()) > 0:
        return max(domain_scores, key=domain_scores.get)
    else:
        return "General Law" 