import json
#categoryFiltered = input("Enter category: ")
categoryFiltered2 = input("Enter Priority: ")

#research the posible match with the category provided by the user
def filter_by_category(category):
    task_number = 0
    with open('dataBase.json', 'r') as file:
        data = json.load(file)
        for taskfilterd in data:
            if taskfilterd['category'] == category:
                task_number += 1
                print(f"#{task_number} Task: {taskfilterd['description']} Deadline: {taskfilterd['deadline']} Category: {category} Priority: {taskfilterd['priority']}")

    if task_number == 0:
        print(f"Lo siento, no tienes tareas de {category}")
        
#filter_by_category(categoryFiltered)

# hacer una funcion que permita como el usuario tiene que filtrar  y como puede filtrar




def filter_by_priority(priority):
    task_number = 0
    with open('dataBase.json', 'r') as file:
        data = json.load(file)
        for taskfilterd in data:
            if taskfilterd['priority'] == priority:
                task_number += 1
                print(f"#{task_number} Task: {taskfilterd['description']} Deadline: {taskfilterd['deadline']} Priority: {priority} Category: {taskfilterd['category']}")

    if task_number == 0:
        print(f"Lo siento, no tienes tareas de {priority}")
        
filter_by_priority(categoryFiltered2)