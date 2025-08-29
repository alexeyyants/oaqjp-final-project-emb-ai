"""Flask server for Emotion Detection App."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection App")

@app.route("/emotionDetector")
def emotion_detector_route():
    """Route to detect emotions from input text."""
    # Get the text from the query parameters
    text_to_analyze = request.args.get('textToAnalyze')
    print(text_to_analyze)
    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)

    # validate the result
    if 'dominant_emotion' not in result or result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is "
        f"<b>{result['dominant_emotion']}</b>."
    )

@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
