# task_manager/task_utils.py
from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []

def add_task(title, description, due_date):
    is_valid, msg = validate_task_title(title)
    if not is_valid:
        return msg

    is_valid, msg = validate_task_description(description)
    if not is_valid:
        return msg

    is_valid, msg = validate_due_date(due_date)
    if not is_valid:
        return msg

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    return "Task added successfully."

def mark_task_as_complete(index):
    if index < 0 or index >= len(tasks):
        return "Invalid task number."

    tasks[index]["completed"] = True
    return f'Task "{tasks[index]["title"]}" marked as complete.'

def view_pending_tasks():
    return [task for task in tasks if not task["completed"]]

def calculate_progress():
    if len(tasks) == 0:
        return 0

    completed = sum(task["completed"] for task in tasks)
    return round((completed / len(tasks)) * 100, 2)