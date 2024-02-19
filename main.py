import random
from question_model import Question
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface
from menu import load_questions_from_file
from tkinter import Tk, Button, Label, Scrollbar, Canvas, Frame

THEME_COLOR = "#375362"

class MenuInterface:
    def __init__(self, question_bank):
        self.question_bank = question_bank
        self.root = Tk()
        self.root.title("Thi An toan EVN")

        # Create a canvas with a scrollbar
        self.canvas = Canvas(self.root)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar = Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame = Frame(self.canvas)  # Create a frame inside the canvas
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        # Display Title
        self.display_title()

        # Display quiz button
        self.display_quiz()

        # Update canvas scroll region after adding widgets
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        self.root.mainloop()


    def display_title(self):
        label = Label(self.frame, text="Chọn một đề Kiểm Tra An Toàn:", font=("Times New Roman", 20))
        label.grid(row=0, column=0, pady=20)

    def display_quiz(self):
        quiz_button = Button(self.frame, text="Bắt đầu bài kiểm tra", font=("Times New Roman", 14),
                             command=self.start_quiz)
        quiz_button.grid(row=1, column=0, padx=20, pady=10)

    def start_quiz(self):
        self.root.destroy()  # Close the menu window
        selected_questions = random.sample(self.question_bank, 70)  # Chọn ngẫu nhiên 70 câu hỏi
        quiz = QuizBrain(selected_questions)
        quiz_ui = QuizInterface(quiz)

def main():
    # Load question data from JSON file
    file_path = 'questions_bank.json'
    question_bank = load_questions_from_file(file_path)

    # Display menu and choose a quiz
    menu = MenuInterface(question_bank)

    print("You've completed the quiz.")


if __name__ == "__main__":
    main()
