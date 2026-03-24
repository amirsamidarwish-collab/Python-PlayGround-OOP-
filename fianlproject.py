import tkinter as tk
from tkinter import font
import random
from openai import OpenAI
from config import API_KEY

BACKGROUND_COLOR = "black"
TEXT_COLOR = "white"
INPUT_BACKGROUND_COLOR = "#111"
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
FONT_FAMILY = "Helvetica"
FONT_SIZE = 14


class PythonPlayground:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Python Playground")
        self.root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
        self.root.configure(bg=BACKGROUND_COLOR)
        self.app_font = font.Font(family=FONT_FAMILY, size=FONT_SIZE)

        self.client = OpenAI(api_key=API_KEY)

        self.score = 0
        self.current_index = 0
        self.current_questions = []
        self.current_question = None
        self.language = "English"
        self.story_entry = None

        self.menu_frame = tk.Frame(self.root, bg=BACKGROUND_COLOR)
        self.explain_frame = tk.Frame(self.root, bg=BACKGROUND_COLOR)
        self.story_frame = tk.Frame(self.root, bg=BACKGROUND_COLOR)
        self.game_frame = tk.Frame(self.root, bg=BACKGROUND_COLOR)

        self.questions = self.build_questions()

        self.show_menu()

    def build_questions(self):
        easy_questions = [
            {"code": "x = 5\ny = 3\nprint(x + y)", "story": "Add 5 and 3."},
            {"code": "name = 'Tom'\nprint('Hi ' + name)", "story": "Say hi to Tom."},
            {"code": "for i in range(3):\n    print(i)", "story": "Count from 0 to 2."},
            {"code": "x = 2 * 4\nprint(x)", "story": "Multiply 2 and 4."},
            {"code": "x = 10\nx = x + 5\nprint(x)", "story": "Start at 10 and add 5."},
            {"code": "fruits = ['apple', 'banana']\nprint(fruits[0])", "story": "Print the first fruit."},
            {"code": "def hello():\n    print('Hi!')\nhello()", "story": "Say hi using a function."},
            {"code": "for i in [1,2,3]:\n    print(i*2)", "story": "Double each number."},
            {"code": "x = 3\nif x > 2:\n    print('big')", "story": "If 3 is big, print big."},
            {"code": "print(len('dog'))", "story": "Length of the word dog."}
        ]

        medium_questions = [
            {"code": "def square(x):\n    return x * x\nprint(square(3))", "story": "Return square of a number."},
            {"code": "def greet(name):\n    return 'Hello ' + name\nprint(greet('Dan'))", "story": "Greet Dan."},
            {"code": "nums = [1, 2, 3]\nprint(sum(nums))", "story": "Sum list of numbers."},
            {"code": "x = [1,2,3]\nx.append(4)\nprint(x)", "story": "Add 4 to list."},
            {"code": "x = { 'a': 1, 'b': 2 }\nprint(x['a'])", "story": "Print value of 'a' in dict."},
            {"code": "def add(a,b):\n    return a+b\nprint(add(2,3))", "story": "Add two numbers using function."},
            {"code": "s = 'hello'\nprint(s.upper())", "story": "Print word in upper case."},
            {"code": "x = 5\nif x > 3:\n    print('yes')\nelse:\n    print('no')", "story": "Check if 5 > 3 and print."},
            {"code": "for i in range(1,4):\n    print(i**2)", "story": "Print squares of 1 to 3."},
            {"code": "nums = [5,2,9]\nnums.sort()\nprint(nums)", "story": "Sort list and print."}
        ]

        hard_questions = [
            {"code": "class Dog:\n    def __init__(self, name):\n        self.name = name\n    def speak(self):\n        return self.name + ' says woof'\nd = Dog('Rex')\nprint(d.speak())", "story": "Create a dog and make it speak."},
            {"code": "class Cat:\n    def __init__(self, name):\n        self.name = name\n    def speak(self):\n        return self.name + ' meows'\nprint(Cat('Milo').speak())", "story": "Make Milo the cat meow."},
            {"code": "class Box:\n    def __init__(self):\n        self.items = []\n    def add(self, item):\n        self.items.append(item)\nb = Box()\nb.add('ball')\nprint(b.items)", "story": "Add ball to box using class."},
            {"code": "class Student:\n    def __init__(self, name):\n        self.name = name\ns = Student('Tom')\nprint(s.name)", "story": "Create a student named Tom."},
            {"code": "class Car:\n    def drive(self):\n        return 'Vroom!'\nprint(Car().drive())", "story": "Drive the car."},
            {"code": "class Book:\n    def __init__(self, title):\n        self.title = title\n    def read(self):\n        return 'Reading ' + self.title\nprint(Book('Python').read())", "story": "Read Python book."},
            {"code": "class Door:\n    def open(self):\n        return 'Open'\nd = Door()\nprint(d.open())", "story": "Open the door."},
            {"code": "class Hello:\n    def say(self):\n        return 'hi'\nprint(Hello().say())", "story": "Say hi from class."}
        ]

        questions_dict = {
            "easy": easy_questions,
            "medium": medium_questions,
            "hard": hard_questions
        }
        return questions_dict

    def reset_frames(self):
        self.menu_frame.pack_forget()
        self.explain_frame.pack_forget()
        self.story_frame.pack_forget()
        self.game_frame.pack_forget()

        for widget in self.menu_frame.winfo_children():
            widget.destroy()
        for widget in self.explain_frame.winfo_children():
            widget.destroy()
        for widget in self.story_frame.winfo_children():
            widget.destroy()
        for widget in self.game_frame.winfo_children():
            widget.destroy()

    def show_menu(self):
        self.reset_frames()
        self.menu_frame.pack(pady=50)

        label = tk.Label(self.menu_frame, text="Choose Mode:", font=self.app_font, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        label.pack(pady=10)

        btn1 = tk.Button(self.menu_frame, text="Explain Code", font=self.app_font, command=self.show_explain)
        btn1.pack(pady=10)

        btn2 = tk.Button(self.menu_frame, text="Story to Code", font=self.app_font, command=self.show_story)
        btn2.pack(pady=10)

        btn3 = tk.Button(self.menu_frame, text="Play Game", font=self.app_font, command=self.choose_language)
        btn3.pack(pady=10)

    def show_explain(self):
        self.reset_frames()
        self.explain_frame.pack(pady=10)

        label1 = tk.Label(self.explain_frame, text="Paste your Python code:", font=self.app_font, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        label1.pack()

        code_input = tk.Text(self.explain_frame, height=7, width=80, bg=INPUT_BACKGROUND_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, font=self.app_font)
        code_input.pack()

        label2 = tk.Label(self.explain_frame, text="Response language (e.g., English, Hebrew):", font=self.app_font, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        label2.pack()

        lang_input = tk.Text(self.explain_frame, height=1, width=40, bg=INPUT_BACKGROUND_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, font=self.app_font)
        lang_input.pack()

        label3 = tk.Label(self.explain_frame, text="Explanation:", font=self.app_font, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        label3.pack()

        output_text = tk.Text(self.explain_frame, height=10, width=80, bg=INPUT_BACKGROUND_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, font=self.app_font)
        output_text.pack()

        def explain():
            code = code_input.get("1.0", tk.END).strip()
            lang = lang_input.get("1.0", tk.END).strip()
            if lang == "":
                lang = "English"
            prompt = "Explain the following Python code in " + lang + " like a creative story for a child:\n" + code
            try:
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                result = response.choices[0].message.content
            except Exception as e:
                result = "Error: " + str(e)
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, result)

        btn_explain = tk.Button(self.explain_frame, text="Explain", command=explain, font=self.app_font)
        btn_explain.pack(pady=10)

        btn_back = tk.Button(self.explain_frame, text="Back to Menu", command=self.show_menu, font=self.app_font)
        btn_back.pack(pady=10)

    def show_story(self):
        self.reset_frames()
        self.story_frame.pack(pady=10)

        label1 = tk.Label(self.story_frame, text="Write your idea or story below:", font=self.app_font, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        label1.pack()

        story_input = tk.Text(self.story_frame, height=5, width=80, bg=INPUT_BACKGROUND_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, font=self.app_font)
        story_input.pack()

        label2 = tk.Label(self.story_frame, text="Response language (e.g., English, Hebrew):", font=self.app_font, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        label2.pack()

        lang_input = tk.Text(self.story_frame, height=1, width=40, bg=INPUT_BACKGROUND_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, font=self.app_font)
        lang_input.pack()

        label3 = tk.Label(self.story_frame, text="Generated Python Code:", font=self.app_font, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        label3.pack()

        output_text = tk.Text(self.story_frame, height=10, width=80, bg=INPUT_BACKGROUND_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, font=self.app_font)
        output_text.pack()

        def convert():
            story = story_input.get("1.0", tk.END).strip()
            lang = lang_input.get("1.0", tk.END).strip()
            if lang == "":
                lang = "English"
            prompt = "Write Python code from this story in " + lang + ". Simple explanation:\n" + story
            try:
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                result = response.choices[0].message.content
            except Exception as e:
                result = "Error: " + str(e)
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, result)

        btn_convert = tk.Button(self.story_frame, text="Convert to Python Code", command=convert, font=self.app_font)
        btn_convert.pack(pady=10)

        btn_back = tk.Button(self.story_frame, text="Back to Menu", command=self.show_menu, font=self.app_font)
        btn_back.pack(pady=10)

    def choose_language(self):
        self.reset_frames()
        self.menu_frame.pack(pady=50)

        label = tk.Label(self.menu_frame, text="Select Game Language:", font=self.app_font, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        label.pack(pady=10)

        btn_hebrew = tk.Button(self.menu_frame, text="Hebrew", font=self.app_font, command=self.start_hebrew)
        btn_hebrew.pack(pady=5)

        btn_english = tk.Button(self.menu_frame, text="English", font=self.app_font, command=self.start_english)
        btn_english.pack(pady=5)

    def start_hebrew(self):
        self.start_game_intro("Hebrew")

    def start_english(self):
        self.start_game_intro("English")

    def start_game_intro(self, lang):
        self.language = lang
        self.reset_frames()
        self.game_frame.pack(pady=10)

        if lang == "Hebrew":
            intro = "Game Mode:\nExplain the code like a story!\nPoints: 0-3"
        else:
            intro = "Game Mode:\nExplain the code like a fun story!\nPoints: 0-3 each round"

        label = tk.Label(self.game_frame, text=intro, font=self.app_font, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        label.pack(pady=10)

        btn_easy = tk.Button(self.game_frame, text="Easy", font=self.app_font, command=self.start_easy)
        btn_easy.pack()

        btn_medium = tk.Button(self.game_frame, text="Medium", font=self.app_font, command=self.start_medium)
        btn_medium.pack()

        btn_hard = tk.Button(self.game_frame, text="Hard", font=self.app_font, command=self.start_hard)
        btn_hard.pack()

    def start_easy(self):
        self.start_game("easy")

    def start_medium(self):
        self.start_game("medium")

    def start_hard(self):
        self.start_game("hard")

    def start_game(self, difficulty):
        self.current_questions = random.sample(self.questions[difficulty], len(self.questions[difficulty]))
        self.current_index = 0
        self.score = 0
        self.load_question()

    def load_question(self):
        self.reset_frames()
        self.game_frame.pack(pady=10)

        self.current_question = self.current_questions[self.current_index]

        label1 = tk.Label(self.game_frame, text="Write a story for this code:", font=self.app_font, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        label1.pack()

        label2 = tk.Label(self.game_frame, text=self.current_question["code"], font=self.app_font, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        label2.pack()

        self.story_entry = tk.Text(self.game_frame, height=3, width=60, bg=INPUT_BACKGROUND_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR)
        self.story_entry.pack()

        btn_submit = tk.Button(self.game_frame, text="Submit Answer", command=self.submit_answer, font=self.app_font)
        btn_submit.pack(pady=5)

        score_label = tk.Label(self.game_frame, text="Score: " + str(self.score), font=self.app_font, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        score_label.pack()

        btn_back = tk.Button(self.game_frame, text="Back to Menu", command=self.show_menu, font=self.app_font)
        btn_back.pack(pady=10)

    def submit_answer(self):
        user_story = self.story_entry.get("1.0", tk.END).strip().lower()
        correct = self.current_question["story"].lower()

        if user_story != "" and correct != "":
            if user_story in correct or correct in user_story:
                self.score = self.score + 3
            else:
                words = user_story.split()
                found = False
                for word in words:
                    if word in correct:
                        found = True
                if found:
                    self.score = self.score + 1

        self.next_question()

    def next_question(self):
        self.current_index = self.current_index + 1
        if self.current_index < len(self.current_questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        self.reset_frames()
        self.menu_frame.pack(pady=50)

        label = tk.Label(self.menu_frame, text="Game Over! Your final score: " + str(self.score), font=self.app_font, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
        label.pack(pady=10)

        btn_back = tk.Button(self.menu_frame, text="Back to Menu", command=self.show_menu, font=self.app_font)
        btn_back.pack()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = PythonPlayground()
    app.run()
