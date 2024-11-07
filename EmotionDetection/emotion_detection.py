import json
import requests

def emotion_detector(textToAnalyze):
    '''This function uses the IBM Watson NLP API to perform emotion detection on the input text.'''

    if not textToAnalyze:
        return {
            "anger": None, "disgust": None, 
            "fear": None, "joy": None, 
            "sadness": None, "dominant_emotion": None
            }, 400

    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_object = { "raw_document": { "text": textToAnalyze } }
    response = requests.post(URL, json = my_object, headers=headers)
    formatted_response = json.loads(response.text)

    formatted = formatted_response['emotionPredictions'][0]['emotion']

    max_key = max(formatted, key = formatted.get)
    formatted["dominant_emotion"] = max_key

    return {'formatted': formatted}, 200

if __name__ == "__main__":
    app.run(debug=True)

    