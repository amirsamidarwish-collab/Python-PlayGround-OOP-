<div align="center">

# Python Playground 🐍

**An AI-powered Python learning game built with Tkinter and GPT-3.5**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-412991?style=for-the-badge&logo=openai&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-informational?style=for-the-badge)
![University](https://img.shields.io/badge/Bar--Ilan_University-First_Year_Project-blue?style=for-the-badge)

</div>

---

## What is Python Playground?

A desktop learning app that teaches Python and OOP concepts through storytelling and AI — built as a first-year Computer Science project at Bar-Ilan University.

Instead of dry exercises, it turns code into stories. Users explain what code does in plain language, convert story ideas into real Python code, and play a quiz game — all powered by GPT-3.5.

---

## Modes

### 🎮 Game Mode
- Shows a Python code snippet
- User writes a "story" describing what the code does
- GPT scores the answer: 0–3 points per round
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

## Tech Stack

- **Python 3** — core language
- **Tkinter** — desktop GUI
- **OpenAI GPT-3.5** — AI explanations, scoring, and code generation
- **OOP architecture** — entire app built as a single class (`PythonPlayground`)

---

## OOP Concepts Demonstrated

This project was built to practice and demonstrate core OOP principles:

| Concept | Where Used |
|---|---|
| Classes & Objects | `PythonPlayground` class encapsulates entire app |
| `__init__` constructor | App state, frames, and OpenAI client initialized on startup |
| Instance methods | Each mode (`show_explain`, `show_story`, `start_game`) is a method |
| Instance variables | `self.score`, `self.language`, `self.current_question` etc. |
| Encapsulation | All UI and logic contained within the class |

---

## Project Structure

```
Python-PlayGround-OOP/
├── fianlproject.py   # Main application
├── config.py         # API key configuration (not committed)
└── README.md
```

---

## Setup

1. Clone the repo:
```bash
git clone https://github.com/amirsamidarwish-collab/Python-PlayGround-OOP.git
```

2. Install dependencies:
```bash
pip install openai
```

3. Create a `config.py` file with your OpenAI API key:
```python
API_KEY = "your-openai-api-key-here"
```

4. Run the app:
```bash
python fianlproject.py
```

---

## Screenshots

> Coming soon

---

## What I Learned

- Building a full desktop application with Tkinter
- Structuring a project using OOP — one class managing all state and logic
- Integrating the OpenAI API into a Python app
- Handling multilingual user input (Hebrew + English)
- Designing an interactive quiz engine with dynamic scoring

---

## About

Built by **Amir Samidarwish** as a first-year OOP final project at Bar-Ilan University (CS Honors Track).

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/amir-darwish-060b47282)

---

<div align="center">
<sub>First-year CS project — Bar-Ilan University, 2024</sub>
</div>
