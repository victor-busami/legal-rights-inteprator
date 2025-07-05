import json
import os
from datetime import datetime
from typing import Dict, List

FEEDBACK_FILE = 'data/feedback.json'

def ensure_data_directory():
    """Ensure the data directory exists"""
    os.makedirs('data', exist_ok=True)

def save_feedback(question: str, answer: str, rating: int, feedback_text: str = ""):
    """Save user feedback to the database"""
    ensure_data_directory()
    
    feedback_entry = {
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "answer": answer,
        "rating": rating,
        "feedback_text": feedback_text,
        "domain": classify_feedback_domain(question)
    }
    
    # Load existing feedback
    existing_feedback = load_feedback()
    existing_feedback.append(feedback_entry)
    
    # Save updated feedback
    with open(FEEDBACK_FILE, 'w', encoding='utf-8') as f:
        json.dump(existing_feedback, f, indent=2, ensure_ascii=False)

def load_feedback() -> List[Dict]:
    """Load existing feedback from file"""
    ensure_data_directory()
    
    if not os.path.exists(FEEDBACK_FILE):
        return []
    
    try:
        with open(FEEDBACK_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def classify_feedback_domain(question: str) -> str:
    """Classify the domain of feedback for analysis"""
    from .classifier import classify
    return classify(question)

def get_feedback_stats() -> Dict:
    """Get statistics from user feedback"""
    feedback_data = load_feedback()
    
    if not feedback_data:
        return {
            "total_feedback": 0,
            "average_rating": 0,
            "domain_distribution": {},
            "recent_feedback": []
        }
    
    # Calculate statistics
    total_feedback = len(feedback_data)
    ratings = [f["rating"] for f in feedback_data if f["rating"] > 0]
    average_rating = sum(ratings) / len(ratings) if ratings else 0
    
    # Domain distribution
    domain_counts = {}
    for feedback in feedback_data:
        domain = feedback.get("domain", "Unknown")
        domain_counts[domain] = domain_counts.get(domain, 0) + 1
    
    # Recent feedback (last 10)
    recent_feedback = sorted(feedback_data, key=lambda x: x["timestamp"], reverse=True)[:10]
    
    return {
        "total_feedback": total_feedback,
        "average_rating": round(average_rating, 2),
        "domain_distribution": domain_counts,
        "recent_feedback": recent_feedback
    }

def get_domain_performance() -> Dict:
    """Get performance metrics by legal domain"""
    feedback_data = load_feedback()
    
    domain_performance = {}
    
    for feedback in feedback_data:
        domain = feedback.get("domain", "Unknown")
        rating = feedback.get("rating", 0)
        
        if domain not in domain_performance:
            domain_performance[domain] = {
                "total_feedback": 0,
                "ratings": [],
                "average_rating": 0
            }
        
        domain_performance[domain]["total_feedback"] += 1
        if rating > 0:
            domain_performance[domain]["ratings"].append(rating)
    
    # Calculate averages
    for domain, data in domain_performance.items():
        if data["ratings"]:
            data["average_rating"] = round(sum(data["ratings"]) / len(data["ratings"]), 2)
        else:
            data["average_rating"] = 0
    
    return domain_performance

def get_improvement_suggestions() -> List[str]:
    """Generate improvement suggestions based on feedback"""
    stats = get_feedback_stats()
    suggestions = []
    
    if stats["total_feedback"] < 10:
        suggestions.append("Need more user feedback to generate meaningful insights")
        return suggestions
    
    if stats["average_rating"] < 3.5:
        suggestions.append("Consider improving answer quality and relevance")
    
    # Domain-specific suggestions
    domain_performance = get_domain_performance()
    for domain, performance in domain_performance.items():
        if performance["average_rating"] < 3.0:
            suggestions.append(f"Improve {domain} responses - current rating: {performance['average_rating']}")
    
    return suggestions

def export_feedback_data() -> str:
    """Export feedback data for analysis"""
    feedback_data = load_feedback()
    
    if not feedback_data:
        return "No feedback data available"
    
    # Create summary report
    stats = get_feedback_stats()
    performance = get_domain_performance()
    
    report = f"""
Feedback Analysis Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Summary:
- Total Feedback: {stats['total_feedback']}
- Average Rating: {stats['average_rating']}/5

Domain Performance:
"""
    
    for domain, perf in performance.items():
        report += f"- {domain}: {perf['average_rating']}/5 ({perf['total_feedback']} responses)\n"
    
    return report 