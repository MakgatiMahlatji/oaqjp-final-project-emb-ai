import requests
import json

def emotion_detector(text_to_analyse):

    if not text_to_analyse.strip():
        return {
            'anger': None,'disgust': None,'fear': None,'joy': None,'sadness': None,'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    try:
        response = requests.post(url, json = myobj, headers=header)
        if response.status_code == 400:
            return {'anger': None,'disgust': None,'fear': None,'joy': None,'sadness': None,'dominant_emotion': None
            }

        response.raise_for_status()
        formatted_response = json.loads(response.text)
        required_emotions = ['anger','disgust','fear','joy','sadness']

        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
        extracted_emotions = {emotion: emotion_scores[emotion] for emotion in required_emotions if emotion in emotion_scores}
        dominant_emotion = max(extracted_emotions,key=extracted_emotions.get)

        output ={'anger' : extracted_emotions['anger'],'disgust' : extracted_emotions['disgust'],'fear' : extracted_emotions['fear'],'joy' : extracted_emotions['joy'],'sadness' : extracted_emotions['sadness'],'dominant_emotion' : dominant_emotion}

        return output

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

    except json.JSONDecodeError:
        print("Error decoding JSON response")
        return None