from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("ĐỀ THI Thử An Toàn")
        self.window.geometry("850x700")

        # Display Title
        self.display_title()

        # Creating a canvas for question text, and dsiplay question
        self.canvas = Canvas(width=800, height=250)
        self.question_text = self.canvas.create_text(400, 125,
                                                     text="Question here",
                                                     width=680,
                                                     fill=THEME_COLOR,
                                                     font=(
                                                         'Ariel', 15, 'italic')
                                                     )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()

        # Declare a StringVar to store user's answer
        self.user_answer = StringVar()

        # Display four options(radio buttons)
        self.opts = self.radio_buttons()
        self.display_options()

        # To show whether the answer is correct or wrong
        self.feedback = Label(self.window, pady=10, font=("ariel", 15, "bold"))
        self.feedback.place(x=300, y=380)

        # Next and Submit Button
        self.buttons()

        # Mainloop
        self.window.mainloop()

    def display_title(self):
        """To display title"""
        # Title
        title = Label(self.window, text="ĐỀ THI Thử An Toàn",
                      width=50, bg="green", fg="white", font=("ariel", 20, "bold"))

        # place of the title
        title.place(x=0, y=2)

    def display_question(self):
        """To display the question"""
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def radio_buttons(self):
        """To create four options (radio buttons)"""
        # initialize the list with an empty list of options
        choice_list = []

        # position of the first option
        y_pos = 230

        # Gap between radio buttons vertically
        y_gap = 90

        # adding the options to the list
        while len(choice_list) < 4:
            # setting the radio button properties
            radio_btn = Radiobutton(self.window, text="", variable=self.user_answer,
                                    value='', font=("ariel", 14), wraplength=600)

            # adding the button to the list
            choice_list.append(radio_btn)

            # placing the button
            radio_btn.place(x=100, y=y_pos)

            # incrementing the y-axis position by 40
            y_pos += y_gap

        # return the radio buttons
        return choice_list

    def display_options(self):
        """To display four options"""
        val = 0

        # deselecting the options
        self.user_answer.set(None)

        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in self.quiz.current_question.choices:
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            self.opts[val]['wraplength'] = 500  # Set the maximum width for wrapping
            self.opts[val]['anchor'] = "w"
            self.opts[val]['justify'] = "left"
            val += 1

    def submit_btn(self):
        """To show feedback for each answer after submitting"""
        if self.quiz.check_answer(self.user_answer.get()):
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Trả lời đúng! \U0001F44D'
        else:
            correct_answer = self.quiz.current_question.correct_answer
            self.feedback['fg'] = 'red'
            self.feedback['text'] = f'Sai! Đáp án đúng: {correct_answer}'
        self.feedback.place(x=200, y=560)

    def next_btn(self):
        """To move to the next question"""
        if self.quiz.has_more_questions():
            # Moves to next to display next question and its options
            self.display_question()
            self.display_options()
            # Reset feedback label
            self.feedback.config(text="")
        else:
            # if no more questions, then it displays the score
            self.display_result()
            # destroys the self.window
            self.window.destroy()

    def buttons(self):
        """To show next and submit buttons"""
        # The first button is the Submit button to check the answer
        submit_button = Button(self.window, text="Trả lời", command=self.submit_btn,
                              width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))
        submit_button.place(x=200, y=600)

        # The second button is the Next button to move to the next Question
        next_button = Button(self.window, text="Câu tiếp", command=self.next_btn,
                             width=10, bg="green", fg="white", font=("ariel", 16, "bold"))
        next_button.place(x=550, y=600)

        # The third button is the Quit button to close the window
        quit_button = Button(self.window, text="Quit", command=self.window.destroy,
                             width=5, bg="red", fg="white", font=("ariel", 16, "bold"))
        quit_button.place(x=750, y=50)

    def display_result(self):
        """To display the result using messagebox"""
        correct, wrong, score_percent = self.quiz.get_score()

        correct = f"Correct: {correct}"
        wrong = f"Wrong: {wrong}"

        # calculates the percentage of correct answers
        result = f"Score: {score_percent}%"

        # Shows a message box to display the result
        messagebox.showinfo("Result", f"{result}\n{correct}\n{wrong}")


# Sample usage
# Assuming quiz_brain.py provides a QuizBrain class with necessary methods.
# quiz = QuizBrain()
# quiz_ui = QuizInterface(quiz)
