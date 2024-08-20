# IC.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate_caption', methods=['POST'])
def generate_caption():
    data = request.get_json()
    image_url = data.get('image_url')
    # Logic for generating caption from the image URL
    caption = "Generated caption for the image"
    return jsonify({'caption': caption})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

