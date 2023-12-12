#!/usr/bin/env python3
"""
This file contains commands for tkinter app
"""
import tkinter
from crud import Crud

def create_task_command(task, start_time, end_time):
    """create task and set time to it"""
    crud = Crud()
    return crud.create_task(task, start_time, end_time)
"""
def read_tasks_command():
    read tasks available in the self.tasks list
    and see remaining time for the task to start
    
    #crud = Crud()
    #return crud.read_tasks()
    """

def read_tasks_command():
    # Assuming 'crud' is an instance of your Crud class
    tasks_info = Crud.read_tasks()  # Fetch tasks from your Crud class method
    
    if tasks_info:
        # Clear the current content in the Text widget
        show_tasks_entry.delete('1.0', tk.END)
        
        # Insert tasks into the Text widget
        for task, task_info in tasks_info.items():
            show_tasks_entry.insert(tk.END, f"{task}: {task_info}\n")
    else:
        show_tasks_entry.insert(tk.END, "No tasks available\n")