# models/ner.py

import re
from typing import List, Dict

def extract_entities(text: str) -> List[Dict]:
    """Extract legal entities using pattern matching"""
    entities = []
    
    # Legal-specific entity patterns
    legal_patterns = {
        "PERSON": r"\b[A-Z][a-z]+ [A-Z][a-z]+\b",  # Names
        "ORGANIZATION": r"\b[A-Z][a-zA-Z\s&]+(?:Corp|Inc|LLC|Ltd|Company|Law Firm|Court)\b",
        "DATE": r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b|\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}\b",
        "MONEY": r"\$\d+(?:,\d{3})*(?:\.\d{2})?|\d+(?:,\d{3})*(?:\.\d{2})?\s*(?:dollars|USD)",
        "LAW_REFERENCE": r"\b(?:Section|Article|Chapter|Title)\s+\d+[A-Z]?\b",
        "COURT": r"\b(?:Supreme Court|District Court|Circuit Court|Appeals Court|Federal Court)\b",
        "CASE_NUMBER": r"\b(?:Case|Docket)\s+(?:No\.?|Number)\s+[A-Z0-9-]+\b"
    }
    
    # Extract legal-specific entities using regex patterns
    for label, pattern in legal_patterns.items():
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            entity_info = {
                "text": match.group(),
                "label": label,
                "start": match.start(),
                "end": match.end()
            }
            entities.append(entity_info)
    
    # Also extract common legal keywords
    legal_keywords = {
        "LEGAL_TERM": ["attorney", "lawyer", "judge", "plaintiff", "defendant", "witness", "evidence", "testimony", "verdict", "appeal", "motion", "hearing", "trial", "settlement", "damages", "compensation", "liability", "negligence"]
    }
    
    text_lower = text.lower()
    for label, keywords in legal_keywords.items():
        for keyword in keywords:
            if keyword in text_lower:
                # Find the actual text in the original case
                pattern = re.compile(re.escape(keyword), re.IGNORECASE)
                for match in pattern.finditer(text):
                    entity_info = {
                        "text": match.group(),
                        "label": label,
                        "start": match.start(),
                        "end": match.end()
                    }
                    entities.append(entity_info)
    
    # Remove duplicates and sort by position
    unique_entities = []
    seen = set()
    for entity in sorted(entities, key=lambda x: x["start"]):
        entity_key = (entity["text"], entity["start"], entity["end"])
        if entity_key not in seen:
            seen.add(entity_key)
            unique_entities.append(entity)
    
    return unique_entities

def get_entity_texts(entities: List[Dict]) -> List[str]:
    """Extract just the text of entities for display"""
    return [entity["text"] for entity in entities] 