import json
import os
import uuid 
# Global variables
 
tasklocation = "./task.json"

def TaskManager():
    

# Global variables


 def CreateTask(description, deadline, priority, category):
    # Generate a unique ID for the task
    idTask = str(uuid.uuid4())

    # Create a dictionary representing the new task
    newTask = {
        "id": idTask,
        "description": description,
        "deadline": deadline,
        "priority": priority,
        "category": category
    }

    # Read existing tasks from the JSON file
    tasks = readTask()

    # Add the new task to the list
    tasks.append(newTask)

    # Write the updated list of tasks to the JSON file
    write_task(tasks)

def readTask():
    if os.path.exists(tasklocation):
        with open(tasklocation, 'r') as Datafile:
            tasks = json.load(Datafile)
    else:
        tasks = []

    return tasks

def write_task(tasks):
    with open(tasklocation, 'w') as task:
        json.dump(tasks, task, indent=4)

def list_tasks():
    # open the file and show the tasks
    tasks = readTask()
    task_number = 0
    for task in tasks:
        task_number += 1
        description = task['description']
        priority = task['priority']
        deadline = task['deadline']
        category = task['category']
        print(f"#{task_number} Task: {description} Deadline: {deadline} Category: {category} Priority: {priority}")

# Example usage