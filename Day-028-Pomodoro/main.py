from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
GREEN = "#3C6255"
MINT = "#61876E"
SAGE = "#A6BB8D"
DESERT = "#EAE7B1"
PINK = "#FA7070"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
CHECK_MARK = "✔"
check_mark_total = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global check_mark_total

    window.after_cancel(timer)
    
    timer_label.config(text="Timer", fg=DESERT)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark_total = ""
    check_label.config(text=check_mark_total, fg=SAGE)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = math.floor(WORK_MIN * 60)
    short_break_sec = math.floor(SHORT_BREAK_MIN * 60)
    long_break_sec = math.floor(LONG_BREAK_MIN * 60)

    #If it's the 1st/3rd/5th/7th rep:
    if reps % 2 == 1:
        timer_label.config(text="Focus", fg=DESERT)
        count_down(work_sec)

    #If it's the 8th rep:    
    elif reps % 8 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(long_break_sec)

    #If it's 2nd/4th/6th rep:
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=SAGE)
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global check_mark_total

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_mark_total += CHECK_MARK
            check_label.config(text=check_mark_total, fg=SAGE)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)


#Timer Label
timer_label = Label(text="Timer", fg=DESERT, bg=GREEN, font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=1, row=0)

#Buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

#Checkmarks
check_label = Label(fg=DESERT, bg=GREEN, font=(FONT_NAME, 15, "bold"))
check_label.grid(column=1, row=3)

window.mainloop()
