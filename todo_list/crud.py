#!/usr/bin/env python3
"""
This file has methods that helps to achieve crud operations of a todo list app
    1. create task && set time to it
    2. read tasks available && see remaining time for the task to start
    3. update task && update time
    4. delete task 
    5. clear all tasks
"""
from datetime import datetime

class Crud():
    def __init__(self):
        self.tasks = []
        self.start_time = []
        self.end_time = []

    def create_task(self, task, start_time, end_time):
        """create task and set time to it"""
        if task and start_time and end_time:
            self.tasks.append(task)
            self.start_time.append(start_time)
            self.end_time.append(end_time)

            time_now = datetime.now()
            time_remaining = start_time - time_now

            if time_remaining.total_seconds() <= 0:
                return f"Task: {task} will start at {start_time}"
            else:
                hours, minutes = divmod(time_remaining.seconds, 3600)
                minutes, seconds = divmod(minutes, 60)
                remaining_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                return f"Task: {task} will start at {start_time.strftime('%H:%M:%S')} : {remaining_time} time remaining"


    def read_tasks(self):
        """
        read tasks available in the self.tasks list
        and see remaining time for the task to start
        """
        tasks_info = {}
        if self.tasks:
            for task, start_time in zip(self.tasks, self.start_time):
                time_now = datetime.now()
                time_remaining = start_time - time_now
                if time_remaining.total_seconds() <= 0:
                    tasks_info[task] = "Task has started"
                else:
                    hours, minutes = divmod(time_remaining.seconds, 3600)
                    minutes, seconds = divmod(minutes, 60)
                    time_remaining = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                    tasks_info[task] = f"time remaining: {time_remaining}"

            return tasks_info
        else:
            return "No tasks available"
