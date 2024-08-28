import requests
import json

def get_emotion_reponse(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    INPUT = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = INPUT, headers=HEADERS)
    return json.loads(response.text) 

def get_dominant_emotion(emotions):
    max_value = -1
    max_label = ""

    for key in emotions.keys():
        if(emotions[key] > max_value):
            max_value = emotions[key]
            max_label = key

    return max_label

def emotion_detector(text_to_analyse):
    emotion_response = get_emotion_reponse(text_to_analyse)
    if(emotion_response is not None):
        response = emotion_response["emotionPredictions"][0]["emotion"]
        response["dominant_emotion"] = get_dominant_emotion(response)
        return response
    else:
        return "something went wrong"