import json

classification_type = input("entra una clasificacion:")

with open('dataBase.json','r') as file:
    data = json.load(file) 
    
def classify_task(classification_type):
    #clasification by priority
    if classification_type == "priority":
        task_numbers = 0
        print("-" * 10, "PRIORITY A", "-" * 10)
        for task in data:
            if task['priority'] == 'A':
                task_numbers += 1
                print(f"#{task_numbers} Task: {task['description']} Deadline: {task['deadline']} Category: {task['category']} Priority: {task['priority']}")
        
        task_numbers = 0
        print("-" * 10, "PRIORITY B", "-" * 10)
        for task in data:
            if task['priority'] == 'B':
                task_numbers += 1
                print(f"#{task_numbers} Task: {task['description']} Deadline: {task['deadline']} Category: {task['category']} Priority: {task['priority']}")

        task_numbers = 0
        print("-" * 10, "PRIORITY C", "-" * 10)
        for task in data:
            if task['priority'] == 'C':
                task_numbers += 1
                print(f"#{task_numbers} Task: {task['description']} Deadline: {task['deadline']} Category: {task['category']} Priority: {task['priority']}")
    #clasification by status
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
                print(f"#{task_numbers} Task: {task['description']} Deadline: {task['deadline']} Category: {task['category']} State: {task['state']}")


classify_task(classification_type)
