import tkinter as tk
from PIL import Image, ImageTk
from quiz_brain import QuizBrain


class QuizUI:
    # ------------------ CONSTANTS ------------------
    BACKGROUND_NAVY = "#053050"
    CARD_WIDTH = 700
    CARD_HEIGHT = 450

    QUESTION_FONT = ("Arial", 28, "bold")
    SMALL_FONT = ("Arial", 16)

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quiz Master")
        self.window.geometry("1000x600")
        self.window.config(bg=self.BACKGROUND_NAVY)

        # Example data (replace later with QuizBrain)
        self.question_text = (
            "The python language was named after a snake.\nTrue or False?"
        )
        self.question_number = 1
        self.score = self.quiz.score

        self._create_main_card()
        self._create_score_pill()
        self.q_txt = self._create_question_text()
        self._create_answer_buttons()
        self.get_next_question()

        self.window.mainloop()

    # ------------------ HELPERS ------------------
    def create_rounded_rect(self, canvas, x1, y1, x2, y2, r, **kwargs):
        points = [
            x1 + r, y1, x2 - r, y1,
            x2, y1, x2, y1 + r,
            x2, y2 - r, x2, y2,
            x2 - r, y2, x1 + r, y2,
            x1, y2, x1, y2 - r,
            x1, y1 + r, x1, y1
        ]
        return canvas.create_polygon(points, smooth=True, **kwargs)

    # ------------------ MAIN CARD ------------------
    def _create_main_card(self):
        self.card = tk.Canvas(
            self.window,
            width=self.CARD_WIDTH,
            height=self.CARD_HEIGHT,
            bg=self.BACKGROUND_NAVY,
            highlightthickness=0
        )
        self.card.place(relx=0.5, rely=0.5, anchor="center")

        self.create_rounded_rect(
            self.card,
            10, 10,
            self.CARD_WIDTH - 10,
            self.CARD_HEIGHT - 10,
            r=40,
            fill="white"
        )

        # Question counter
        self. question_num = self.card.create_text(
            40, 40,
            text=f"Question: {self.question_number}/10",
            font=self.SMALL_FONT,
            fill="black",
            anchor="w"
        )

    # ------------------ SCORE PILL ------------------
    def _create_score_pill(self):
        self.score_canvas = tk.Canvas(
            self.window,
            width=140,
            height=50,
            bg=self.BACKGROUND_NAVY,
            highlightthickness=0
        )
        self.score_canvas.place(relx=0.68, rely=0.06)

        # Shadow
        self.create_rounded_rect(
            self.score_canvas,
            7, 7, 137, 47,
            r=25,
            fill="#c9d6dd",
            outline=""
        )

        # Main pill
        self.create_rounded_rect(
            self.score_canvas,
            5, 5, 135, 45,
            r=25,
            fill="white",
            outline=""
        )

        # Score text
        self.score_text = self.score_canvas.create_text(
            70, 25,
            text=f"Score: {self.score}",
            font=self.SMALL_FONT,
            fill="black"
        )

    # ------------------ QUESTION TEXT ------------------
    def _create_question_text(self):
        return self.card.create_text(
            self.CARD_WIDTH / 2,
            160,
            text=self.question_text,
            font=self.QUESTION_FONT,
            fill="black",
            width=600,
            justify="center"
        )

    # ------------------ TRUE / FALSE BUTTONS ------------------
    def _create_answer_buttons(self):
        # TRUE
        true_img = Image.open("./34_Quiz GUI/images/true.png").resize((140, 140))
        self.true_photo = ImageTk.PhotoImage(true_img)

        true_btn = tk.Button(
            image=self.true_photo,
            bg="white",
            activebackground="white",
            borderwidth=0,
            command=self.true_pressed
        )
        self.card.create_window(230, 330, window=true_btn)

        # FALSE
        false_img = Image.open("./34_Quiz GUI/images/false.png").resize((140, 140))
        self.false_photo = ImageTk.PhotoImage(false_img)

        false_btn = tk.Button(
            image=self.false_photo,
            bg="white",
            activebackground="white",
            borderwidth=0,
            command=self.false_pressed
        )
        self.card.create_window(470, 330, window=false_btn)

    # ------------------ BUTTON HANDLERS ------------------
    def true_pressed(self):
        if self.quiz.still_has_questions():
            self.quiz.check_answer("True")
            self.score_canvas.itemconfig(self.score_text, text= f"Score: {self.quiz.score}")
            self.card.itemconfig(self.question_num, text= f"Question: {self.quiz.question_number}/10")
            self.get_next_question()
        else:
            self.card.itemconfig(self.q_txt,text=f"Final Result: {self.quiz.score}/10")
    def false_pressed(self):
        if self.quiz.still_has_questions():
            self.quiz.check_answer("False")
            self.score_canvas.itemconfig(self.score_text, text= f"Score: {self.quiz.score}")
            self.card.itemconfig(self.question_num, text= f"Question: {self.quiz.question_number}/10")
            self.get_next_question()
        else:
            self.card.itemconfig(self.q_txt,text=f"Final Result: {self.quiz.score}/10")
        
    def get_next_question(self):
        question_txt = self.quiz.next_question()
        self.card.itemconfig(self.q_txt,text=question_txt)



