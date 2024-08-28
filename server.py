from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """ detect emotion and respond back to the user """
    text_to_detect = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_detect)
    return "For the given statement, the system response is "\
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "\
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "\
        f"'sadness': {result['sadness']}. "\
        f"The dominant emotion is {result['dominant_emotion']}."

@app.route("/")
def render_index_page():
    """ Render Index page """
    return render_template('index.html')