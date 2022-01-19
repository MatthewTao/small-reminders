"""
File that contains the GUI definition
"""
import tkinter as tk
from datetime import datetime
from functools import partial

from reminders import Reminders


def check_action_due(reminder):
    action_info = reminder.check_action_due()
    lbl_last_drink['text'] = 'Last drink was ' + action_info['time_since_drink'] + ' hours ago'
    lbl_last_move['text'] = 'Last move was ' + action_info['time_since_move'] + ' hours ago '
    
    if action_info['drink_due']:
        lbl_last_drink['foreground']='red'
    else:
        lbl_last_drink['foreground']='white'
    
    if action_info['move_due']:
        lbl_last_move['foreground']='red'
    else:
        lbl_last_move['foreground']='white'

    window.after(1000 * 60, check_action_due, reminder)


def drink(reminder):
    reminder.take_drink()
    window.after(1, check_action_due, reminder)


def move(reminder):
    reminder.move_about()
    window.after(1, check_action_due, reminder)


reminder_instance = Reminders()

# Set-up the window
window = tk.Tk()
window.title("Small Reminders")
window["bg"] = "black"

# Establish frames
frm_datetime = tk.Frame(master=window)
lbl_time = tk.Label(
    master=frm_datetime,
    text="",
    font=("Consolas", 25),
    foreground="white",
    background="black")
lbl_last_drink = tk.Label(
    master=frm_datetime,
    text='',
    font=("Consolas", 15),
    foreground="white",
    background="black")
lbl_last_move = tk.Label(
    master=frm_datetime,
    text='',
    font=("Consolas", 15),
    foreground="white",
    background="black")

bt_drink = tk.Button(window, text ="Drink", command = partial(drink, reminder_instance))
bt_move = tk.Button(window, text ="Move", command = partial(move, reminder_instance))

# Fill frames
lbl_last_move.pack()
lbl_last_drink.pack()
frm_datetime.grid(row=0, column=0, columnspan=2)
bt_drink.grid(row=1, column=0, sticky='NESW')
bt_move.grid(row=1, column=1, sticky='NESW')


# Run the application
window.after(1, check_action_due, reminder_instance)

# Show GUI
window.mainloop()
