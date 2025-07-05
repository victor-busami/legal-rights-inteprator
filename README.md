# AI-Powered Legal Rights Interpreter (SDG 16)

An intelligent web application that helps users understand their legal rights using machine learning and natural language processing. Built with Flask and designed to promote access to justice (SDG 16: Peace, Justice, and Strong Institutions).

## 🎯 Project Overview

This application uses AI/ML to interpret legal questions and provide users with:
- **Legal domain classification** (Labor Law, Criminal Law, Civil Law, Family Law, Property Law)
- **Entity extraction** (names, dates, legal terms, money amounts)
- **Contextual legal rights interpretation**
- **Relevant legal references and statutes**

## ✨ Features

### 🤖 AI/ML Capabilities
- **Smart Text Classification**: Automatically identifies the legal domain of user queries
- **Named Entity Recognition**: Extracts key legal entities using pattern matching
- **Contextual Interpretation**: Provides domain-specific legal rights and advice
- **Legal Knowledge Base**: Comprehensive rights database for different legal areas

### 🎨 User Interface
- **Clean, Professional Design**: Modern UI with clear sections
- **Responsive Layout**: Works on desktop and mobile devices
- **Detailed Results**: Shows input, analysis, interpretation, and references
- **User-Friendly**: Simple form-based interaction

### 📋 Legal Domains Covered
- **Labor Law**: Employment rights, discrimination, workplace safety
- **Criminal Law**: Constitutional rights, due process, legal counsel
- **Civil Law**: Contracts, torts, lawsuits, damages
- **Family Law**: Divorce, custody, child support, domestic relations
- **Property Law**: Landlord-tenant, real estate, housing rights

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Flask

### Installation

1. **Clone or download the project**
   ```bash
   cd legal-law
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the app**
   Open your browser and go to: `http://127.0.0.1:5000`

## 📁 Project Structure

```
legal-law/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── models/               # ML modules
│   ├── __init__.py
│   ├── classifier.py     # Legal domain classification
│   ├── ner.py           # Named entity recognition
│   └── qa.py            # Question answering & interpretation
├── templates/            # HTML templates
│   ├── layout.html       # Base template
│   ├── index.html        # Input form
│   └── result.html       # Results display
└── static/              # CSS styles
    └── style.css
```

## 🔧 How It Works

### 1. User Input
Users enter their legal question or paste legal documents through a simple web form.

### 2. AI Processing Pipeline
- **Classification**: Identifies the legal domain (Labor, Criminal, Civil, etc.)
- **Entity Extraction**: Finds key legal terms, names, dates, and references
- **Interpretation**: Generates contextual legal rights based on the domain

### 3. Results Display
The app presents:
- **User's original input**
- **AI analysis** (domain + extracted entities)
- **Legal rights interpretation** with specific advice
- **Relevant legal references** and statutes
- **Professional disclaimer**

## 🧠 ML Implementation

### Text Classification
- Uses keyword-based scoring system
- Covers 5 major legal domains
- Efficient pattern matching for quick responses

### Entity Recognition
- Regex-based extraction for legal entities
- Identifies: persons, organizations, dates, money, legal references
- Handles case numbers, court names, and legal citations

### Legal Interpretation
- Domain-specific knowledge bases
- Contextual rights generation
- Issue identification (wrongful termination, discrimination, etc.)
- Professional legal disclaimers

## 💡 Example Usage

### Sample Questions to Try:
- "I was fired from my job without notice"
- "My landlord is trying to evict me"
- "I was arrested and charged with a crime"
- "I'm going through a divorce and need custody"
- "My employer is not paying me overtime"

### Expected Output:
- **Domain**: Labor Law
- **Entities**: "fired", "job", "employer"
- **Rights**: Minimum wage, discrimination protection, workplace safety
- **References**: Title VII, FLSA, ADA, FMLA

## 🎯 SDG 16 Alignment

This project directly supports **Sustainable Development Goal 16: Peace, Justice, and Strong Institutions** by:

- **Promoting Access to Justice**: Making legal information accessible to everyone
- **Reducing Legal Barriers**: Helping users understand their rights
- **Supporting Strong Institutions**: Complementing existing legal systems
- **Empowering Citizens**: Providing legal knowledge and awareness

## 🔒 Legal Disclaimer

⚠️ **Important**: This application provides informational legal content only and should not be considered legal advice. Users should consult with qualified attorneys for specific legal guidance.

## 🛠️ Technical Details

### Dependencies
- **Flask**: Web framework
- **Python 3.7+**: Runtime environment

### Architecture
- **Frontend**: Flask templates with Jinja2
- **Backend**: Python with custom ML modules
- **Styling**: CSS for responsive design
- **Processing**: Pattern matching and knowledge-based AI

### Performance
- **Fast Startup**: No heavy model downloads
- **Efficient Processing**: Lightweight algorithms
- **Responsive UI**: Quick user interactions

## 🚀 Future Enhancements

Potential improvements for future versions:
- Integration with real legal databases
- More sophisticated NLP models
- Multi-language support
- Document upload capabilities
- User feedback and learning
- Integration with legal aid organizations

## 📞 Support

For questions or issues:
1. Check the project structure and dependencies
2. Ensure Python 3.7+ is installed
3. Verify Flask is properly installed
4. Check browser console for any errors

## 📄 License

This project is created for educational and demonstration purposes. Please ensure compliance with local laws and regulations when using legal information.

---

**Built with ❤️ for SDG 16: Peace, Justice, and Strong Institutions** 