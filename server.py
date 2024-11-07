from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_to_emotion_detector():
    try:
        textToAnalyze = request.args.get("textToAnalyze")

        response = emotion_detector(textToAnalyze)
        
        if 'error' in response:
            return jsonify('No text provided for analysis.')

        formatted = response.get('formatted')
        dom_emotion = formatted.get("dominant_emotion")

        formatted_scores = ', '.join([f"'{emotion}': {score}" for emotion, score in formatted.items()])
        return f"<p>For the given statement, the system response is {formatted_scores}. The dominant emotion is {dom_emotion}.</p>"

    except Exception as e:
        return f"<p style='color: red;'>An unexpected error occurred: {str(e)}</p>", 500

if __name__ == "__main__":
    app.run(debug=True, port=8080)
