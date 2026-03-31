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
    print("2. Mark Task as Complete")   # ✅ swapped
    print("3. View Pending Tasks")
    print("4. View Progress")
    print("5. Exit")

def main():
    while True:
        display_menu()

        try:
            choice = input("Enter your choice: ")
        except EOFError:
            break

        if choice == "1":
            try:
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                due_date = input("Enter task due date (YYYY-MM-DD): ")
            except EOFError:
                break

            print(add_task(title, description, due_date))

        elif choice == "2":   # ✅ NOW MARK COMPLETE
            try:
                index = int(input("Enter task number: ")) - 1
                print(mark_task_as_complete(index))
            except:
                print("Invalid task number.")

        elif choice == "3":   # ✅ NOW VIEW
            pending = view_pending_tasks()

            if len(pending) == 0:
                print("No pending tasks.")
            else:
                for i in range(len(pending)):
                    print(f"{i+1}. {pending[i]['title']}")

        elif choice == "4":
            print(calculate_progress(tasks))

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()