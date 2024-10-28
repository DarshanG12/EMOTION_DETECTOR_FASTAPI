# Emotion Detection in Video with FastAPI

This project provides an API for detecting emotions in video files using FastAPI and the `fer` library.

## Features

- Detects emotions such as `happy`, `fear`, `sad`, and `surprise` from video files.
- Calculates the percentage representation of each detected emotion.
- Easily deployable using FastAPI.

## Requirements

- Python 3.11+
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DarshanG12/EMOTION_DETECTOR_FASTAPI.git
   

2. Install dependencies
pip install -r requirements.txt

3.Start the FastAPI server:
uvicorn main:app --host 127.0.0.1 --port 8000 --reload

4.Send a POST request to the API with the video file path:

URL: http://127.0.0.1:8000/analyze-video-emotions
Method: POST

JSON Body:
{
  "filePath": "<absolute path to your video file>"
}

5.Sample Response:
{
    "emotions": {
        "fear": 1.5425531914893622,
        "happy": 70.69148936170212,
        "sad": 26.06382978723405,
        "surprise": 1.7021276595744685
    }
}

