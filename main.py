from question_model import Question
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface
from menu import load_questions_from_file, split_questions_into_sets

from tkinter import Tk, Button, Label
from tkinter import Tk, Button, Label

THEME_COLOR = "#375362"

class MenuInterface:
    def __init__(self, question_sets):
        self.question_sets = question_sets
        self.root = Tk()
        self.root.title("Quiz Menu")

        # Display Title
        self.display_title()

        # Display quiz buttons
        self.display_quizzes()

        self.root.mainloop()

    def display_title(self):
        label = Label(self.root, text="Chọn một đề Kiểm Tra An Toàn:", font=("Arial", 20))
        label.grid(row=0, column=0, pady=20)

    def display_quizzes(self):
        for i, question_set in enumerate(self.question_sets):
            quiz_number = i + 1
            quiz_button = Button(self.root, text=f"Đề số {quiz_number}", font=("Arial", 14),
                                 command=lambda index=i: self.start_quiz(index))
            quiz_button.grid(row=i+1, column=0, padx=20, pady=10)

    def start_quiz(self, index):
        self.root.destroy()  # Close the menu window
        selected_question_set = self.question_sets[index]
        quiz = QuizBrain(selected_question_set)
        quiz_ui = QuizInterface(quiz)
        new_menu = MenuInterface(self.question_sets)  # Tạo một menu mới để chọn bài kiểm tra khác


def main():
    # Load question data from JSON file
    file_path = 'questions_bank.json'
    question_bank = load_questions_from_file(file_path)

    # Split question bank into sets with a fixed number of questions per set
    num_questions_per_set = 10
    question_sets = split_questions_into_sets(question_bank, num_questions_per_set)

    # Display menu and choose a quiz
    menu = MenuInterface(question_sets)

    print("You've completed the quiz.")

def main():
    # Load question data from JSON file
    file_path = 'questions_bank.json'
    question_bank = load_questions_from_file(file_path)

    # Split question bank into sets with a fixed number of questions per set
    num_questions_per_set = 10
    question_sets = split_questions_into_sets(question_bank, num_questions_per_set)

    # Display menu and choose a quiz
    menu = MenuInterface(question_sets)

    print("You've completed the quiz.")

if __name__ == "__main__":
    main()