import datetime

def validate_task_title(title):
    if not title or not title.strip():
        return False, "Title cannot be empty."
    if len(title) > 50:
        return False, "Title cannot exceed 50 characters."
    return True, ""

def validate_task_description(description):
    if not description or not description.strip():
        return False, "Description cannot be empty."
    if len (description) > 200:
        return False, "Description cannot exceed 200 characters."
    return True, ""

def validate_due_date(due_date):
    try:
        due = datetime.datetime.strptime(due_date, "%Y-%m-%d")
        if due < datetime.datetime.now():
            return False, "Due date cannot be in the past."
        return True, ""
    except ValueError:
        return False, "Invalid date format. Use YYYY-MM-DD."
    