# 🤖 AI-Powered Digital Health Coach
**by Meie Koning**

A next-gen health coach that uses **vision**, **language**, **voice**, and **reinforcement learning** to track food intake, exercise posture, and lifestyle habits—offering real-time feedback, motivational nudges, and weekly summaries.

---

## 🧠 Features

### 👁️ Visual Recognition
- 🍽️ Recognizes meals and estimates calories using **DINOv2**
- 🏋️ Evaluates exercise posture via **MediaPipe** body landmarks

### 🧠 Personalized Reasoning
- 🎯 Interprets user goals like "lose weight", "sleep better", etc.
- 🗣️ GPT-4V provides real-time feedback, encouragement, and habit suggestions

### 📊 Habit Tracking + RL Optimization
- 📈 Tracks habits, form scores, calories, etc.
- 🧪 Uses reinforcement learning to personalize nudges and weekly plans

### 🎙️ Voice Interaction
- 🎧 Uses **Whisper** for natural conversation via speech input
- 🔊 TTS support for spoken feedback

---

## 🧩 Architecture Overview

- User → Camera → Vision (DINOv2, MediaPipe) → GPT-4V → Habits DB → RL → UI ↘ Whisper (voice input) ↗

---

## ⚙️ Tech Stack

| Component        | Tools/Models                      |
|------------------|-----------------------------------|
| Vision           | DINOv2, MediaPipe, OpenCV         |
| Language         | GPT-4V, LangChain, custom prompts |
| Audio            | Whisper, pyttsx3 / ElevenLabs     |
| Reinforcement    | RLlib / custom Q-learning         |
| UI/API           | Streamlit / React + FastAPI       |
| Database         | SQLite / PostgreSQL               |

---

## 🛠️ Installation

```bash
git clone https://github.com/your-username/ai-health-coach
cd ai-health-coach
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

---

👤 Author  
Meie Koning  
🔗 [LinkedIn](https://www.linkedin.com/in/meie-koning-59702a368/)  
📧 meie.koning@gmail.com