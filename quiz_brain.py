class QuizBrain:
    def __init__(self, questions):
        self.question_no = 0
        self.score = 0
        self.questions = questions
        self.current_question = None
        self.wrong_answers = []

    def has_more_questions(self):
        """Check if the quiz has more questions"""
        return self.question_no < len(self.questions)

    def next_question(self):
        """Get the next question by incrementing the question number"""
        self.current_question = self.questions[self.question_no]
        self.question_no += 1
        q_text = self.current_question.question_text
        return f"Q.{self.question_no}: {q_text}"

    def check_answer(self, user_answer):
        """Check the user answer against the correct answer and maintain the score"""
        correct_answer = self.current_question.correct_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            self.record_wrong_answer()
            return False

    def record_wrong_answer(self):
        """Record the wrong answer"""
        self.wrong_answers.append(self.current_question)

    def get_score(self):
        """Get the number of correct answers, wrong answers, and score percentage"""
        total_questions = len(self.questions)
        wrong = len(self.wrong_answers)
        score_percent = (self.score / total_questions) * 100 if total_questions > 0 else 0
        return self.score, wrong, score_percent
