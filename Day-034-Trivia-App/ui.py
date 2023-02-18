from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
GREEN = "#058C42"
RED = "#7B0D1E"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas.config(highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Question Goes Here",
            fill=THEME_COLOR,
            font=("Arial", 14, "italic"),
            width=280
            )

        #Score label
        self.score_label = Label(text="Score: 0", highlightthickness=0, bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        #Button Images
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        #Buttons
        self.true_button = Button(image=true_image, highlightthickness=0, borderwidth=0, command=self.set_answer_true)
        self.true_button.grid(column=0, row=3)

        self.false_button = Button(image=false_image, highlightthickness=0, borderwidth=0, command=self.set_answer_false)
        self.false_button.grid(column=1, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def set_answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def set_answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg=GREEN)
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(bg=RED)
            self.canvas.itemconfig(self.question_text, fill="white")

        self.window.after(1000, self.get_next_question)
        