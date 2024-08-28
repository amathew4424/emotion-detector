import requests
import json

DETECTOR_RESPONSE_KEYS = [
    "anger", "disgust", "fear", "joy", "sadness"
]

def get_emotion_reponse(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    INPUT = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = INPUT, headers=HEADERS)
    result = { 
        "status_code": response.status_code,
        "reason": response.reason
    }

    if(response.status_code == 200):
        result["data"] = json.loads(response.text) 
    
    return result

def get_detector_response(emotions):
    max_value = -1
    max_label = None
    response = {}

    for key in DETECTOR_RESPONSE_KEYS:
        if(key in emotions):
            response[key] = emotions[key]
            if(emotions[key] > max_value):
                max_value = emotions[key]
                max_label = key
        else
            response[key] = None

    response["dominant_emotion"] = max_label
    return response

def emotion_detector(text_to_analyse):
    emotion_response = get_emotion_reponse(text_to_analyse)
    if(emotion_response["status_code"] == 200):
        return get_detector_response(
            emotion_response["emotionPredictions"][0]["emotion"]
        )
        
    elif(emotion_response["status_code"] == 400):
        return get_detector_response({})

    else:
        return None