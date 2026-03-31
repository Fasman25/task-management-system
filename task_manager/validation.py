# task_manager/validation.py
import datetime

def validate_task_title(title):
    if not title.strip():
        return False, "Title cannot be empty."
    if len(title.strip()) > 50:
        return False, "Title too long."
    return True, ""

def validate_task_description(description):
    if not description.strip():
        return False, "Description cannot be empty."
    if len(description.strip()) > 200:
        return False, "Description too long."
    return True, ""

def validate_due_date(due_date):
    try:
        datetime.datetime.strptime(due_date, "%Y-%m-%d")
        return True, ""
    except ValueError:
        return False, "Invalid date format."