# main.py
from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
    tasks
)

def display_menu():
    print("\n--- Task Management System ---")
    print("1. Add Task")
    print("2. View Pending Tasks")
    print("3. Mark Task as Complete")
    print("4. View Progress")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date (YYYY-MM-DD): ")

            print(add_task(title, description, due_date))

        elif choice == "2":
            pending = view_pending_tasks()
            if not pending:
                print("No pending tasks.")
            else:
                for i, task in enumerate(pending):
                    print(f"{i+1}. {task['title']}")

        elif choice == "3":
            pending = view_pending_tasks()

            if not pending:
                print("No pending tasks to mark as complete.")
            else:
                for i, task in enumerate(pending):
                    print(f"{i+1}. {task['title']}")

                try:
                    index = int(input("Enter task number: ")) - 1
                    print(mark_task_as_complete(index))
                except ValueError:
                    print("Invalid input.")

        elif choice == "4":
            print(calculate_progress(tasks))   # ✅ PASS list

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()