from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection App")

@app.route("/emotionDetector")
def emotion_detector():

    # Get the text from the query parameters
    text_to_analyze = request.args.get('text_to_analyze')
    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)

    # validate the result
    output = ''
    if 'dominant_emotion' not in result or result['dominant_emotion'] is None:
        output = "Error: Unable to detect emotion"
    else:
        output = f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is <b>{dominant_emotion}</b>.".format(
            anger=result['anger'],
            disgust=result['disgust'],
            fear=result['fear'],
            joy=result['joy'],
            sadness=result['sadness'],
            dominant_emotion=result['dominant_emotion']
        )

    return output

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)