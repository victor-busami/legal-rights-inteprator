# models/qa.py

from typing import Dict, List

def answer_question(text: str, domain: str) -> str:
    """Generate legal interpretation using knowledge base with actionable advice"""
    
    # Legal knowledge base for different domains with actionable steps
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
            ],
            "situations": {
                "fired": {
                    "title": "Wrongful Termination",
                    "immediate_actions": [
                        "1. Request a written termination letter explaining the reason",
                        "2. Collect all relevant documents (pay stubs, performance reviews, emails)",
                        "3. Contact your state's Department of Labor",
                        "4. Consider filing for unemployment benefits",
                        "5. Consult with an employment attorney"
                    ],
                    "legal_options": [
                        "File a complaint with the EEOC if discrimination is suspected",
                        "File a wage claim if final pay is withheld",
                        "Consider wrongful termination lawsuit if you have evidence",
                        "Apply for unemployment benefits immediately"
                    ],
                    "resources": [
                        "Equal Employment Opportunity Commission (EEOC)",
                        "State Department of Labor",
                        "Local legal aid organizations",
                        "Employment law attorneys"
                    ]
                },
                "discrimination": {
                    "title": "Workplace Discrimination",
                    "immediate_actions": [
                        "1. Document all incidents with dates, times, and witnesses",
                        "2. Report to HR in writing and keep copies",
                        "3. Contact the EEOC within 180 days",
                        "4. Consult with an employment attorney",
                        "5. Consider filing a formal complaint"
                    ],
                    "legal_options": [
                        "File EEOC complaint for federal protection",
                        "File with state anti-discrimination agency",
                        "Consider private lawsuit after EEOC process",
                        "Seek injunctive relief to stop discrimination"
                    ],
                    "resources": [
                        "EEOC - Equal Employment Opportunity Commission",
                        "State civil rights agencies",
                        "Employment discrimination attorneys",
                        "Workplace rights organizations"
                    ]
                },
                "harassment": {
                    "title": "Workplace Harassment",
                    "immediate_actions": [
                        "1. Tell the harasser to stop (if safe to do so)",
                        "2. Report to supervisor and HR in writing",
                        "3. Document all incidents with details",
                        "4. Contact the EEOC or state agency",
                        "5. Consider legal action if employer doesn't act"
                    ],
                    "legal_options": [
                        "File harassment complaint with EEOC",
                        "File with state employment agency",
                        "Consider private lawsuit for damages",
                        "Seek restraining order if necessary"
                    ],
                    "resources": [
                        "EEOC Harassment Information",
                        "State employment agencies",
                        "Workplace harassment attorneys",
                        "Employee rights organizations"
                    ]
                }
            }
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
            ],
            "situations": {
                "arrested": {
                    "title": "If You Are Arrested",
                    "immediate_actions": [
                        "1. Stay calm and do not resist arrest",
                        "2. Exercise your right to remain silent",
                        "3. Ask for a lawyer immediately",
                        "4. Do not answer questions without legal counsel",
                        "5. Remember: 'I want to speak to my lawyer'",
                        "6. Do not consent to searches without a warrant"
                    ],
                    "legal_options": [
                        "Request a public defender if you cannot afford an attorney",
                        "File a motion to suppress if rights were violated",
                        "Consider plea bargain negotiations",
                        "Prepare for trial if pleading not guilty",
                        "Appeal conviction if found guilty"
                    ],
                    "resources": [
                        "Public Defender Services",
                        "Local criminal defense attorneys",
                        "Bail bond services",
                        "Legal aid organizations"
                    ]
                },
                "charged": {
                    "title": "If You Are Charged with a Crime",
                    "immediate_actions": [
                        "1. Contact a criminal defense attorney immediately",
                        "2. Do not discuss the case with anyone except your lawyer",
                        "3. Gather all relevant documents and evidence",
                        "4. Attend all court hearings",
                        "5. Follow your attorney's advice"
                    ],
                    "legal_options": [
                        "File pre-trial motions to dismiss or suppress evidence",
                        "Negotiate plea agreement if appropriate",
                        "Prepare for trial defense",
                        "Consider alternative sentencing programs"
                    ],
                    "resources": [
                        "Criminal defense attorneys",
                        "Public defender office",
                        "Legal aid organizations",
                        "Court-appointed counsel"
                    ]
                }
            }
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
            ],
            "situations": {
                "contract_dispute": {
                    "title": "Contract Dispute",
                    "immediate_actions": [
                        "1. Review the contract terms carefully",
                        "2. Document all communications with the other party",
                        "3. Send a demand letter outlining your position",
                        "4. Consider mediation or arbitration",
                        "5. Consult with a contract attorney"
                    ],
                    "legal_options": [
                        "File breach of contract lawsuit",
                        "Seek specific performance",
                        "Request damages for breach",
                        "Consider alternative dispute resolution"
                    ],
                    "resources": [
                        "Contract law attorneys",
                        "Mediation services",
                        "Small claims court",
                        "Legal aid organizations"
                    ]
                },
                "personal_injury": {
                    "title": "Personal Injury",
                    "immediate_actions": [
                        "1. Seek medical attention immediately",
                        "2. Document the accident scene and injuries",
                        "3. Collect witness statements and contact information",
                        "4. Report to relevant authorities",
                        "5. Contact a personal injury attorney"
                    ],
                    "legal_options": [
                        "File personal injury lawsuit",
                        "Negotiate settlement with insurance",
                        "Seek compensation for medical expenses",
                        "Request damages for pain and suffering"
                    ],
                    "resources": [
                        "Personal injury attorneys",
                        "Medical malpractice lawyers",
                        "Insurance claim specialists",
                        "Accident reconstruction experts"
                    ]
                }
            }
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
            ],
            "situations": {
                "divorce": {
                    "title": "Filing for Divorce",
                    "immediate_actions": [
                        "1. Consult with a family law attorney",
                        "2. Gather financial documents (bank statements, tax returns)",
                        "3. Document marital assets and debts",
                        "4. Consider mediation for uncontested divorce",
                        "5. File divorce petition in appropriate court"
                    ],
                    "legal_options": [
                        "File for uncontested divorce if both parties agree",
                        "File for contested divorce if disputes exist",
                        "Seek temporary orders for support/custody",
                        "Request property division and spousal support"
                    ],
                    "resources": [
                        "Family law attorneys",
                        "Divorce mediators",
                        "Financial advisors",
                        "Child custody evaluators"
                    ]
                },
                "custody": {
                    "title": "Child Custody Dispute",
                    "immediate_actions": [
                        "1. Document your involvement in child's life",
                        "2. Keep records of all child-related expenses",
                        "3. Consider mediation to resolve disputes",
                        "4. File for custody modification if needed",
                        "5. Consult with family law attorney"
                    ],
                    "legal_options": [
                        "File for joint or sole custody",
                        "Request visitation schedule modification",
                        "Seek child support modification",
                        "File for emergency custody if necessary"
                    ],
                    "resources": [
                        "Family law attorneys",
                        "Child custody mediators",
                        "Parenting coordinators",
                        "Child support enforcement agencies"
                    ]
                }
            }
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
            ],
            "situations": {
                "eviction": {
                    "title": "Facing Eviction",
                    "immediate_actions": [
                        "1. Review your lease agreement carefully",
                        "2. Check if eviction notice is legally valid",
                        "3. Contact legal aid or tenant rights organization",
                        "4. Consider negotiating with landlord",
                        "5. File answer to eviction lawsuit if served"
                    ],
                    "legal_options": [
                        "File motion to dismiss if notice is defective",
                        "Request rent abatement for uninhabitable conditions",
                        "Counter-sue for landlord violations",
                        "Request emergency stay of eviction"
                    ],
                    "resources": [
                        "Tenant rights organizations",
                        "Legal aid housing attorneys",
                        "Local housing authorities",
                        "Tenant advocacy groups"
                    ]
                },
                "landlord_dispute": {
                    "title": "Landlord-Tenant Dispute",
                    "immediate_actions": [
                        "1. Document all communications with landlord",
                        "2. Take photos of any property issues",
                        "3. Send written notice of problems",
                        "4. Contact local housing authority",
                        "5. Consider legal action if necessary"
                    ],
                    "legal_options": [
                        "File complaint with housing authority",
                        "Sue for return of security deposit",
                        "Request rent abatement for repairs",
                        "File for emergency repairs if needed"
                    ],
                    "resources": [
                        "Housing authority",
                        "Tenant rights attorneys",
                        "Local tenant organizations",
                        "Building code enforcement"
                    ]
                }
            }
        }
    }
    
    # Get domain-specific knowledge
    domain_knowledge = legal_knowledge.get(domain, legal_knowledge["Civil Law"])
    
    # Generate contextual response based on the input text
    response = generate_actionable_advice(text, domain_knowledge, domain)
    
    return response

def generate_actionable_advice(text: str, knowledge: Dict, domain: str) -> str:
    """Generate actionable legal advice based on specific situations"""
    
    # Analyze the input text for key issues
    text_lower = text.lower()
    
    # Identify specific legal situations
    situations = {}
    
    # Labor Law situations
    if any(word in text_lower for word in ["fired", "terminated", "laid off"]):
        situations["fired"] = knowledge["situations"]["fired"]
    if any(word in text_lower for word in ["discrimination", "harassment"]):
        situations["discrimination"] = knowledge["situations"]["discrimination"]
    if any(word in text_lower for word in ["harassment", "harassed"]):
        situations["harassment"] = knowledge["situations"]["harassment"]
    
    # Criminal Law situations
    if any(word in text_lower for word in ["arrested", "arrest"]):
        situations["arrested"] = knowledge["situations"]["arrested"]
    if any(word in text_lower for word in ["charged", "criminal", "crime"]):
        situations["charged"] = knowledge["situations"]["charged"]
    
    # Family Law situations
    if any(word in text_lower for word in ["divorce", "divorced"]):
        situations["divorce"] = knowledge["situations"]["divorce"]
    if any(word in text_lower for word in ["custody", "child", "children"]):
        situations["custody"] = knowledge["situations"]["custody"]
    
    # Property Law situations
    if any(word in text_lower for word in ["eviction", "evicted"]):
        situations["eviction"] = knowledge["situations"]["eviction"]
    if any(word in text_lower for word in ["landlord", "rent", "lease"]):
        situations["landlord_dispute"] = knowledge["situations"]["landlord_dispute"]
    
    # Generate comprehensive response
    response_parts = []
    response_parts.append(f"Based on your situation involving {domain.lower()}, here's what you need to know:")
    
    # Add general rights
    response_parts.append(f"\n📋 YOUR LEGAL RIGHTS:")
    for right in knowledge["rights"][:4]:
        response_parts.append(f"• {right}")
    
    # Add specific situation advice
    if situations:
        for situation_key, situation_data in situations.items():
            response_parts.append(f"\n🚨 IMMEDIATE ACTIONS - {situation_data['title']}:")
            for action in situation_data["immediate_actions"]:
                response_parts.append(action)
            
            response_parts.append(f"\n⚖️ LEGAL OPTIONS:")
            for option in situation_data["legal_options"]:
                response_parts.append(f"• {option}")
            
            response_parts.append(f"\n📞 HELPFUL RESOURCES:")
            for resource in situation_data["resources"]:
                response_parts.append(f"• {resource}")
    
    response_parts.append(f"\n⚠️ IMPORTANT: This information is for guidance only. Please consult with a qualified attorney for specific legal advice tailored to your situation.")
    
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