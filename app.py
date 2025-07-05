from flask import Flask, render_template, request, jsonify, session
import os
from werkzeug.utils import secure_filename
from models.classifier import classify
from models.ner import extract_entities, get_entity_texts
from models.qa import answer_question, get_legal_references
from models.document_processor import process_document
from models.translator import translate_text, detect_language
from models.feedback import save_feedback, get_feedback_stats
from models.legal_database import search_legal_database

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # For session management

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx', 'doc'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        language = request.form.get('language', 'en')
        
        # Detect language if not specified
        if language == 'auto':
            detected_lang = detect_language(user_input)
            language = detected_lang if detected_lang else 'en'
        
        # Translate input if not in English
        if language != 'en':
            user_input = translate_text(user_input, language, 'en')
        
        # Process with ML models
        domain = classify(user_input)
        entities = extract_entities(user_input)
        answer = answer_question(user_input, domain)
        legal_references = get_legal_references(domain)
        
        # Search legal database for additional information
        database_results = search_legal_database(domain, user_input)
        
        # Extract entity texts for display
        entity_texts = get_entity_texts(entities)
        
        # Translate back to original language if needed
        if language != 'en':
            answer = translate_text(answer, 'en', language)
            legal_references = [translate_text(ref, 'en', language) for ref in legal_references]
        
        return render_template('result.html', 
                             answer=answer, 
                             entities=entity_texts,
                             domain=domain,
                             legal_references=legal_references,
                             user_input=user_input,
                             database_results=database_results,
                             language=language)
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_document():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Process the document
        extracted_text = process_document(filepath)
        
        # Clean up uploaded file
        os.remove(filepath)
        
        return jsonify({
            'success': True,
            'extracted_text': extracted_text
        })
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    question = data.get('question', '')
    answer = data.get('answer', '')
    rating = data.get('rating', 0)
    feedback_text = data.get('feedback_text', '')
    
    save_feedback(question, answer, rating, feedback_text)
    
    return jsonify({'success': True})

@app.route('/stats')
def get_stats():
    stats = get_feedback_stats()
    return jsonify(stats)

@app.route('/api/translate', methods=['POST'])
def translate_api():
    data = request.get_json()
    text = data.get('text', '')
    target_lang = data.get('target_lang', 'en')
    
    translated_text = translate_text(text, 'en', target_lang)
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True) 