import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = obj, headers=header)

    formatted = json.loads(response.text)
    anger_score = formatted['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted['emotionPredictions'][0]['emotion']['sadness']

    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
    }

    dominant_one = get_dominant(result)

    result['dominant_emotion'] = dominant_one

    return result

def get_dominant(emotion_dict):
    dominant_emotion = 0
    name = ""
    for index,emotion in enumerate(emotion_dict):
        if emotion_dict[emotion] > dominant_emotion:
            dominant_emotion = emotion_dict[emotion]
            name = emotion

    return name