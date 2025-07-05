# models/qa.py

from typing import Dict, List

def answer_question(text: str, domain: str) -> str:
    """Generate legal interpretation using knowledge base"""
    
    # Legal knowledge base for different domains
    legal_knowledge = {
        "Labor Law": {
            "context": """
            Employment law covers various aspects of the employer-employee relationship. 
            Key rights include: protection against discrimination, right to fair wages, 
            workplace safety, and protection from wrongful termination. 
            Employees have the right to form unions and engage in collective bargaining.
            """,
            "rights": [
                "Right to minimum wage and overtime pay",
                "Protection against discrimination based on race, gender, age, disability",
                "Right to a safe workplace",
                "Protection from retaliation for reporting violations",
                "Right to family and medical leave (FMLA)",
                "Right to workers' compensation for workplace injuries"
            ]
        },
        "Criminal Law": {
            "context": """
            Criminal law deals with offenses against the state or society. 
            Defendants have constitutional rights including due process, 
            right to counsel, right to remain silent, and protection from double jeopardy.
            """,
            "rights": [
                "Right to remain silent (Fifth Amendment)",
                "Right to legal counsel (Sixth Amendment)",
                "Right to a speedy and public trial",
                "Protection from unreasonable searches and seizures",
                "Right to confront witnesses",
                "Protection from cruel and unusual punishment"
            ]
        },
        "Civil Law": {
            "context": """
            Civil law governs disputes between individuals or organizations. 
            It covers contracts, torts, property disputes, and personal injury cases.
            Parties have the right to sue for damages and seek legal remedies.
            """,
            "rights": [
                "Right to file a lawsuit",
                "Right to legal representation",
                "Right to discovery of evidence",
                "Right to a jury trial in certain cases",
                "Right to appeal decisions",
                "Right to seek damages and injunctive relief"
            ]
        },
        "Family Law": {
            "context": """
            Family law covers marriage, divorce, child custody, and domestic relations.
            The best interests of the child are paramount in custody decisions.
            """,
            "rights": [
                "Right to file for divorce",
                "Right to seek child custody and support",
                "Right to spousal support in appropriate cases",
                "Right to visitation with children",
                "Right to equitable division of marital property",
                "Right to protection from domestic violence"
            ]
        },
        "Property Law": {
            "context": """
            Property law governs ownership and use of real and personal property.
            It includes landlord-tenant law, real estate transactions, and property rights.
            """,
            "rights": [
                "Right to quiet enjoyment of property",
                "Right to fair housing without discrimination",
                "Right to proper notice before eviction",
                "Right to habitable living conditions",
                "Right to security deposit return",
                "Right to privacy in rental property"
            ]
        }
    }
    
    # Get domain-specific knowledge
    domain_knowledge = legal_knowledge.get(domain, legal_knowledge["Civil Law"])
    
    # Generate contextual response based on the input text
    response = generate_legal_interpretation(text, domain_knowledge, domain)
    
    return response

def generate_legal_interpretation(text: str, knowledge: Dict, domain: str) -> str:
    """Generate legal interpretation using the knowledge base"""
    
    # Analyze the input text for key issues
    text_lower = text.lower()
    
    # Identify specific legal issues mentioned
    issues = []
    if any(word in text_lower for word in ["fired", "terminated", "laid off"]):
        issues.append("wrongful termination")
    if any(word in text_lower for word in ["discrimination", "harassment"]):
        issues.append("workplace discrimination")
    if any(word in text_lower for word in ["wage", "salary", "pay"]):
        issues.append("wage and hour violations")
    if any(word in text_lower for word in ["arrest", "charged", "criminal"]):
        issues.append("criminal charges")
    if any(word in text_lower for word in ["eviction", "landlord", "rent"]):
        issues.append("tenant rights")
    if any(word in text_lower for word in ["divorce", "custody", "child"]):
        issues.append("family law matters")
    
    # Generate response
    response_parts = []
    response_parts.append(f"Based on your situation involving {domain.lower()}, here are your key rights:")
    
    # Add relevant rights
    for right in knowledge["rights"][:4]:  # Limit to 4 most relevant rights
        response_parts.append(f"• {right}")
    
    # Add specific advice based on identified issues
    if issues:
        response_parts.append(f"\nSpecific concerns identified: {', '.join(issues)}")
        response_parts.append("I recommend consulting with a qualified attorney in your jurisdiction for specific legal advice.")
    
    response_parts.append(f"\nNote: This interpretation is for informational purposes only and should not be considered legal advice.")
    
    return "\n".join(response_parts)

def get_legal_references(domain: str) -> List[str]:
    """Get relevant legal references for the domain"""
    references = {
        "Labor Law": [
            "Title VII of the Civil Rights Act of 1964",
            "Fair Labor Standards Act (FLSA)",
            "Americans with Disabilities Act (ADA)",
            "Family and Medical Leave Act (FMLA)"
        ],
        "Criminal Law": [
            "U.S. Constitution (Bill of Rights)",
            "Miranda v. Arizona (1966)",
            "Gideon v. Wainwright (1963)"
        ],
        "Civil Law": [
            "State civil procedure rules",
            "Contract law principles",
            "Tort law standards"
        ],
        "Family Law": [
            "State family law statutes",
            "Uniform Child Custody Jurisdiction Act",
            "Child Support Guidelines"
        ],
        "Property Law": [
            "Fair Housing Act",
            "State landlord-tenant laws",
            "Real estate transaction laws"
        ]
    }
    
    return references.get(domain, ["Consult local laws and regulations"]) 