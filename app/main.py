from flask import Flask, request, render_template, jsonify
from rag_pipeline import get_answer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    
    data = request.json
    query = data.get('question')
    print("Received query:", query)

    if not query:
        return jsonify({'error': 'No question provided'}), 400
    answer = get_answer(query)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)