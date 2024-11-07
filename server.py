from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_to_emotion_detector():

    try:
        textToAnalyze = request.args.get("textToAnalyze")
        if not textToAnalyze:
            raise ValueError("No text provided for analysis.")

        response = emotion_detector(textToAnalyze)

        formatted = response.get('formatted')

        if formatted is None:
            raise ValueError("Invalid response from emotion_detector().")

        dom_emotion = formatted.get("dominant_emotion")

        if dom_emotion is None:
            raise ValueError("No dominant emotion found in response.")
        
        formatted_scores = ', '.join([f"'{emotion}': {score}" for emotion, score in formatted.items()])
        return f"For the given statement, the system response is {formatted_scores}. The dominant emotion is {dom_emotion}."

    except (TypeError, RuntimeError) as e:
        return f"An unexpected error occurred: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)
