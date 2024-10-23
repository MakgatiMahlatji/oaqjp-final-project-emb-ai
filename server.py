"""
Flask application for emotion detection.

This module sets up a Flask web application with endpoints to detect emotions
from text input. It uses the emotion_detector function from the
EmotionDetection.emotion_detection module to analyze the given text and
return the probabilities of different emotions along with the dominant emotion.

Endpoints:
- GET /: Renders the home page.
- POST /emotionDetector: Accepts text input and returns the detected emotions.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page.

    Returns:
        str: The HTML content for the home page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """Detect the emotion from the given text.

    This function receives a POST request with JSON data containing
    the text to analyze. It processes the text and returns the 
    probabilities of various emotions and the dominant emotion.

    Returns:
        jsonify: A JSON response containing the detected emotions
                  or an error message if the input is invalid.
    """
    data = request.get_json()
    text_to_analyze = data.get('text', '')
    result = emotion_detector(text_to_analyze)

    if "error" in result:
        return jsonify({"error": result["error"]}), 500

    if result.get('dominant_emotion') is None:
        return jsonify({"message": "Invalid text! Please try again!"})

    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']},"
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}.")
    return jsonify({"message": response_message})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
