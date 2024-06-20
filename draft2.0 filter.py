import json

filter_type = input("Type the type of filter (Category, Priority or Deadline): ").lower()
filter_value = input(f"Type the value to filter by {filter_type}: ")

def filter_tasks(filter_type, filter_value):
    task_number = 0
    with open('dataBase.json', 'r') as file:
        data = json.load(file)
        for task in data:
            #filtery by category
            if filter_type == 'category' and task['category'] == filter_value:
                task_number += 1
                print(f"#{task_number} Task: {task['description']} Deadline: {task['deadline']} Category: {filter_value} Priority: {task['priority']}")
                #filter by priority
            elif filter_type == 'priority' and task['priority'] == filter_value:
                task_number += 1
                print(f"#{task_number} Task: {task['description']} Deadline: {task['deadline']} Priority: {filter_value} Category: {task['category']}")
                #filter by deadline
            elif filter_type == 'deadline' and task['deadline'] == filter_value:
                task_number += 1
                print(f"#{task_number} Task: {task['description']} Deadline: {filter_value} Priority: {task['priority']} Category: {task['category']}")

    if task_number == 0:
        print(f"Lo siento, no tienes tareas con {filter_type} '{filter_value}'")

filter_tasks(filter_type, filter_value)