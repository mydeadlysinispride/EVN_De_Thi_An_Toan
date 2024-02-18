from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
from quiz_brain import QuizBrain
from tkinter.ttk import Style, Scrollbar, Frame
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("ĐỀ Thi Thử An Toàn")
        # self.window.attributes('-fullscreen', True)

        # Hiển thị cửa sổ toàn màn hình
        # self.window.bind('<Configure>', self.on_window_configure)
        # Display Title
        self.display_title()

        # Creating a canvas for question text, and dsiplay question
        self.canvas = Canvas(width=1200, height=650)
        self.question_text = self.canvas.create_text(500, 100,
                                                     text="Question here",
                                                     width=700,
                                                     font=(
                                                         'Ariel', 17, 'italic')
                                                     )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()

        # Declare a StringVar to store user's answer
        self.user_answer = StringVar()

        # Create a frame to hold the radio buttons and add a scrollbar
        self.radio_frame = Frame(self.window)
        self.canvas.create_window(250, 200, window=self.radio_frame, anchor='nw')
        self.scrollbar = Scrollbar(self.radio_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Display four options(radio buttons)
        self.opts = self.radio_buttons()
        self.display_options()

        # To show whether the answer is correct or wrong
        self.feedback = Label(self.window, pady=10, font=("Arial", 14, "bold"))
        self.feedback.place(relx=0.25, rely=0.85, anchor='center')

        # Next and Submit Button
        self.buttons()

        # Mainloop
        self.window.mainloop()

    def on_window_configure(self, event):
        """Được gọi khi kích thước của cửa sổ thay đổi."""
        # Lấy kích thước mới của cửa sổ
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()

        # Căn chỉnh vị trí của các nút
        self.submit_button.place(relx=0.25, rely=0.9, anchor='center')
        self.next_button.place(relx=0.75, rely=0.9, anchor='center')
        self.quit_button.place(relx=0.9, rely=0.1, anchor='center')

    def display_title(self):
        """To display title"""
        # Title
        title = Label(self.window, text="ĐỀ THI Thử An Toàn",
                      width=100, bg="green", fg="white", font=("ariel", 20, "bold"))

        # place of the title
        title.place(x=0, y=2)

    def display_question(self):
        """To display the question"""
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        

    def radio_buttons(self):
        """Create four options (radio buttons)"""
        choice_list = []
        choices_labels = ['a', 'b', 'c', 'd']  # Danh sách các nhãn cho từng lựa chọn
        y_pos = 0

        for i in range(4):
            text = f"{choices_labels[i]}. "  # Thêm nhãn a, b, c, d
            radio_btn = Radiobutton(self.radio_frame, text=text, variable=self.user_answer,
                                    value='', font=("Arial", 15), wraplength=500, width=200, justify="left")
            radio_btn.pack(side="top", anchor="w")
            choice_list.append(radio_btn)

        return choice_list


    def display_options(self):
        """To display four options"""
        val = 0

        # deselecting the options
        self.user_answer.set(None)

        # List of characters for options (a, b, c, d)
        option_chars = ['a', 'b', 'c', 'd']

        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in self.quiz.current_question.choices:
            # Loại bỏ phần "A.", "B.", "C.", "D." từ mỗi lựa chọn
            if len(option) > 2 and option[1] == ".":
                option = option[3:]

            # Thêm ký tự a, b, c, d vào phía trước của mỗi lựa chọn
            option_with_char = f"{option_chars[val]}. {option}"

            self.opts[val]['text'] = option_with_char
            self.opts[val]['value'] = option
            self.opts[val]['wraplength'] = 800  # Set the maximum width for wrapping
            self.opts[val]['anchor'] = "w"
            self.opts[val]['justify'] = "left"
            val += 1


    def submit_btn(self):
        """Hiển thị phản hồi cho mỗi câu trả lời sau khi nhấn Trả lời"""
        selected_answer = self.user_answer.get()
        correct_answer = self.quiz.current_question.correct_answer

        # Kiểm tra xem câu trả lời có đúng hay không
        if selected_answer == correct_answer:
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Trả lời đúng! \U0001F44D'

            # Đổi màu sắc của đáp án đúng
            for opt in self.opts:
                if opt['value'] == correct_answer:  # Sử dụng 'value' thay vì 'text'
                    opt.config(fg="green")
        else:
            self.feedback['fg'] = 'red'
            self.feedback['text'] = 'Trả lời sai'

            # Đổi màu sắc của đáp án đúng và đáp án người dùng chọn
            for opt in self.opts:
                if opt['value'] == correct_answer:  # Sử dụng 'value' thay vì 'text'
                    opt.config(fg="green")
                elif opt['value'] == selected_answer:  # Sử dụng 'value' thay vì 'text'
                    opt.config(fg="red")
        # Cập nhật câu trả lời của người dùng trong quiz brain
        self.quiz.check_answer(selected_answer)


    def next_btn(self):
        """Chuyển đến câu hỏi tiếp theo"""
        if self.quiz.has_more_questions():
            # Đặt lại màu sắc của tất cả các radio button thành màu đen
            for opt in self.opts:
                opt.config(fg="black")

            # Chuyển đến câu tiếp theo và hiển thị tùy chọn của nó
            self.display_question()
            self.display_options()
            # Đặt lại phản hồi
            self.feedback.config(text="")
        else:
            # Nếu không còn câu hỏi nào nữa, thì hiển thị điểm số
            self.display_result()
            # Đóng cửa sổ
            self.window.destroy()

    def buttons(self):
        """To show next and submit buttons"""
        # The first button is the Submit button to check the answer
        self.submit_button = Button(self.window, text="Trả lời", command=self.submit_btn,
                                    width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))
        self.submit_button.place(relx=0.25, rely=0.9, anchor='center')

        # The second button is the Next button to move to the next Question
        self.next_button = Button(self.window, text="Câu tiếp", command=self.next_btn,
                                  width=10, bg="green", fg="white", font=("ariel", 16, "bold"))
        self.next_button.place(relx=0.75, rely=0.9, anchor='center')

        # The third button is the Quit button to close the window
        self.quit_button = Button(self.window, text="Quit", command=self.window.destroy,
                                  width=5, bg="red", fg="white", font=("ariel", 16, "bold"))
        self.quit_button.place(relx=0.9, rely=0.1, anchor='center')

    def display_result(self):
        """To display the result using messagebox"""
        correct, wrong, score_percent = self.quiz.get_score()

        correct = f"Trả Lời Chính Xác: {correct}"
        wrong = f"Tra Lời Sai: {wrong}"

        # calculates the percentage of correct answers
        result = f"Tổng Điểm: {score_percent}%"

        # create a themed style for the messagebox
        style = Style()
        style.theme_use('clam')  # you can choose a different theme here

        # Show a message box with the result
        messagebox.showinfo("Result", f"{result}\n{correct}\n{wrong}")


# Sample usage
# Assuming quiz_brain.py provides a QuizBrain class with necessary methods.
# quiz = QuizBrain()
# quiz_ui = QuizInterface(quiz)
