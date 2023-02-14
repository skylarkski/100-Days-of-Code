import random
from tkinter import *
import os
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Ariel'
current_card = {}
# ----------------- DATA SETUP --------------------

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
except pd.errors.EmptyDataError:
    data = pd.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")


# ----------------- SAVE PROGRESS -----------------
def all_learned():
    next_card()

# ----------------- REMOVE WORD AND SAVE ----------
def remove_word():
    global current_card
    to_learn.remove(current_card)
    data = pd.DataFrame.from_dict(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


# ----------------- GENERATE WORD -----------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    
    try:
        current_card = random.choice(to_learn)
    except IndexError:
        canvas.itemconfig(card_title, text="You learned them all!", fill="black",  font=(FONT_NAME, 40, "bold"))
        canvas.itemconfig(card_word, text='Congratulations!', fill="black")
        canvas.itemconfig(canvas_image, image=card_front_image)
        known_button.config(command=next_card)
        unknown_button.config(command=next_card)
    else:
        canvas.itemconfig(card_title, text=current_card['French'], fill="black")
        canvas.itemconfig(card_word, text='French', fill="black")
        canvas.itemconfig(canvas_image, image=card_front_image)

        flip_timer = window.after(3000, flip_card)

# ----------------- FLIP CARD -----------------
def flip_card():
    canvas.itemconfig(card_title, text=current_card['English'], fill="white")
    canvas.itemconfig(card_word, text='English', fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image)

# ----------------- UI SETUP -----------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

#Images
check_image = PhotoImage(file="images/right.png")
cross_image = PhotoImage(file="images/wrong.png")
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

#Canvas
canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_word = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"))
card_title = canvas.create_text(400, 263, text="word", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#Buttons
known_button = Button(image=check_image, highlightthickness=0, command=remove_word)
known_button.grid(column=1, row=1)
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

next_card()




window.mainloop()