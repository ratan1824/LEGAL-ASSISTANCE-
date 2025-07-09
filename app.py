from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def chat():
    return render_template('chat.html')  # Ensure chat.html is in the 'templates' folder

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')

    if not question:
        return jsonify({'answer': 'Please enter a question.'})

    try:
        # Change the API URL according to your local setup for DeepSeek-R1 model
        response = requests.post(
            'http://localhost:11434/api/generate',  # Assuming DeepSeek is running at this port
            json={
                "model": "deepseek-r1",  # Use deepseek-r1 model from Ollama
                "prompt": question,
                "stream": False
            }
        )
        # Check if the response contains the answer
        answer = response.json().get('response', 'No response from DeepSeek.')
    except Exception as e:
        answer = f"Error contacting DeepSeek-R1: {e}"

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
