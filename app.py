# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def classify_message(user_message):
    if user_message.startswith("http"):
        URL = "http://127.0.0.1:5001/generate_caption"
        PARAMS = {'image_url': user_message}
        response = requests.post(url=URL, json=PARAMS)
        caption = response.json()['caption']
        return caption
    else:
        return "General response"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify_message', methods=['POST'])
def classify_message_route():
    user_message = request.form['user_message']
    response_text = classify_message(user_message)
    return render_template('index.html', response=response_text)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)
