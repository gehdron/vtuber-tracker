# src/extract_landmarks.py
import cv2
import mediapipe as mp
import json

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

BaseOptions = python.BaseOptions
FaceLandmarker = vision.FaceLandmarker
FaceLandmarkerOptions = vision.FaceLandmarkerOptions
VisionRunningMode = vision.RunningMode

options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path="models/face_landmarker.task"),
    running_mode=VisionRunningMode.VIDEO,
    output_face_blendshapes=True,
    output_facial_transformation_matrixes=True,
)

# TODO (you): open your video with cv2.VideoCapture, loop frames,
# call landmarker.detect_for_video(mp_image, timestamp_ms),
# pull out result.face_blendshapes and result.facial_transformation_matrixes,
# and append a per-frame dict to a list.
# When done, json.dump(your_list, open("output/tracking_data.json", "w"))