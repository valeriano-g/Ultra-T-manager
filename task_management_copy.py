import json
import os
import uuid
from datetime import datetime

tasklocation = "./task.json"

class TaskManager:
    def __init__(self):
        self.tasklocation = tasklocation

    # Function to create a new task
    def create_task(self, description, deadline, priority, category, status):
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
        tasks = self.read_task()

        # Add the new task to the list
        tasks.append(new_task)

        # Write the updated list of tasks to the JSON file
        self.write_task(tasks)

    # Function to read tasks from the JSON file
    def read_task(self):
        if os.path.exists(self.tasklocation):
            with open(self.tasklocation, 'r') as data_file:
                try:
                    tasks = json.load(data_file)
                except json.JSONDecodeError:
                    tasks = []
        else:
            tasks = []

        return tasks

    # Function to write tasks to the JSON file
    def write_task(self, tasks):
        with open(self.tasklocation, 'w') as task_file:
            json.dump(tasks, task_file, indent=4)

    # Function to list all tasks
    def list_tasks(self):
        # Open the task file and display all tasks
        tasks = self.read_task()
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

    # Function to update a task
    def update_task(self, task_id, **kwargs):
        tasks = self.read_task()
        for task in tasks:
            if task['id'] == task_id:
                task.update(kwargs)
                break
        self.write_task(tasks)

    # Function to delete a task
    def delete_task(self, task_id):
        tasks = self.read_task()
        tasks = [task for task in tasks if task['id'] != task_id]
        self.write_task(tasks)

    # Function to filter tasks
    def filter_tasks(self, filter_type, filter_value):
        tasks = self.read_task()
        filtered_tasks = [task for task in tasks if task[filter_type] == filter_value.upper()]

        if not filtered_tasks:
            print(f"No tasks found with {filter_type} '{filter_value}'")
            return

        for i, task in enumerate(filtered_tasks, start=1):
            description = task['description']
            priority = task['priority']
            deadline = task['deadline']
            category = task['category']
            status = task['status']
            print(f"{'-'*10}#{i} {description} {'-'*10}\n  Category: {category} Priority: {priority}   Status: {status}   Deadline: {deadline}   ")

    # Function to classify tasks
    def classify_tasks(self, classification_type):
        tasks = self.read_task()

        if classification_type == "priority":
            priorities = ['A', 'B', 'C']
            for priority in priorities:
                print(f"{'-'*10} PRIORITY {priority} {'-'*10}")
                for i, task in enumerate(tasks, start=1):
                    if task['priority'] == priority:
                        print(f"#{i} Task: {task['description']} Deadline: {task['deadline']} Category: {task['category']} Priority: {task['priority']} Status: {task['status']}")
        
        elif classification_type == "status":
            statuses = ['P', 'I', 'C']
            status_names = {'P': 'PENDING', 'I': 'IN PROGRESS', 'C': 'COMPLETED'}
            for status in statuses:
                print(f"{'-'*10} {status_names[status]} {'-'*10}")
                for i, task in enumerate(tasks, start=1):
                    if task['status'] == status:
                        print(f"#{i} Task: {task['description']} Deadline: {task['deadline']} Category: {task['category']} Priority: {task['priority']} Status: {task['status']}")
        
        elif classification_type == 'category':
            categories = set(task['category'] for task in tasks)
            for category in categories:
                print(f"{'-'*10} CATEGORY {category} {'-'*10}")
                for i, task in enumerate(tasks, start=1):
                    if task['category'] == category:
<<<<<<< HEAD
                        print(f"#{i} Task:")
=======
                        print(f"#{i} Task:
>>>>>>> b1a8c4f204d102f5a90221a56e6036e825ec0180
