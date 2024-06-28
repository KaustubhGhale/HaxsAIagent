from flask import Flask, request, jsonify
from groq import Groq
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Set the GROK_API_KEY environment variable
os.environ["GROK_API_KEY"] = "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"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']

    client = Groq()
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    assistant_response = ""
    for chunk in completion:
        assistant_response += chunk.choices[0].delta.content or ""

    return jsonify({'response': assistant_response})

if __name__ == '__main__':
    app.run(debug=True)
