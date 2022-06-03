import math
import time
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
tick = "✅"
rep = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global rep
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    rep = 0
    check_mark.config(text="")
    label.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global rep, label
    if rep % 2 == 0:
        label.config(text="Work Time", fg=RED)
        time.sleep(1)
        count = WORK_MIN * 60
    else:
        if rep == 7:
            label.config(text="Long Break", fg=PINK)
            time.sleep(1)
            count = LONG_BREAK_MIN * 60
        elif rep == 8:
            count = 0
            label.config(text="Done", fg=RED)
            time.sleep(1)
            exit()
        else:
            count = SHORT_BREAK_MIN * 60
            label.config(text="Short Break", fg=PINK)
            time.sleep(1)

    rep += 1
    count_down(count)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min = int(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"  # Dynamic typing sec store's int previously but now stores string
    if min < 10:
        canvas.itemconfig(timer_text, text=f"0{min}:{sec}")
    else:
        canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(rep / 2)
        for _ in range(work_session):
            mark += tick
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window['bg'] = YELLOW
window.config(padx=100, pady=50)

image = PhotoImage(file="tomato.png")
canvas = Canvas(master=window, width=200, height=224, highlightthickness=0)
canvas.create_image(100, 112, image=image)
canvas['bg'] = YELLOW
timer_text = canvas.create_text(100, 112, text="00:00", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1, columnspan=6)

label = Label(window, text="TIMER", font=(FONT_NAME, 45, 'bold'))
label['bg'] = YELLOW
label.config(fg=GREEN)
label.grid(column=2, row=0, columnspan=4)

start = Button(window, text="Start", font=(FONT_NAME, 15, "bold"), command=start_timer)
start.grid(column=0, row=3)

check_mark = Label(window, background=YELLOW)
check_mark.grid(column=3, row=3)

reset = Button(window, text="Reset", font=(FONT_NAME, 15, "bold"), command=reset_timer)
reset.grid(column=9, row=3)

window.mainloop()
