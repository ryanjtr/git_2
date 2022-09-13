from itertools import count
from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
mark_checker = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def timer_start():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60
    if reps % 2 == 0 and reps < 8 and reps > 0:
        count_down(short_break_time)
        timer_label.config(text="BREAK", fg=RED)
    elif reps % 8 == 0:
        count_down(long_break_time)
        timer_label.config(text="BREAK", fg=RED)
    else:
        count_down(work_time)
        timer_label.config(text="WORK", fg=RED)


def reset_time():
    global mark_checker
    global reps
    window.after_cancel(timer)
    timer_label.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    mark_checker = ""
    reps = 0
    tick_label.config(text=mark_checker)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global mark_checker
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_start()
        for _ in range(math.floor(reps / 2)):
            mark_checker += "✔"
        tick_label.config(text=mark_checker)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.after(1000)
timer_label = Label(text="TIMER", font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
timer_label.grid(columns=5, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=False)
tomato = PhotoImage(file="F:\Code python\Day28/tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=timer_start)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=reset_time)
reset_button.grid(column=4, row=2)

tick_label = Label(text=mark_checker, font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
tick_label.grid(column=1, row=3)
window.mainloop()
