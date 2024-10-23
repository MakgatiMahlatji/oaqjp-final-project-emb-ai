from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotiontection(unittest.TestCase):

    def test_joy_detection(self):
        input_text = "I am glad this happened"
        result = emotion_detector(input_text)
        self.assertEqual(result['dominant_emotion'],'joy')

    def test_anger_detection(self):
        input_text = "I am really mad about this"
        result = emotion_detector(input_text)
        self.assertEqual(result['dominant_emotion'],'anger')

    def test_disgust_detection(self):
        input_text = "I feel disgusted just hearing about this"
        result = emotion_detector(input_text)
        self.assertEqual(result['dominant_emotion'],'disgust')

    def test_sadness_detection(self):
        input_text = "I am so sad about this"
        result = emotion_detector(input_text)
        self.assertEqual(result['dominant_emotion'],'sadness')

    def test_fear_detection(self):
        input_text = "I am really afraid that this will happen"
        result = emotion_detector(input_text)
        self.assertEqual(result['dominant_emotion'],'fear')



unittest.main()