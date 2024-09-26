"""
Server that directs requests for sentiment analysis to internal function.
"""

from flask import Flask, render_template, request
from final_project.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Routes to default index.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Pulls requested text for sentiment analysis from request args.
    Passes to function/api and returns formatted analysis.
    """

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    return (
        f"For the given statement, the system response is 'anger':"
        f"{anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. " 
        f"The dominant emotion is {dominant_emotion}."
    )


if __name__ == '__main__':
    app.run(debug=True)
