from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from detector import detect_emotions_in_video

app = FastAPI()

# CORS setup
origins = ["http://localhost:8080"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for the request body
class VideoPath(BaseModel):
    filePath: str

# POST endpoint for analyzing video emotions
@app.post("/analyze-video-emotions")
async def analyze_video_emotions(video_path: VideoPath):
    try:
        file_path = video_path.filePath
        
        # Check if the file path is valid
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="Video file not found")

        # Perform emotion detection on the video
        emotions = detect_emotions_in_video(file_path)
        
        return {"emotions": emotions}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
