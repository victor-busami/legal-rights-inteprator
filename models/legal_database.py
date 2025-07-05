import json
import os
from typing import List, Dict

# Simulated legal database
LEGAL_DATABASE = {
    "Labor Law": {
        "statutes": [
            {
                "title": "Title VII of the Civil Rights Act of 1964",
                "description": "Prohibits employment discrimination based on race, color, religion, sex, or national origin",
                "section": "42 U.S.C. § 2000e",
                "relevance_score": 0.95
            },
            {
                "title": "Fair Labor Standards Act (FLSA)",
                "description": "Establishes minimum wage, overtime pay, and child labor standards",
                "section": "29 U.S.C. § 201",
                "relevance_score": 0.90
            },
            {
                "title": "Americans with Disabilities Act (ADA)",
                "description": "Prohibits discrimination against individuals with disabilities in employment",
                "section": "42 U.S.C. § 12101",
                "relevance_score": 0.85
            }
        ],
        "cases": [
            {
                "title": "Griggs v. Duke Power Co.",
                "year": 1971,
                "description": "Established disparate impact theory in employment discrimination",
                "citation": "401 U.S. 424"
            },
            {
                "title": "Meritor Savings Bank v. Vinson",
                "year": 1986,
                "description": "Recognized hostile work environment as form of sexual harassment",
                "citation": "477 U.S. 57"
            }
        ]
    },
    "Criminal Law": {
        "statutes": [
            {
                "title": "Fourth Amendment",
                "description": "Protects against unreasonable searches and seizures",
                "section": "U.S. Constitution",
                "relevance_score": 0.95
            },
            {
                "title": "Fifth Amendment",
                "description": "Right to remain silent and protection against self-incrimination",
                "section": "U.S. Constitution",
                "relevance_score": 0.90
            },
            {
                "title": "Sixth Amendment",
                "description": "Right to counsel and speedy trial",
                "section": "U.S. Constitution",
                "relevance_score": 0.90
            }
        ],
        "cases": [
            {
                "title": "Miranda v. Arizona",
                "year": 1966,
                "description": "Established Miranda rights for criminal suspects",
                "citation": "384 U.S. 436"
            },
            {
                "title": "Gideon v. Wainwright",
                "year": 1963,
                "description": "Established right to counsel for indigent defendants",
                "citation": "372 U.S. 335"
            }
        ]
    },
    "Civil Law": {
        "statutes": [
            {
                "title": "Federal Rules of Civil Procedure",
                "description": "Rules governing civil litigation in federal courts",
                "section": "28 U.S.C. App.",
                "relevance_score": 0.85
            },
            {
                "title": "Uniform Commercial Code",
                "description": "Governs commercial transactions and contracts",
                "section": "Various state adoptions",
                "relevance_score": 0.80
            }
        ],
        "cases": [
            {
                "title": "Palsgraf v. Long Island Railroad Co.",
                "year": 1928,
                "description": "Established proximate cause in negligence cases",
                "citation": "248 N.Y. 339"
            }
        ]
    },
    "Family Law": {
        "statutes": [
            {
                "title": "Uniform Child Custody Jurisdiction Act",
                "description": "Governs jurisdiction in child custody disputes",
                "section": "State adoptions",
                "relevance_score": 0.90
            },
            {
                "title": "Child Support Guidelines",
                "description": "Federal guidelines for child support calculations",
                "section": "45 C.F.R. § 302.56",
                "relevance_score": 0.85
            }
        ],
        "cases": [
            {
                "title": "Troxel v. Granville",
                "year": 2000,
                "description": "Established parental rights in custody disputes",
                "citation": "530 U.S. 57"
            }
        ]
    },
    "Property Law": {
        "statutes": [
            {
                "title": "Fair Housing Act",
                "description": "Prohibits discrimination in housing",
                "section": "42 U.S.C. § 3601",
                "relevance_score": 0.90
            },
            {
                "title": "Uniform Residential Landlord and Tenant Act",
                "description": "Model law for landlord-tenant relationships",
                "section": "State adoptions",
                "relevance_score": 0.85
            }
        ],
        "cases": [
            {
                "title": "Kelo v. City of New London",
                "year": 2005,
                "description": "Expanded eminent domain for economic development",
                "citation": "545 U.S. 469"
            }
        ]
    }
}

def search_legal_database(domain: str, query: str) -> Dict:
    """Search legal database for relevant information"""
    if domain not in LEGAL_DATABASE:
        return {"statutes": [], "cases": []}
    
    domain_data = LEGAL_DATABASE[domain]
    
    # Filter statutes by relevance to query
    relevant_statutes = []
    query_lower = query.lower()
    
    for statute in domain_data["statutes"]:
        # Simple keyword matching for relevance
        keywords = query_lower.split()
        statute_text = f"{statute['title']} {statute['description']}".lower()
        
        relevance_count = sum(1 for keyword in keywords if keyword in statute_text)
        if relevance_count > 0:
            relevant_statutes.append(statute)
    
    # Sort by relevance score
    relevant_statutes.sort(key=lambda x: x.get('relevance_score', 0), reverse=True)
    
    return {
        "statutes": relevant_statutes[:3],  # Top 3 most relevant
        "cases": domain_data["cases"][:2]  # Top 2 cases
    }

def get_legal_forms(domain: str) -> List[Dict]:
    """Get relevant legal forms for the domain"""
    forms_database = {
        "Labor Law": [
            {"name": "EEOC Charge Form", "description": "Employment discrimination complaint"},
            {"name": "Wage Claim Form", "description": "Unpaid wages complaint"},
            {"name": "OSHA Complaint Form", "description": "Workplace safety violation"}
        ],
        "Criminal Law": [
            {"name": "Motion to Suppress", "description": "Challenge evidence admissibility"},
            {"name": "Bail Application", "description": "Request for bail"},
            {"name": "Plea Agreement", "description": "Guilty plea terms"}
        ],
        "Civil Law": [
            {"name": "Complaint Form", "description": "File a lawsuit"},
            {"name": "Motion for Summary Judgment", "description": "Request judgment without trial"},
            {"name": "Discovery Request", "description": "Request evidence from opposing party"}
        ],
        "Family Law": [
            {"name": "Divorce Petition", "description": "File for divorce"},
            {"name": "Custody Agreement", "description": "Child custody arrangement"},
            {"name": "Child Support Modification", "description": "Modify child support"}
        ],
        "Property Law": [
            {"name": "Eviction Notice", "description": "Notice to vacate property"},
            {"name": "Lease Agreement", "description": "Rental property contract"},
            {"name": "Property Damage Claim", "description": "Claim for property damage"}
        ]
    }
    
    return forms_database.get(domain, [])

def get_legal_resources(domain: str) -> List[Dict]:
    """Get additional legal resources for the domain"""
    resources = {
        "Labor Law": [
            {"name": "Department of Labor", "url": "https://www.dol.gov/", "description": "Federal labor law information"},
            {"name": "Equal Employment Opportunity Commission", "url": "https://www.eeoc.gov/", "description": "Employment discrimination resources"},
            {"name": "National Labor Relations Board", "url": "https://www.nlrb.gov/", "description": "Union and collective bargaining information"}
        ],
        "Criminal Law": [
            {"name": "Public Defender Services", "url": "https://www.justice.gov/defender", "description": "Free legal representation"},
            {"name": "Bail Bond Information", "url": "#", "description": "Information about bail and bonds"},
            {"name": "Court System Resources", "url": "#", "description": "Court procedures and forms"}
        ],
        "Civil Law": [
            {"name": "Legal Aid Organizations", "url": "#", "description": "Free legal services for low-income individuals"},
            {"name": "Small Claims Court", "url": "#", "description": "Information about small claims procedures"},
            {"name": "Alternative Dispute Resolution", "url": "#", "description": "Mediation and arbitration services"}
        ]
    }
    
    return resources.get(domain, []) 