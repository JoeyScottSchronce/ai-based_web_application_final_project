'''Responsible for rendering the index page and handling the requests to the emotion detector.'''
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    '''Renders the index page of the web application.'''
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_to_emotion_detector():
    '''Handles the request to the emotion detector and returns the response.'''

    try:
        text_to_analyze = request.args.get("textToAnalyze")

        response, status_code = emotion_detector(text_to_analyze)
        # status_code is not an unused variable, it is used in the emotion_detector function

        formatted = response.get('formatted')
        if formatted is None or formatted.get("dominant_emotion") == "None":
            return jsonify("Invalid text! Please try again.")

        dom_emotion = formatted.get("dominant_emotion")
        formatted_scores = ', '.join([f"'{emotion}': {score}" \
            for emotion, score in formatted.items()])

        return f"For the given statement, the system response is \
            {formatted_scores}. The dominant emotion is {dom_emotion}."

    except (TypeError, RuntimeError):
        return jsonify("An unexpected error occurred")

if __name__ == "__main__":
    app.run(debug=True)
