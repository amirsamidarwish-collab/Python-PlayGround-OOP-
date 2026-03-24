<div align="center">

# Python Playground 🐍

**An AI-powered Python learning game built with Tkinter and GPT-3.5**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-412991?style=for-the-badge&logo=openai&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-informational?style=for-the-badge)
![University](https://img.shields.io/badge/Bar--Ilan_University-OOP_Course_Project-blue?style=for-the-badge)

</div>

---

## What is Python Playground?

I built this as my final project for the OOP course at Bar-Ilan University. The idea was simple — instead of learning Python through boring exercises, why not turn code into stories?

Python Playground is a desktop app where you can explain what code does in plain language, convert story ideas into real Python code, and play a quiz game. All powered by GPT-3.5 under the hood.

---

## Modes

### 🎮 Game Mode
- Shows a Python code snippet
- You write a "story" describing what the code does
- Scores your answer: 0–3 points per round
- Three difficulty levels: Easy, Medium, Hard
- Supports Hebrew and English

### 🤖 Explain Mode
- Paste any Python code
- GPT explains it like a creative story for a child
- Choose your explanation language (English, Hebrew, etc.)

### ✍️ Story to Code Mode
- Write any idea or story in plain language
- GPT converts it into working Python code
- Supports multiple languages

---

## OOP Concepts Demonstrated

The whole app is structured as a single class — `PythonPlayground`. Here's what I used:

| Concept | Where Used |
|---|---|
| Classes & Objects | `PythonPlayground` class encapsulates the entire app |
| `__init__` constructor | App state, frames, and OpenAI client initialized on startup |
| Instance methods | Each mode (`show_explain`, `show_story`, `start_game`) is a method |
| Instance variables | `self.score`, `self.language`, `self.current_question` etc. |
| Encapsulation | All UI and logic contained within the class |

---

## How to Run It

### 1. Clone the repo
```bash
git clone https://github.com/amirsamidarwish-collab/Python-PlayGround-OOP.git
cd Python-PlayGround-OOP
```

### 2. Install dependencies

Install the OpenAI library:
```bash
pip install openai
```

Install Tkinter (if not already installed):
```bash
# On Windows — usually comes with Python by default
# On Mac:
brew install python-tk
# On Linux:
sudo apt-get install python3-tk
```

> Make sure Tkinter is also recognized in your IDE. In PyCharm or VS Code, just make sure your Python interpreter has it available. You can test it by running `import tkinter` in the terminal — if no error, you're good.

### 3. Create your config file

The API key is **not included** in this repo for security reasons. You need to create a file called `config.py` in the same folder as `fianlproject.py` and add this:

```python
API_KEY = "your-openai-api-key-here"
```

Get your API key from: https://platform.openai.com/api-keys

### 4. Run the app
```bash
python fianlproject.py
```

---

## Project Structure

```
Python-PlayGround-OOP/
├── fianlproject.py   # Main application
├── config.py         # Your API key — create this yourself, not committed
└── README.md
```

---

## What I Learned Building This

- How to structure a full desktop app using OOP — one class managing all state, UI, and logic
- Integrating the OpenAI API into a real Python project
- Building GUIs with Tkinter — frames, buttons, text inputs, layouts
- Handling multilingual input (Hebrew + English) in the same app
- Designing a quiz engine with dynamic scoring logic

---

## About

I'm Amir Samidarwish — I wrote this project for my OOP course at Bar-Ilan University. It was one of my first times combining AI APIs with a desktop GUI, and honestly a fun way to learn OOP by actually building something.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/amir-darwish-060b47282)

---

<div align="center">
<sub>OOP Course Final Project — Bar-Ilan University, 2024</sub>
</div>
