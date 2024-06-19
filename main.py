

#from task_management.task_manager import TaskManager: Imports TaskManager class from task_manager.py
from task_management.task_manager import TaskManager

#Enters a loop to display a menu and handle user input for various operations andd executes operations based on user input
def main():
    task_manager = TaskManager()

    while True:
        print("\n===== Ultra Task Manager =====")
        print("1. List Tasks")
        print("2. Create a Task")
        print("3. Update a Task")
        print("4. Delete a Task")
        print("5 filter tasks")
        print("6. Exit")
        print("====================")

#Get user input for menu choice
        choice = input("Please select an option: ")

#Process user choice
        if choice == "1":
#Option 1: List all tasks
            task_manager.list_tasks()
        elif choice == "2":
#Option 2: Create a new task
            description = input("Enter task description: ")
            deadline = input("Enter deadline: ")
            priority = input("Enter priority: ")
            category = input("Enter category: ")
            task_manager.create_task(description, deadline, priority, category)
        elif choice == "3":
#Option 3: Update an existing task
            task_id = int(input("Enter task ID to update: "))
            description = input("Enter new description (press Enter to keep current): ")
            deadline = input("Enter new deadline (press Enter to keep current): ")
            priority = input("Enter new priority (press Enter to keep current): ")
            category = input("Enter new category (press Enter to keep current): ")
            status = input("Enter new status (press Enter to keep current): ")
            update_data = {
                "description": description,
                "deadline": deadline,
                "priority": priority,
                "category": category,
                "status": status
            }
            task_manager.update_task(task_id, **update_data)
        elif choice == "4":
#Option 4: Delete an existing task
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)
        elif choice == "5":
#Option 5: Filter tasks by status
            filter_type = input("Type the type of filter (Category, Priority or Deadline): ").lower()
            filter_value = input(f"Type the value to filter by {filter_type}: ")
            task_manager.filter_tasks(filter_type, filter_value)
#Option 8: Exit the program
        elif choice == "8":
            print("Exiting, please wait...")
            break
        else:
#Handles invalid input
            print("Invalid choice. Please choose a number from the menu.")
#After exiting the loop, save tasks to file
    print("Saving tasks...")
    task_manager.save_tasks()
    print("Tasks saved successfully.")

if __name__ == "__main__":
    main()
