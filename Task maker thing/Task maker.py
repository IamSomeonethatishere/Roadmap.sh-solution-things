import json
import os

tasks = []

# Load existing tasks
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    tasks = []
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Menu
print("What do you want to do?")
print("Options, (1)(2)(3)")
print("1. Add task")
print("2. Update progress on a task")
print("3. List all tasks")
Menu_input = int(input("Type 1, 2 or 3. Only integers are allowed: "))

# Adding tasks
if Menu_input == 1:
    task_name = input("You want to add a task. What will this task be called? ")
    new_task = {"name": task_name, "progress": 0}
    tasks.append(new_task)
    print(f"Task '{task_name}' added!")
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)

# Updating tasks
elif Menu_input == 2:
    if not tasks:
        print("No tasks available to update.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task['name']} (Progress: {task['progress']}%)")
        choice = int(input("Enter the number of the task you want to update: ")) - 1
        if 0 <= choice < len(tasks):
            new_progress = int(input("Enter new progress (0-100): "))
            tasks[choice]["progress"] = new_progress
            print(f"Task '{tasks[choice]['name']}' updated to {new_progress}% progress.")
            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=2)
        else:
            print("Invalid task number.")

# Listing tasks
elif Menu_input == 3:
    if not tasks:
        print("No tasks available.")
    else:
        print("Here are all the tasks:")
        for task in tasks:
            print(f"- {task['name']} (Progress: {task['progress']}%)")

# Errors
else:
    print("An error occurred. Please try again.")