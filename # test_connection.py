# todo_app.py

tasks = []

def show_menu():
    print("\nTo-Do List App")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Added task: '{task}'")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        removed = tasks.pop(task_num - 1)
        print(f"Removed task: '{removed}'")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid task number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
