import json
from typing import Dict, List, Optional
from datetime import datetime

class LegalChatbot:
    def __init__(self):
        self.conversation_history = {}
        self.user_context = {}
        
        # Predefined conversation flows
        self.conversation_flows = {
            "greeting": {
                "triggers": ["hello", "hi", "hey", "start", "begin"],
                "response": "Hello! I'm your AI Legal Assistant. I can help you understand your legal rights and provide guidance on various legal matters. What legal situation would you like to discuss today?",
                "suggestions": [
                    "I was arrested",
                    "I was fired from my job",
                    "My landlord is evicting me",
                    "I'm going through a divorce",
                    "I have a contract dispute"
                ]
            },
            "arrest": {
                "triggers": ["arrested", "arrest", "police", "charged", "criminal"],
                "response": "I understand you're dealing with a criminal law situation. This is serious and you have important rights. Let me help you understand what you should do.",
                "follow_up": "Can you tell me more about your situation? For example:\n- When were you arrested?\n- What were you charged with?\n- Do you have a lawyer?\n- Are you currently in custody?",
                "suggestions": [
                    "What are my rights when arrested?",
                    "How do I get a lawyer?",
                    "What should I say to the police?",
                    "How do I post bail?"
                ]
            },
            "employment": {
                "triggers": ["fired", "terminated", "laid off", "job", "work", "employment", "discrimination", "harassment"],
                "response": "I see you're dealing with an employment law issue. This can be stressful, but you have rights as an employee. Let me help you understand your situation.",
                "follow_up": "To better assist you, I need to know:\n- Why were you terminated?\n- Did you receive any written notice?\n- Were there any warning signs?\n- Do you have documentation?",
                "suggestions": [
                    "What are my rights when fired?",
                    "How do I file for unemployment?",
                    "Can I sue for wrongful termination?",
                    "What is workplace discrimination?"
                ]
            },
            "housing": {
                "triggers": ["eviction", "evicted", "landlord", "rent", "lease", "apartment", "house"],
                "response": "I understand you're facing a housing law issue. Tenant rights are important and there are legal protections in place. Let me help you understand your rights.",
                "follow_up": "To provide better guidance, please tell me:\n- What type of notice did you receive?\n- How long have you lived there?\n- Are you behind on rent?\n- Are there any habitability issues?",
                "suggestions": [
                    "What are my tenant rights?",
                    "How do I fight an eviction?",
                    "Can I withhold rent for repairs?",
                    "What is a security deposit dispute?"
                ]
            },
            "family": {
                "triggers": ["divorce", "custody", "child", "marriage", "spouse", "alimony"],
                "response": "I understand you're dealing with a family law matter. These situations can be emotionally challenging, but understanding your legal rights is important.",
                "follow_up": "To help you better, I need to know:\n- Are you married or in a domestic partnership?\n- Do you have children together?\n- Have you already filed for divorce?\n- Are there custody concerns?",
                "suggestions": [
                    "How do I file for divorce?",
                    "What are my custody rights?",
                    "How is child support calculated?",
                    "What is the divorce process?"
                ]
            },
            "contract": {
                "triggers": ["contract", "agreement", "breach", "lawsuit", "damages", "settlement"],
                "response": "I see you're dealing with a contract or civil law issue. Understanding your legal options is crucial in these situations.",
                "follow_up": "To provide specific guidance, please tell me:\n- What type of contract is involved?\n- What was the breach?\n- Do you have evidence?\n- What damages are you seeking?",
                "suggestions": [
                    "How do I sue for breach of contract?",
                    "What evidence do I need?",
                    "Should I hire a lawyer?",
                    "What are my damages?"
                ]
            }
        }
        
        # Quick responses for common questions
        self.quick_responses = {
            "rights": {
                "arrest": "When arrested, you have the right to:\n• Remain silent\n• Speak to a lawyer\n• Be informed of charges\n• A speedy trial\n• Protection from unreasonable searches",
                "employment": "As an employee, you have the right to:\n• Minimum wage and overtime\n• Safe working conditions\n• Protection from discrimination\n• Family and medical leave\n• Workers' compensation",
                "housing": "As a tenant, you have the right to:\n• Habitable living conditions\n• Privacy in your home\n• Proper notice before eviction\n• Return of security deposit\n• Fair housing without discrimination"
            },
            "immediate_actions": {
                "arrest": "If arrested:\n1. Stay calm and don't resist\n2. Say 'I want to speak to my lawyer'\n3. Don't answer questions without counsel\n4. Don't consent to searches\n5. Contact family/friends",
                "fired": "If fired:\n1. Request written termination letter\n2. Collect all documents\n3. File for unemployment immediately\n4. Contact Department of Labor\n5. Consider legal consultation",
                "eviction": "If facing eviction:\n1. Review the eviction notice carefully\n2. Contact legal aid immediately\n3. Don't move out without legal advice\n4. Document all communications\n5. Consider negotiating with landlord"
            }
        }

    def get_response(self, message: str, session_id: str) -> Dict:
        """Generate a response based on the user's message and conversation context"""
        
        # Initialize session if not exists
        if session_id not in self.conversation_history:
            self.conversation_history[session_id] = []
            self.user_context[session_id] = {}
        
        # Add message to history
        self.conversation_history[session_id].append({
            'user': message,
            'timestamp': datetime.now().isoformat()
        })
        
        # Analyze message and determine response
        response = self._analyze_message(message, session_id)
        
        # Add response to history
        self.conversation_history[session_id].append({
            'bot': response['message'],
            'timestamp': datetime.now().isoformat()
        })
        
        return response

    def _analyze_message(self, message: str, session_id: str) -> Dict:
        """Analyze the message and generate appropriate response"""
        message_lower = message.lower()
        
        # Check for greeting
        if any(word in message_lower for word in self.conversation_flows["greeting"]["triggers"]):
            return {
                'message': self.conversation_flows["greeting"]["response"],
                'suggestions': self.conversation_flows["greeting"]["suggestions"]
            }
        
        # Check for specific legal situations
        for flow_key, flow_data in self.conversation_flows.items():
            if flow_key != "greeting":
                if any(word in message_lower for word in flow_data["triggers"]):
                    # Update user context
                    self.user_context[session_id]['primary_issue'] = flow_key
                    
                    # Check if this is a follow-up question
                    if self.user_context[session_id].get('issue_identified'):
                        return self._handle_follow_up(message, flow_key, session_id)
                    else:
                        self.user_context[session_id]['issue_identified'] = True
                        return {
                            'message': flow_data["response"] + "\n\n" + flow_data["follow_up"],
                            'suggestions': flow_data["suggestions"]
                        }
        
        # Handle specific questions
        if "right" in message_lower or "rights" in message_lower:
            return self._handle_rights_question(message, session_id)
        elif "do" in message_lower and "now" in message_lower:
            return self._handle_immediate_actions_question(message, session_id)
        elif "lawyer" in message_lower or "attorney" in message_lower:
            return self._handle_lawyer_question(message, session_id)
        elif "cost" in message_lower or "money" in message_lower or "expensive" in message_lower:
            return self._handle_cost_question(message, session_id)
        elif "time" in message_lower or "long" in message_lower:
            return self._handle_timing_question(message, session_id)
        
        # Default response
        return {
            'message': "I understand you're dealing with a legal situation. To help you better, could you tell me more specifically about your issue? For example:\n\n• What type of legal problem are you facing?\n• What happened that led to this situation?\n• What outcome are you hoping for?\n\nI'm here to help guide you through your legal rights and options.",
            'suggestions': [
                "I need help with criminal charges",
                "I have an employment issue",
                "I'm dealing with a housing problem",
                "I need family law advice",
                "I have a contract dispute"
            ]
        }

    def _handle_follow_up(self, message: str, issue_type: str, session_id: str) -> Dict:
        """Handle follow-up questions based on the identified issue"""
        message_lower = message.lower()
        
        if issue_type == "arrest":
            if "right" in message_lower:
                return {
                    'message': self.quick_responses["rights"]["arrest"],
                    'suggestions': ["What should I say to police?", "How do I get a lawyer?", "What about bail?"]
                }
            elif "lawyer" in message_lower:
                return {
                    'message': "You have the right to a lawyer. If you can't afford one:\n\n• Ask for a public defender\n• Contact legal aid organizations\n• Look for pro bono services\n• Consider a payment plan with private attorneys\n\nNever represent yourself in criminal matters - it's too risky.",
                    'suggestions': ["How do I find a good lawyer?", "What questions should I ask?", "How much will it cost?"]
                }
        
        elif issue_type == "employment":
            if "right" in message_lower:
                return {
                    'message': self.quick_responses["rights"]["employment"],
                    'suggestions': ["How do I file a complaint?", "What is wrongful termination?", "Can I get unemployment?"]
                }
            elif "unemployment" in message_lower:
                return {
                    'message': "To file for unemployment:\n\n1. Apply immediately (don't wait)\n2. Contact your state's unemployment office\n3. Have your work history ready\n4. Be honest about why you were terminated\n5. Appeal if denied\n\nEach state has different rules, so check your state's specific requirements.",
                    'suggestions': ["What if I'm denied?", "How long does it take?", "What documents do I need?"]
                }
        
        elif issue_type == "housing":
            if "right" in message_lower:
                return {
                    'message': self.quick_responses["rights"]["housing"],
                    'suggestions': ["How do I fight an eviction?", "What about repairs?", "Can I withhold rent?"]
                }
            elif "eviction" in message_lower:
                return {
                    'message': "To fight an eviction:\n\n1. Don't move out immediately\n2. Contact legal aid right away\n3. Check if the eviction notice is valid\n4. Consider negotiating with landlord\n5. File an answer to the eviction lawsuit\n\nMany evictions can be fought successfully with proper legal help.",
                    'suggestions': ["What makes an eviction illegal?", "How long do I have?", "What if I can't afford a lawyer?"]
                }
        
        # Default follow-up response
        return {
            'message': f"Thank you for that information. Based on what you've told me about your {issue_type} situation, I recommend:\n\n1. Document everything\n2. Don't sign anything without legal review\n3. Contact appropriate legal resources\n4. Act quickly - time limits may apply\n\nWould you like me to provide more specific guidance on any of these areas?",
            'suggestions': ["What documents should I gather?", "How do I find legal help?", "What are my next steps?"]
        }

    def _handle_rights_question(self, message: str, session_id: str) -> Dict:
        """Handle questions about legal rights"""
        context = self.user_context.get(session_id, {})
        issue = context.get('primary_issue')
        
        if issue in self.quick_responses["rights"]:
            return {
                'message': self.quick_responses["rights"][issue],
                'suggestions': ["What should I do next?", "How do I enforce my rights?", "What if my rights were violated?"]
            }
        
        return {
            'message': "Your legal rights depend on your specific situation. To give you accurate information, could you tell me more about your legal issue? For example:\n\n• What type of legal problem are you facing?\n• What happened that led to this situation?\n• Are you dealing with employment, housing, criminal, or family law?",
            'suggestions': ["I was arrested", "I was fired", "I'm being evicted", "I'm getting divorced"]
        }

    def _handle_immediate_actions_question(self, message: str, session_id: str) -> Dict:
        """Handle questions about immediate actions"""
        context = self.user_context.get(session_id, {})
        issue = context.get('primary_issue')
        
        if issue in self.quick_responses["immediate_actions"]:
            return {
                'message': self.quick_responses["immediate_actions"][issue],
                'suggestions': ["What documents do I need?", "How do I find a lawyer?", "What are my legal options?"]
            }
        
        return {
            'message': "The immediate actions you should take depend on your specific legal situation. To provide accurate guidance, I need to know:\n\n• What type of legal problem are you facing?\n• What just happened?\n• What outcome are you hoping for?\n\nOnce I understand your situation better, I can give you specific steps to take right now.",
            'suggestions': ["I was just arrested", "I was just fired", "I just received an eviction notice"]
        }

    def _handle_lawyer_question(self, message: str, session_id: str) -> Dict:
        """Handle questions about finding lawyers"""
        return {
            'message': "Finding the right lawyer is crucial. Here are your options:\n\n**Free/Low-Cost Options:**\n• Legal Aid organizations\n• Pro bono services\n• Public defenders (criminal cases)\n• Law school clinics\n\n**Private Attorneys:**\n• Bar association referrals\n• Online legal directories\n• Personal recommendations\n• Specialized legal organizations\n\n**Questions to Ask:**\n• Experience with your type of case\n• Fee structure and costs\n• Communication style\n• Success rate\n\nAlways consult multiple attorneys before choosing.",
            'suggestions': ["How do I know if a lawyer is good?", "What questions should I ask?", "How much will it cost?"]
        }

    def _handle_cost_question(self, message: str, session_id: str) -> Dict:
        """Handle questions about legal costs"""
        return {
            'message': "Legal costs vary widely depending on your situation:\n\n**Free Options:**\n• Legal Aid (income-based)\n• Pro bono services\n• Public defenders\n• Self-help resources\n\n**Low-Cost Options:**\n• Payment plans\n• Contingency fees (personal injury)\n• Flat fees for simple matters\n• Legal insurance\n\n**Cost Factors:**\n• Case complexity\n• Attorney experience\n• Geographic location\n• Time required\n\nDon't let cost prevent you from getting legal help - many options exist for different budgets.",
            'suggestions': ["How do I find free legal help?", "What are payment plans?", "Is legal aid available?"]
        }

    def _handle_timing_question(self, message: str, session_id: str) -> Dict:
        """Handle questions about legal timing"""
        return {
            'message': "Legal timing is critical and varies by situation:\n\n**Immediate (Same Day):**\n• Criminal arrests\n• Emergency evictions\n• Workplace safety issues\n\n**Within Days:**\n• Employment discrimination\n• Contract disputes\n• Family law emergencies\n\n**Within Weeks:**\n• Most civil lawsuits\n• Administrative complaints\n• Standard legal filings\n\n**Important:** Many legal claims have strict deadlines (statutes of limitations). Acting quickly often improves your chances of success and preserves your rights.",
            'suggestions': ["What are the deadlines for my case?", "How do I file quickly?", "What if I missed a deadline?"]
        }

    def get_conversation_history(self, session_id: str) -> List[Dict]:
        """Get conversation history for a session"""
        return self.conversation_history.get(session_id, [])

    def clear_conversation(self, session_id: str):
        """Clear conversation history for a session"""
        if session_id in self.conversation_history:
            del self.conversation_history[session_id]
        if session_id in self.user_context:
            del self.user_context[session_id] 