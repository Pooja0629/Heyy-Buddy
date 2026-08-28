# 🎙️ Heyy Buddy – Voice-Controlled Web Assistant

## 📑 Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Technology Stack](#technology-stack)
* [Installation](#installation)
* [Usage](#usage)
* [API Documentation](#api-documentation)
* [Project Structure](#project-structure)
* [Deployment](#deployment)
* [Future Improvements](#future-improvements)
* [License](#license)
* [Contact](#contact)

---

## 📌 Overview

Heyy Buddy is a voice-controlled web assistant that allows users to perform common web actions using voice commands. It uses the browser's Web Speech API to recognize speech and a Flask backend to process commands.

The assistant can open websites, search and play YouTube videos, and create Gmail email drafts through simple voice instructions.

---

## 🚀 Features

### 🎙️ Voice Commands

* Speech-to-text using Web Speech API
* Real-time voice recognition and status updates
* Interactive microphone and voice visualizer

### 🎵 YouTube Control

* Search and play YouTube videos using voice commands
* Automatically generates the requested video URL

### 📧 Gmail Integration

* Create Gmail email drafts using voice commands
* Automatically detects recipient and email content

### 🎨 Modern UI

* Glassmorphism-inspired interface
* Animated microphone and background effects
* Responsive design

---

## 🛠️ Technology Stack

### 🎨 Frontend

* HTML5
* CSS3
* JavaScript
* Web Speech API

### ⚙️ Backend

* Python
* Flask

### ☁️ Deployment

* Render

---

## ⚙️ Installation

### 🔧 Prerequisites

* Python 3.9+
* Git
* Google Chrome / Microsoft Edge

### 🚀 Steps

```bash
# Clone the repository
git clone https://github.com/Pooja0629/Heyy-Buddy.git

# Navigate to project
cd Heyy-Buddy

# Install dependencies
pip install flask

# Run application
python app.py
```

Open in browser:

```text
http://localhost:8000
```

---

## 📖 Usage

1. Open the application.
2. Click the microphone button.
3. Allow microphone access.
4. Speak a command.

### Example Commands

```text
"Open YouTube and play Karuppu song"
"Email john at gmail.com type hello"
"Open Google"
```

---

## 📡 API Documentation

### 🤖 Agent Endpoint

| **Method** | **Endpoint** | **Description**          |
| ---------- | ------------ | ------------------------ |
| POST       | `/agent`     | Processes voice commands |

### 📥 Request

```json
{
    "command": "Open YouTube and play Karuppu song"
}
```

### 📤 Response

```json
{
    "success": true,
    "message": "Playing karuppu song",
    "url": "https://www.youtube.com/embed/..."
}
```

---

## 📁 Project Structure

```text
Heyy-Buddy/
│
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🌐 Deployment

### 🔗 Live Demo

**Render:** https://agentic-ai-9dai.onrender.com/

🎙️ *Allow microphone access in the browser to use voice commands.*

---

## 🚀 Future Improvements

* AI-powered natural language command processing
* Text-to-speech responses
* More website integrations
* Calendar and reminder commands
* Multi-language support

---

## 👩‍💻 Contact

**Pooja S**

AI & Data Science Student

📧 Email: [poojashree2266@gmail.com](mailto:poojashree2266@gmail.com)

🔗 GitHub: https://github.com/Pooja0629

---

✨ *“Turning your voice into simple web actions with Heyy Buddy.”*
