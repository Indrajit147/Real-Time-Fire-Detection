# 🔥 Real Time Fire Detection System

A real-time fire detection application built using **YOLO**, **OpenCV**, and **Streamlit**, with an integrated audio alert system powered by **pygame**.

## 🚀 Features

- 🔍 Real-time fire detection via webcam using a custom YOLO model
- 🧠 Based on **Ultralytics YOLOv8**
- 🧯 Visual alert through annotated video stream
- 🔊 Audio alarm (`alarm.mp3`) plays when fire is detected
- 🧠 Intelligent logic prevents repeated alarm playback
- ✅ Streamlit-based clean user interface

---

## 🖼️ Demo

![fire-detection-demo](demo.mp4)

---

## 🛠️ Technologies Used

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [OpenCV](https://opencv.org/)
- [Streamlit](https://streamlit.io/)
- [pygame](https://www.pygame.org/) (for audio playback)

---

## 🎓 How It Works

1. Accesses webcam video feed using OpenCV
2. Runs frame-by-frame detection using a custom YOLOv8 model
3. If fire is detected (class 0), an alert sound is played
4. Results are displayed with bounding boxes in the Streamlit UI

---


