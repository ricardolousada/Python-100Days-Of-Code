# Created by Ricardo Lousada
from tkinter import *
import math
from gtts import gTTS
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- CREATE SOUND FILES ------------------------ #
sound_for_small_break = gTTS("Time for a small break.")
sound_for_small_break.save('small_break.mp3')


sound_for_big_break = gTTS("Time for a big break.")
sound_for_big_break.save('big_break.mp3')


sound_for_work = gTTS("Time to get back to work")
sound_for_work.save('work.mp3')

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    screen.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    tittle_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if it's the 8th rep
    if reps % 8 == 0:
        playsound('big_break.mp3')
        count_down(long_break_sec)
        tittle_label.config(text="Break", fg=RED)
    # if it's 2nd/4th/6th rep
    elif reps % 2 == 0:
        playsound('small_break.mp3')
        count_down(short_break_sec)
        tittle_label.config(text="Break", fg=PINK)
    # if it's the 1st/3rd/5rd rep
    else:
        playsound('work.mp3')
        tittle_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = screen.after(1000, count_down, count - 1)
    else:
        global reps
        print(reps)
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Pomodoro")
screen.config(padx=100, pady=50, bg=YELLOW)

tittle_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
tittle_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

screen.resizable(width=False,height=False)

screen.mainloop()
# text="✔"
