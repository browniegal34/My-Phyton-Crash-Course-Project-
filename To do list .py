import json
import os

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet")
        return
    for i, t in enumerate(tasks, 1):
        mark = "[x]" if t["done"] else "[ ]"
        print(i, mark, t["title"])

tasks = load_tasks()

while True:
    print("\n1.Add 2.View 3.Done 4.Delete 5.Quit")
    choice = input("Choose: ")

    if choice == "1":
        title = input("Task: ")
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("Task added")
    elif choice == "2":
        show_tasks(tasks)
    elif choice == "3":
        show_tasks(tasks)
        try:
            n = int(input("Task number: "))
            tasks[n - 1]["done"] = True
            save_tasks(tasks)
            print("Marked as done")
        except (ValueError, IndexError):
            print("Task does not exist")
    elif choice == "4":
        show_tasks(tasks)
        try:
            n = int(input("Task number: "))
            removed = tasks.pop(n - 1)
            save_tasks(tasks)
            print("Deleted:", removed["title"])
        except (ValueError, IndexError):
            print("Task does not exist")
    elif choice == "5":
        print("Bye!")
        break
    else:
        print("Invalid choice")