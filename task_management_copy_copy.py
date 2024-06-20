import json
import os
import uuid
from datetime import datetime

tasklocation = "./task.json"

class TaskManager:
    def __init__(self):
        self.tasklocation = tasklocation

    def create_task(self, description, deadline, priority, category, status):
        # Validar el campo 'status'
        while True:
            if status.upper()[0] not in ['P', 'I', 'C']:
                status = input("Invalid status. Please enter a valid status (P, I, or C): ")
            else:
                break

        # Validar el campo 'deadline'
        while True:
            try:
                deadline_datetime = datetime.strptime(deadline, '%Y-%m-%d')
                if deadline_datetime < datetime.now():
                    raise ValueError("Deadline must be a future date.")
                break
            except ValueError:
                deadline = input("Invalid deadline format. Deadline must be in the format 'YYYY-MM-DD': ")

        # Validar el campo 'priority'
        while True:
            if priority.upper() not in ['A', 'B', 'C']:
                priority = input("Invalid priority. Please enter a valid priority (A, B, or C): ")
            else:
                break

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

    def write_task(self, tasks):
        with open(self.tasklocation, 'w') as task_file:
            json.dump(tasks, task_file, indent=4)

    def update_task(self, task_id, **kwargs):
        tasks = self.read_task()
        for task in tasks:
            if task['id'] == task_id:
                # Validar el campo 'status'
                if 'status' in kwargs:
                    while True:
                        if kwargs['status'].upper()[0] not in ['P', 'I', 'C']:
                            kwargs['status'] = input("Invalid status. Please enter a valid status (P, I, or C): ")
                        else:
                            break

                # Validar el campo 'deadline'
                if 'deadline' in kwargs:
                    while True:
                        try:
                            deadline_datetime = datetime.strptime(kwargs['deadline'], '%Y-%m-%d')
                            if deadline_datetime < datetime.now():
                                raise ValueError("Deadline must be a future date.")
                            break
                        except ValueError:
                            kwargs['deadline'] = input("Invalid deadline format. Deadline must be in the format 'YYYY-MM-DD': ")

                # Validar el campo 'priority'
                if 'priority' in kwargs:
                    while True:
                        if kwargs['priority'].upper() not in ['A', 'B', 'C']:
                            kwargs['priority'] = input("Invalid priority. Please enter a valid priority (A, B, or C): ")
                        else:
                            break

                task.update(kwargs)
                break
        self.write_task(tasks)

    def filter_tasks(self, filter_type, filter_value):
        # Validar el campo 'filter_type'
        while True:
            if filter_type not in ['description', 'priority', 'category', 'status']:
                filter_type = input("Invalid filter type. Please enter a valid filter type (description, priority, category, or status): ")
            else:
                break

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
            print(f"{'-'*10}#{i} {description} {'-'*10}\n  Category: {category} Priority: {priority}   Status: {status}   Deadline: {deadline}")
