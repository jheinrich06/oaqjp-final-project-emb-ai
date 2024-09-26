import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def joy_test(self):
        prompt = "I am glad this happened."
        result = emotion_detector(prompt)
        self.assertEqual(result['dominant_emotion'], 'joy')

    def anger_test(self):
        prompt = "I am really mad about this."
        result = emotion_detector(prompt)
        self.assertEqual(result['dominant_emotion'], 'anger')

    def disgust_test(self):
        prompt = "I feel disgusted just hearing about this."
        result = emotion_detector(prompt)
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def sadness_test(self):
        prompt = "I am so sad about this."
        result = emotion_detector(prompt)
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def fear_test(self):
        prompt = "I am really afraid that this will happen."
        result = emotion_detector(prompt)
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()