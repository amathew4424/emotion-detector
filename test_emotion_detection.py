import json
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    TESTCASES = [
        ["I am glad this happened", "joy"],
        ["I am really mad about this", "anger"],
        ["I feel disgusted just hearing about this", "disgust"],
        ["I am so sad about this", "sadness"],
        ["I am really afraid that this will happen", "fear"]
    ]

    def test_emotion_detection(self):
        for i in range(0, len(self.TESTCASES)):
            print("Test Case: " + str(self.TESTCASES[i]))
            detector_response = emotion_detector(self.TESTCASES[i][0])

            self.assertEqual(
                detector_response["dominant_emotion"], 
                self.TESTCASES[i][1]
            )
            
            print("PASSED\n")

unittest.main()
