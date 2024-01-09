from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global REPS
    checkmarks.config(text="")
    title_Label.config(text="Timer", font=(FONT_NAME, 36), bg=YELLOW, fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    REPS = 0
    window.after_cancel(TIMER)
    
    

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN & 60
    REPS += 1
    if REPS % 8 == 0:
        count_down(long_sec)
        title_Label.config(text="Long Break", bg=YELLOW, fg=RED)
    elif REPS % 2 == 0:
        count_down(short_sec)
        title_Label.config(text="Short Break", bg=YELLOW, fg=PINK)
    else:
        count_down(work_sec)
        title_Label.config(text="Work", bg=YELLOW, fg=GREEN)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global TIMER
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(REPS/2)):
            mark += CHECKMARK
        checkmarks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_Label = Label(text="Timer", font=(FONT_NAME, 36), bg=YELLOW, fg=GREEN)
title_Label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file=r"Pomodoro\tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(row=1, column=1)

start_Button = Button(text="Start", command=start_timer, highlightthickness=0)
start_Button.grid(row=2, column=0)

reset_Button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_Button.grid(row=2, column=2)

checkmarks = Label(text="", highlightthickness=0, bg=YELLOW, fg=GREEN)
checkmarks.grid(row=3, column=1)


window.mainloop()
