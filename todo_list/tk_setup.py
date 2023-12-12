#!/usr/bin/env python3
"""
This file contains code for creating tkinter app
"""

import tkinter as tk
from tk_commands import *

root_win = tk.Tk()
root_win.configure(bg="blue")
root_win.geometry("1200x600")
root_win.title("TODO APP")

labels = [
    "Enter Task              : ",
    "Start Time(HH:MM:SS): ",
    "End Time(HH:MM:SS)  : "
]
for i, label_text in enumerate(labels):
    label = tk.Label(root_win, text=label_text)
    label.grid(row=i, column=0, sticky="w", pady=5)


large_font = ('Ariel', 16)
task_entry = tk.Entry(root_win,font=large_font)
task_entry.grid(row=0, column=1, sticky="w", pady=5)



start_time_entry = tk.Entry(root_win, font=(large_font))
start_time_entry.grid(row=1, column=1, sticky="w", pady=5)


end_time_entry = tk.Entry(root_win, font=(large_font))
end_time_entry.grid(row=2, column=1, sticky="w", pady=5)

create_task_button = tk.Button(root_win, text="CREATE TASK", command=create_task_command, bg="green")
create_task_button.grid(row=3, column=1, sticky="w", pady=2)

large_font = ('Ariel', 12)
show_tasks_entry = tk.Text(root_win, font=large_font, height=50, width=60)
show_tasks_entry.grid(row=5, column=0, sticky="nsew", pady=7)

show_tasks_button = tk.Button(root_win, text="Show tasks", command=read_tasks_command)
show_tasks_button.grid(row=4, column=0)


root_win.mainloop()