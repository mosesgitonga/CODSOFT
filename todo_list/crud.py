#!/usr/bin/env python3.10
"""
This file has methods that helps to achieve crud operations of a todo list app
    1. create task 
    2. read tasks available 
    3. clear all tasks
"""
from datetime import datetime

class Crud():
    def __init__(self):
        self.tasks = []  

    def create_task(self, task):
        """Create task """
        if task:
            self.tasks.append(task)
            return f"Task {self.tasks} has been added\n\n\t"
        else:
            return "no task have been entered"

        
    def read_tasks(self):
        """Read tasks available in the self.tasks list"""
       
        tasks_info = "\n".join(f"- {task}" for task in self.tasks)
        return f"Tasks available:\n{tasks_info}\n"
        
    def clear_tasks(self):
        """
        clear all tasks
        """

        if self.tasks:
            self.tasks.clear()
            return "all tasks  have been cleared :)"
        else:
            return "No task to clear"
