# task_manager/task_utils.py
from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []

def add_task(title, description, due_date):
    valid, msg = validate_task_title(title)
    if not valid:
        return msg

    valid, msg = validate_task_description(description)
    if not valid:
        return msg

    valid, msg = validate_due_date(due_date)
    if not valid:
        return msg

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    return "Task added successfully!"


def mark_task_as_complete(index):
    if index >= 0 and index < len(tasks):
        tasks[index]["completed"] = True
        return "Task marked as complete!"
    return "Invalid task number."


def view_pending_tasks():
    pending = []
    for task in tasks:
        if task["completed"] == False:
            pending.append(task)
    return pending


def calculate_progress(task_list):
    if len(task_list) == 0:
        return 0

    completed = 0
    for task in task_list:
        if task["completed"] == True:
            completed += 1

    return (completed / len(task_list)) * 100