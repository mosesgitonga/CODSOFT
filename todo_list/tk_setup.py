#!/usr/bin/env python3.10
"""
This file contains code for creating tkinter app
"""

import tkinter as tk
from tk_commands import *
from crud import Crud

root_win = tk.Tk()
root_win.configure(bg="orange")
root_win.geometry("700x600")
root_win.title("TODO APP")

labels = [
    "Enter Task              : "

]
for i, label_text in enumerate(labels):
    label = tk.Label(root_win, text=label_text)
    label.grid(row=i, column=0, sticky="w", pady=5)


large_font = ('Ariel', 16)
task_entry = tk.Entry(root_win,font=large_font, bg="blue")
task_entry.grid(row=0, column=1, sticky="w", pady=5)

large_font = ('Ariel', 12)
show_tasks_entry = tk.Text(root_win, font=large_font, height=18, width=25, bg="blue")
show_tasks_entry.grid(row=5, column=2, sticky="w", pady=7)

crud = Crud()
def fetch_and_create_task():
    """
    create tasks
    """
    task = task_entry.get()
    show_tasks_entry.delete('1.0', tk.END)

    res = crud.create_task(task)
    
    show_tasks_entry.insert(tk.END, res)
   
def show_all_tasks():
    """
    show all tasks that have been saved
    """
    tasks_info = crud.read_tasks()
    
    show_tasks_entry.delete('1.0', tk.END)  
    show_tasks_entry.insert(tk.END, tasks_info)

def clear_tasks():
    """
    clear all task in storage
    """
    cleared = crud.clear_tasks()

    show_tasks_entry.delete('1.0', tk.END)  
    show_tasks_entry.insert(tk.END, cleared)


create_task_button = tk.Button(root_win, text="CREATE TASK", command=fetch_and_create_task, bg="green")
create_task_button.grid(row=3, column=1, sticky="w", pady=2)

show_tasks_button = tk.Button(root_win, text="Show tasks", command=show_all_tasks, bg="green")
show_tasks_button.grid(row=4, column=2)

clear_task_btn = tk.Button(root_win, text="Clear tasks", command=clear_tasks, bg="red")
clear_task_btn.grid(row=6, column=2)

root_win.mainloop()
