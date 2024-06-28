import os
from flask import Flask, request, jsonify, render_template
from groq import Groq

app = Flask(__name__)

client = Groq(
    api_key="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",
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    if not user_message:
        return jsonify({'error': 'Message is required'}), 400

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_message,
                }
            ],
            model="llama3-8b-8192",
        )
        response_message = chat_completion.choices[0].message.content
        print(f"Response from AI: {response_message}")
        return jsonify({'response': response_message})
    except Exception as e:
        print(f"Error from AI: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)