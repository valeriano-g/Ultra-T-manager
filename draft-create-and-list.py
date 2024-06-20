import json
import os
import uuid
from datetime import datetime

# Global variables
tasklocation = "./dataBase.json"

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
        priority = input("Enter priority (A = CRUCIAL  B = IMPORTANT   C = NOT IMPORTANT): ").upper()
        if priority in validationPriority:
            break
        else:
            print("Invalid format. You have to write A, B, or C.")
    
    category = input("Enter category: ").upper()
    
    # Validate status
    validationStatus = ['P', 'I', 'C']
    while True:
        status = input("Enter status (P = PENDING  I = in progress  C = completed): ").upper()
        if status in validationStatus:
            break
        else:
            print("Invalid format. You have to write P, I, or C.")

    create_task(description, deadline, priority, category, status)
    list_tasks()