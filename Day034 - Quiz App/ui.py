from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = "Arial"
FONT_SIZE = 20
FONT_STYLE = "italic"


class Quizinterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", background=THEME_COLOR, foreground="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.text_question = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Place holder",
            fill=THEME_COLOR,
            font=(FONT, FONT_SIZE, FONT_STYLE)
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        correct_button_img = PhotoImage(file=".\images\\true.png")
        self.correct_button = Button(
            image=correct_button_img,
            highlightthickness=0,
            command=self.true_pressed
        )
        self.correct_button.grid(row=2, column=1)

        incorrect_button_img = PhotoImage(file=".\images\\false.png")
        self.incorrect_button = Button(
            image=incorrect_button_img,
            highlightthickness=0,
            command=self.false_pressed
        )
        self.incorrect_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.resizable(width=False, height=False)
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_question, text=question_text)
        else:
            self.canvas.itemconfig(self.text_question, text="You've reached the end of the quiz.")
            self.correct_button.config(state='disabled')
            self.incorrect_button.config(state='disabled')
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

