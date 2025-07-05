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
    """Classify legal text into domains using enhanced keyword-based approach"""
    
    # Enhanced legal domain keywords and patterns
    domain_keywords = {
        "Labor Law": [
            "employment", "work", "job", "fired", "terminated", "laid off", "employer", "employee", 
            "boss", "manager", "wage", "salary", "pay", "overtime", "discrimination", "harassment", 
            "workplace", "union", "contract", "performance review", "promotion", "demotion", 
            "hostile work environment", "retaliation", "whistleblower", "workers compensation", 
            "unemployment", "severance", "notice period", "at-will employment", "wrongful termination"
        ],
        "Criminal Law": [
            "arrest", "arrested", "police", "crime", "criminal", "charges", "bail", "trial", 
            "conviction", "sentence", "prison", "jail", "probation", "parole", "guilty", "innocent", 
            "defendant", "prosecutor", "district attorney", "public defender", "plea bargain", 
            "misdemeanor", "felony", "indictment", "arraignment", "preliminary hearing", 
            "grand jury", "search warrant", "miranda rights", "right to counsel", "due process"
        ],
        "Civil Law": [
            "contract", "agreement", "breach", "damages", "compensation", "liability", "negligence", 
            "tort", "lawsuit", "settlement", "plaintiff", "defendant", "court", "judge", "jury", 
            "evidence", "testimony", "deposition", "discovery", "motion", "appeal", "verdict", 
            "judgment", "injunction", "specific performance", "restitution", "punitive damages"
        ],
        "Family Law": [
            "divorce", "divorced", "custody", "child support", "alimony", "spousal support", 
            "marriage", "adoption", "prenuptial", "prenup", "visitation", "guardianship", 
            "spouse", "ex-spouse", "children", "parenting", "paternity", "maternity", 
            "domestic violence", "restraining order", "protective order", "marital property", 
            "community property", "separation", "annulment", "paternity test", "adoption"
        ],
        "Property Law": [
            "real estate", "property", "landlord", "tenant", "lease", "rent", "eviction", 
            "evicted", "ownership", "title", "deed", "mortgage", "house", "apartment", "rental", 
            "security deposit", "rent increase", "maintenance", "repairs", "habitability", 
            "quiet enjoyment", "sublease", "assignment", "rent control", "housing discrimination", 
            "fair housing", "zoning", "easement", "adverse possession", "eminent domain"
        ]
    }
    
    text_lower = text.lower()
    
    # Calculate domain scores based on keyword frequency and context
    domain_scores = {}
    for domain, keywords in domain_keywords.items():
        score = 0
        for keyword in keywords:
            if keyword in text_lower:
                # Give higher weight to more specific terms
                if keyword in ["arrested", "fired", "divorce", "eviction"]:
                    score += 3
                elif keyword in ["discrimination", "harassment", "custody", "landlord"]:
                    score += 2
                else:
                    score += 1
        domain_scores[domain] = score
    
    # Return the domain with highest score
    if max(domain_scores.values()) > 0:
        return max(domain_scores, key=domain_scores.get)
    else:
        return "General Law"

def detect_specific_situation(text):
    """Detect specific legal situations within the text"""
    text_lower = text.lower()
    situations = []
    
    # Criminal situations
    if any(word in text_lower for word in ["arrested", "arrest"]):
        situations.append("arrest")
    if any(word in text_lower for word in ["charged", "criminal charges"]):
        situations.append("criminal_charges")
    
    # Employment situations
    if any(word in text_lower for word in ["fired", "terminated", "laid off"]):
        situations.append("wrongful_termination")
    if any(word in text_lower for word in ["discrimination", "discriminated"]):
        situations.append("workplace_discrimination")
    if any(word in text_lower for word in ["harassment", "harassed"]):
        situations.append("workplace_harassment")
    
    # Family situations
    if any(word in text_lower for word in ["divorce", "divorced"]):
        situations.append("divorce")
    if any(word in text_lower for word in ["custody", "child custody"]):
        situations.append("child_custody")
    
    # Property situations
    if any(word in text_lower for word in ["eviction", "evicted"]):
        situations.append("eviction")
    if any(word in text_lower for word in ["landlord", "rent dispute"]):
        situations.append("landlord_tenant_dispute")
    
    return situations 