from flask import Flask, render_template, request, jsonify
from final_project.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotionDetector():

    data = request.json
    text = data.get('text', '')
    result = emotion_detector(text)
    
    if result['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again."}), 400
    
    else:
        return result


if __name__ == '__main__':
    app.run(debug=True)