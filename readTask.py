import json
import os

tasklocation = "./task.json"


def list_tasks():
    #open the file of task and  print all of the task
    with open('dataBase.json', 'r') as file:
        data = json.load(file)
        taskNumber = 0
        for task in data:
            taskNumber = taskNumber + 1
            descripcion = task['description']
            priority = task['priority']
            deadline = task['deadline']
            category = task['category']
            print(f"#{taskNumber} Task:{descripcion} Deadline:{deadline} Category:{category} Priority:{priority}")
            
 




def read_task():
    if os.path.exists(tasklocation):
        list_tasks()
        
    else:
         task =[]
    return task
        
    
read_task()

