import json
from datetime import datetime

valid_classifications = ["priority", "status", "category","deadline"]

while True:
    classification_type = input("Ingresa una clasificación (Priority, Status, Category, Deadline): ").lower()
    if classification_type in valid_classifications:
        break
    else:
        print("Clasificación inválida. Inténtalo de nuevo.")

with open('dataBase.json', 'r') as file:
    data = json.load(file)

def classify_task(classification_type):
    # Clasificación por prioridad
    if classification_type == "priority":
        task_numbers = 0
        print("-" * 10, "PRIORITY A", "-" * 10)
        for task in data:
            if task['priority'] == 'A':
                task_numbers += 1
                print(f"#{task_numbers} Task: {task['description']} Deadline: {task['deadline']} Category: {task['category']} Priority: {task['priority']} Status: {task['status']}")

        task_numbers = 0
        print("-" * 10, "PRIORITY B", "-" * 10)
        for task in data:
            if task['priority'] == 'B':
                task_numbers += 1
                print(f"#{task_numbers} Task: {task['description']} Deadline: {task['deadline']} Category: {task['category']} Priority: {task['priority']} Status: {task['status']}")

        task_numbers = 0
        print("-" * 10, "PRIORITY C", "-" * 10)
        for task in data:
            if task['priority'] == 'C':
                task_numbers += 1
                print(f"#{task_numbers} Task: {task['description']} Deadline: {task['deadline']} Category: {task['category']} Priority: {task['priority']} Status: {task['status']}")

    # Clasificación por estado
    elif classification_type == "status":
        task_numbers = 0
        print("-" * 10, "PENDING", "-" * 10)
        for task in data:
            if task['status'] == 'P':
                task_numbers += 1
                print(f"#{task_numbers} Task: {task['description']} Deadline: {task['deadline']} Category: {task['category']} Status: {task['status']}")

        task_numbers = 0
        print("-" * 10, "IN PROGRESS", "-" * 10)
        for task in data:
            if task['status'] == 'B':
                task_numbers += 1
                print(f"#{task_numbers} Task: {task['description']} Deadline: {task['deadline']} Category: {task['category']} Status: {task['status']}")

        task_numbers = 0
        print("-" * 10, "COMPLETED", "-" * 10)
        for task in data:
            if task['status'] == 'C':
                task_numbers += 1
                print(f"#{task_numbers} Task: {task['description']} Deadline: {task['deadline']} Category: {task['category']} Status: {task['status']}")

    # Clasificación por categoría
    elif classification_type == 'category':
        UserCategory = input("Ingresa el nombre de la categoría: ")
        print("-" * 10, UserCategory, "-" * 10)
        task_numbers = 0
        for task in data:
            if task['category'] == UserCategory:
                task_numbers += 1
                print(f"#{task_numbers} Task: {task['description']} Deadline: {task['deadline']} Category: {task['category']} Status: {task['status']}")
                
    elif classification_type == "deadline":
        sorted_tasks = sorted(data, key=lambda task: datetime.strptime(task['deadline'], '%Y-%m-%d'))
        task_numbers = 1
        for task in sorted_tasks:
            print(f"#{task_numbers} Task: {task['description']} Deadline: {task['deadline']} Category: {task['category']} Status: {task['status']}")
            task_numbers += 1         

classify_task(classification_type)