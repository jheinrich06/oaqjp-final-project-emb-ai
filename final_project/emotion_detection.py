import requests
import json


def emotion_detector(text_to_analyze):
    """
    Takes text passed to function, calls Watson API and adds dominant emotion.
    Returns expected json object
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=input_json)
    #print(response.json()['emotionPredictions'])

    if response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        return emotions


    else:

        scores = response.json()['emotionPredictions'][0]
        #print(scores)

        anger_score = scores['emotion']['anger']
        disgust_score = scores['emotion']['disgust']
        fear_score = scores['emotion']['fear']
        joy_score = scores['emotion']['joy']
        sadness_score = scores['emotion']['sadness']
        
        emotions = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
        }

        dominant_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = dominant_emotion

        return emotions