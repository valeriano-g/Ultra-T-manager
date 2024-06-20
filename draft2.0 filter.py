import json

valid_filters = ["priority", "status", "category", "deadline"]

while True:
    filter_type = input("Ingresa una clasificación (Priority, Status, Category, Deadline): ").lower()
    if filter_type in valid_filters:
        break
    else:
        print("Clasificación inválida. Inténtalo de nuevo.")

filter_value = input(f"Type the value to filter by {filter_type}: ").upper()

def filter_tasks(filter_type, filter_value):
    task_number = 0
    with open('dataBase.json', 'r') as file:
        data = json.load(file)
        print("-" * 10, filter_value, "-" * 10)
        for task in data:
            # Filter by category
            if filter_type == 'category' and task['category'] == filter_value:
                task_number += 1
                print(f"#{task_number} Task: {task['description']}  Category: {filter_value}   Deadline: {task['deadline']}  Priority: {task['priority']} Status: {task['status']}")
            # Filter by priority
            elif filter_type == 'priority' and task['priority'] == filter_value:
                task_number += 1
                print(f"#{task_number} Task: {task['description']} Priority: {filter_value}  Deadline: {task['deadline']}  Category: {task['category']} Status: {task['status']}")
            # Filter by deadline
            elif filter_type == 'deadline' and task['deadline'] == filter_value:
                task_number += 1
                print(f"#{task_number} Task: {task['description']} Deadline: {filter_value} Priority: {task['priority']} Category: {task['category']} Status: {task['status']}")
            # Filter by status
            elif filter_type == 'status' and task['status'] == filter_value:
                task_number += 1
                print(f"#{task_number} Task: {task['description']} Status: {filter_value}  Deadline: {task['deadline']} Priority: {task['priority']} Category: {task['category']} Status: {filter_value}")

    if task_number == 0:
        print(f"Lo siento, no tienes tareas con {filter_type} '{filter_value}'")

filter_tasks(filter_type, filter_value)