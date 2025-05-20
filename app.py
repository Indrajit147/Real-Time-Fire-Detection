import streamlit as st
from ultralytics import YOLO
import cv2
import time
import pygame
import threading
import os

# Streamlit setup
st.set_page_config(page_title="Fire Detection", layout="centered")
st.title("🔥 Real-Time Fire Detection")
st.markdown("Using a YOLO model to detect fire through your webcam.")

# Alarm playing function
def play_alarm(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

# Load YOLO model
if 'model' not in st.session_state:
    st.session_state.model = YOLO('best.pt')

# Session control for sound
if 'alarm_played' not in st.session_state:
    st.session_state.alarm_played = False

start_button = st.button("Start Detection")

if start_button:
    stframe = st.empty()
    cap = cv2.VideoCapture(0)

    stop_button = st.button("Stop Detection", key="stop_button")
    progress = st.progress(0)
    fire_message = st.empty()

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to access webcam.")
            break

        results = st.session_state.model.predict(source=frame, imgsz=640, conf=0.6, verbose=False)
        annotated_frame = results[0].plot()

        fire_detected = any(cls == 0 for cls in results[0].boxes.cls)

        if fire_detected:
            progress.progress(100)
            fire_message.write("🔥 Fire Detected!")

            if not st.session_state.alarm_played:
                alarm_path = 'alarm.mp3'  # Use full path if needed
                if os.path.exists(alarm_path):
                    threading.Thread(target=play_alarm, args=(alarm_path,), daemon=True).start()
                    st.session_state.alarm_played = True
                else:
                    st.warning("⚠️ alarm.mp3 not found.")
        else:
            progress.progress(0)
            fire_message.write("No Fire Detected")
            st.session_state.alarm_played = False

        stframe.image(annotated_frame, channels="BGR")

        if stop_button:
            cap.release()
            st.success("Detection stopped.")
            break

        time.sleep(0.03)
