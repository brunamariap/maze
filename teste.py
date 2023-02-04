from random import randint
from tkinter import *

MS_DELAY = 500  # Milliseconds between updates.

window = Tk()
text1 = StringVar()

def gpio_read():
    """ Simulate GPIO READ. """
    return randint(0, 3)

def check_condition():
    if gpio_read() == 0:
        text1.set("IN Button Pressed.Loading Camera.")
    else:
        text1.set("Waiting for Button Press...")

    window.after(MS_DELAY, check_condition)  # Schedule next check.

lbl = Label(window, textvariable=text1)  # Link to StringVar's value.
lbl.pack()

window.after(MS_DELAY, check_condition)  # Schedule first check.
window.mainloop()