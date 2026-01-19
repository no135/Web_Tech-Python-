import json
import os

FILE = "todo.json"

def load_tasks():
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

tasks = load_tasks()

while True:
    print("\nYour To-Do List:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

    print("\n1. Add")
    print("2. Remove")
    print("3. Quit")

    choice = input("Choose: ")

    if choice == "1":
        tasks.append(input("New task: "))
        save_tasks(tasks)

    elif choice == "2":
        try:
            tasks.pop(int(input("Number: ")) - 1)
            save_tasks(tasks)
        except:
            print("Invalid number.")

    elif choice == "3":
        break
