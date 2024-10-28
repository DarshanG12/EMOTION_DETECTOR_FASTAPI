from fer import FER
from fer import Video
import cv2
import os
import pandas as pd

def detect_emotions_in_video(path_video):
    try:
        # Log the file path
        print(f"Trying to open video file: {path_video}")

        # Check if the file exists
        if not os.path.exists(path_video):
            return {"error": "Video file does not exist"}

        # Verify the video file can be opened with OpenCV
        cap = cv2.VideoCapture(path_video)
        if not cap.isOpened():
            cap.release()
            return {"error": "Video capture not opening"}
        
        cap.release()

        # Initialize the emotion detector
        emotion_detector = FER(mtcnn=True)
        
        # Load and analyze video for emotions
        video = Video(path_video)
        result = video.analyze(emotion_detector, display=False, frequency=10)
        
        if not result:
            return {"error": "No emotions detected in the video"}

        # Convert to DataFrame and calculate emotion percentages
        emotions_df = video.to_pandas(result)
        if emotions_df.empty:
            return {"error": "No emotions detected in the video"}

        # Aggregate emotions and calculate percentages
        aggregated_emotions = emotions_df[["fear", "happy", "sad", "surprise"]].sum()
        total_score = aggregated_emotions.sum()
        if total_score == 0:
            return {"error": "No significant emotions detected in the video"}

        emotion_percentages = {emotion: (score / total_score) * 100 
                               for emotion, score in aggregated_emotions.items()}
        
        return emotion_percentages
    except Exception as e:
        return {"error": str(e)}
