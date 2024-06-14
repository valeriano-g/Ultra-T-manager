import json
import os
import uuid # generate the id

idTask =''
tasklocation ="./task.json"

def CreateTask(description,deadline,priority,category):
    
    idTask = str(uuid.uuid4()) #create identificator
    newTask = {
        "id": idTask,
        "description":description,
        "deadline":deadline,
        "priority": priority,
        "category": category
    }
    
    with open('task.json','w') as task:
        json.dump(newTask,task,indent=4)
    
CreateTask('prueba2','6/4/2024',"a",'rojaa')
