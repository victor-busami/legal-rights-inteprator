from flask import Flask, render_template, request
from models.classifier import classify
from models.ner import extract_entities, get_entity_texts
from models.qa import answer_question, get_legal_references

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        
        # Process with ML models
        domain = classify(user_input)
        entities = extract_entities(user_input)
        answer = answer_question(user_input, domain)
        legal_references = get_legal_references(domain)
        
        # Extract entity texts for display
        entity_texts = get_entity_texts(entities)
        
        return render_template('result.html', 
                             answer=answer, 
                             entities=entity_texts,
                             domain=domain,
                             legal_references=legal_references,
                             user_input=user_input)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 