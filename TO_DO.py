import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    """Load tasks from file."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\n📌 No tasks available.\n")
    else:
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['title']} [{status}]")
        print()

def add_task(tasks):
    """Add a new task."""
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("✅ Task added!")

def mark_done(tasks):
    """Mark a task as done."""
    show_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark done: "))
        tasks[choice-1]["done"] = True
        save_tasks(tasks)
        print("🎉 Task marked as done!")
    except (IndexError, ValueError):
        print("⚠️ Invalid task number.")

def delete_task(tasks):
    """Delete a task."""
    show_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: "))
        tasks.pop(choice-1)
        save_tasks(tasks)
        print("🗑️ Task deleted!")
    except (IndexError, ValueError):
        print("⚠️ Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, try again!")

if __name__ == "__main__":
    main()
1