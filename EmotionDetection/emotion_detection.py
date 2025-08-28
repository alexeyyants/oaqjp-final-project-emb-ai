import requests
import json

def emotion_detector(text_to_analyze: str) -> dict:
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)

    formatted_response = json.loads(response.text)

    if 200 == response.status_code:
        output = formatted_response["emotionPredictions"][0]["emotion"]

        # Find the emotion with the highest rating
        dominant_emotion = max(output, key=output.get)
        output['dominant_emotion'] = dominant_emotion

        return output
    else: # if status code is not 200 (e.g. 400)
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }