from tkinter import *
import math

import datashape.validation
from gtts import gTTS
from playsound import playsound
import pandas as pd
import random

# ---------------------------- CONSTANTS ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"
SMALL_FONT_SIZE = 40
LARGE_FONT_SIZE = 60
SMALL_FONT_STYLE = "italic"
LARGE_FONT_STYLE = "bold"
ROTATION_TIME = 3000
current_index = 0
list_of_words = []


# --------------------- OPEN DATA FILE ------------------------ #

def open_data_file():
    try:
        data = pd.read_csv(".\data\words_to_learn.csv")
    except:
        data = pd.read_csv(".\data\\french_words.csv")
    global list_of_words
    list_of_words = data.to_dict(orient="records")
    print(type(list_of_words))
    generate_random_word(list_of_words)
    # print(data_dict)


# -------------------  GENERATE RANDOM WORD  ------------------ #

def generate_random_word(data_list):
    random_index = random.randint(0, len(data_list) - 1)
    global current_index
    current_index = random_index
    french_word = data_list[current_index]["French"]
    english_word = data_list[current_index]["English"]
    # print(french_word)
    # print(english_word)
    write_random_word(french_word, english_word, "French")


# ---------------  WRITE WORD TO THE CANVAS  ---------------- #

def write_random_word(french_word, english_word, main_language):
    canvas.itemconfig(canvas_image, image=front_flash_card_img)
    correct_button.config(state="disabled")
    incorrect_button.config(state="disabled")
    canvas.itemconfig(small_word, text=main_language, fill="black")
    canvas.itemconfig(big_word, text=french_word, fill="black")
    window.after(3000, flip_card, "English", english_word)


# ------------------ FLIPS THE CARD------------------------------- #
def flip_card(main_language, english_word):
    correct_button.config(state="active")
    incorrect_button.config(state="active")
    canvas.itemconfig(canvas_image, image=back_flash_card_img)
    canvas.itemconfig(small_word, text=main_language, fill="white")
    canvas.itemconfig(big_word, text=english_word, fill="white")


# ----------------------BUTTON FUNCTIONS  --------------------- #
def correct_answer():
    global list_of_words
    # print(current_index)
    list_of_words.remove(list_of_words[current_index])
    data_frame = pd.DataFrame(list_of_words)
    # print(data_frame)
    data_frame.to_csv(".\data\words_to_learn.csv", index="false")
    generate_random_word(list_of_words)


def incorrect_answer():
    global list_of_words
    generate_random_word(list_of_words)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, )

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
front_flash_card_img = PhotoImage(file=".\images\card_front.png")
back_flash_card_img = PhotoImage(file=".\images\card_back.png")
canvas_image = canvas.create_image((400, 263), image=front_flash_card_img)
small_word = canvas.create_text(400, 150, text="", font=(FONT, SMALL_FONT_SIZE, SMALL_FONT_STYLE))
big_word = canvas.create_text(400, 263, text="", font=(FONT, LARGE_FONT_SIZE, LARGE_FONT_STYLE))
canvas.grid(row=0, column=0, columnspan=2)

# timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.grid(row=1, column=1)

correct_button_img = PhotoImage(file=".\images\\right.png")
correct_button = Button(image=correct_button_img, highlightthickness=0, state="disabled", command=correct_answer)
correct_button.grid(row=1, column=1)

incorrect_button_img = PhotoImage(file=".\images\wrong.png")
incorrect_button = Button(image=incorrect_button_img, highlightthickness=0, state="disabled", command=incorrect_answer)
incorrect_button.grid(row=1, column=0)

open_data_file()

window.resizable(width=False, height=False)

window.mainloop()
