#!/usr/bin/env python3.10

import tkinter
from crud import Crud

def create_task_command(task):
   
    crud = Crud()
    return crud.create_task(task)

def read_tasks_command():
    # Assuming 'crud' is an instance of your Crud class
    crud = Crud()
    tasks_info = crud.read_tasks()  # Fetch tasks from your Crud class method
    
        