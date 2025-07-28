from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# Index html page
@app.route("/")
def get_index_template():
    return render_template("index.html")

# Analysing emotion route
@app.route("/emotionDetector")
def sent_emotion():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] == None:
        return "Invalid text! Please try again!"

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant = response["dominant_emotion"]

    message = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

    return message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)