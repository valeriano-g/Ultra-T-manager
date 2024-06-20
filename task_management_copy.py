import json
import os
import uuid
from datetime import datetime

tasklocation = "./task.json"

def TaskManager():
    
# Global variables 
 

# Function to create a new task
 def create_task(description, deadline, priority, category, status):
    # Generate a unique ID for the task 
    id_task = str(uuid.uuid4()) 

    # Create a dictionary representing the new task 
    new_task = {
        "id": id_task,
        "description": description,
        "deadline": deadline,
        "priority": priority.upper(),  # Convert priority to uppercase 
        "category": category,
        "status": status.upper()[0],  # Convert status to uppercase and take the first character
    }

    # Read existing tasks from the JSON file
    tasks = read_task()

    # Add the new task to the list
    tasks.append(new_task)

    # Write the updated list of tasks to the JSON file
    write_task(tasks)

# Function to read tasks from the JSON file
def read_task():
    if os.path.exists(tasklocation):
        with open(tasklocation, 'r') as data_file:
            try:
                tasks = json.load(data_file)
            except json.JSONDecodeError:
                tasks = []
    else:
        tasks = []

    return tasks

# Function to write tasks to the JSON file
def write_task(tasks):
    with open(tasklocation, 'w') as task_file:
        json.dump(tasks, task_file, indent=4)

# Function to list all tasks
def list_tasks():
    # Open the task file and display all tasks
    tasks = read_task()
    if not tasks:
        print("No tasks found.")
        return
    
    for i, task in enumerate(tasks, start=1):
        description = task['description']
        priority = task['priority']
        deadline = task['deadline']
        category = task['category']
        status = task['status']
        print(f"{'-'*10}#{i} {description} {'-'*10}\n  Category: {category} Priority: {priority}   Status: {status}   Deadline: {deadline}   ")


# Example usage
if __name__ == "__main__":
    description = input("Enter task description: ")
    
    # Validate the deadline input
    while True:
        deadline = input("Enter deadline (YYYY-MM-DD): ")
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    
    # Validate priority
    validationPriority = ['A', 'B', 'C']
    while True:
        priority = input("Enter priority (A = CRUCIAL  B = IMPORTANT   C = SIGNIFICANT): ").upper()
        if priority in validationPriority:
            break
        else:
            print("Invalid format. You have to write A, B, or C.")
    
    category = input("Enter category: ").upper()
    
    # Validate status
    validationStatus = ['P', 'I', 'C']
    while True:
        status = input("Enter status (P = PENDING  I = IN PROGRESS...  C = completed): ").upper()
        if status in validationStatus:
            break
        else:
            print("Invalid format. You have to write P, I, or C.")

#filter 



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
        

#clasification


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

