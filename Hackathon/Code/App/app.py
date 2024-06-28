from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

openai.api_key = "304950d84fd35e3fc2524541fc281db67b395716ce0ae8039ebcef070e4b069c"
baseurl = "https://llm.mdb.ai/"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = openai.ChatCompletion.create(
        model="llama-3-70b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ],
        stream=False
    )
    reply = response.choices[0].message['content']
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)