# ✋ Hand Gesture Number Detection using OpenCV & MediaPipe

---

## 📌 Project Overview

This project is a real-time hand gesture recognition system that detects and counts the number of fingers shown using a webcam.

It uses OpenCV for video capture and MediaPipe for hand landmark detection. The system processes live video input, identifies finger positions, and displays the number of fingers raised in real time.

This project demonstrates how computer vision can be used to build interactive, real-time applications without requiring any training dataset.

---

## 🚀 Features

- 🎥 Real-time webcam detection  
- ✋ Hand landmark tracking (21 key points)  
- 🔢 Finger counting (0–5)  
- ⚡ Fast and lightweight  
- 🧠 No dataset or training required  

---

## ⚙️ Tech Stack

- Python  
- OpenCV  
- MediaPipe  

---

## 🧠 How It Works

1. Capture video using webcam  
2. Convert frames to RGB  
3. Detect hand using MediaPipe  
4. Extract hand landmarks  
5. Apply logic to determine finger positions  
6. Count and display number of fingers  

---

## 📊 Flowchart

👉 <img width="496" height="321" alt="image" src="https://github.com/user-attachments/assets/0680a85a-375d-40ef-9c7f-f6bd05466449" />


**Example flow:**

Webcam → Hand Detection → Landmark Extraction → Finger Logic → Output

---

## 📁 Project Structure

hand-gesture-project/
│
├── src/
│   ├── main.py
│   ├── hand_tracker.py
│   └── utils.py
│
├── outputs/
├── requirements.txt
└── README.md

---

## 🛠️ Installation & Setup

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/hand-gesture-detection.git
cd hand-gesture-detection

### 2. Create virtual environment

python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

---

## ▶️ Run the Project

python src/main.py

---

## 🎥 Usage

- Show your hand in front of the webcam  
- Extend fingers (0–5)  
- The system will display the detected number  

⸻

📸 Screenshots

<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/5ee71d87-5a43-4ebe-b1d3-752fc9ef69e6" />
<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/df7e3830-f457-4fb7-b0fb-9c77bd2ad130" />
<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/825cf4d0-633b-419e-a234-711839850bc9" />


Examples:
	•	Hand detection with landmarks
	•	Finger count display

⸻

⚠️ Limitations
	•	Accuracy depends on lighting conditions
	•	Thumb detection may vary with angle
	•	Works best with a single hand

⸻

🔮 Future Improvements
	•	Gesture recognition (👍 ✌️ 👊)
	•	Multi-hand detection
	•	Smoother predictions (reduce flickering)
	•	GUI-based interface

⸻

🧠 Conclusion

This project showcases the power of computer vision in building real-time interactive systems. By combining OpenCV and MediaPipe, it is possible to create efficient gesture recognition systems without the need for large datasets or complex training processes.

⸻

⭐ If you like this project

Give it a star on GitHub ⭐
