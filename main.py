#from task_management.task_manager import TaskManager  # Asegúrate de que la importación correcta esté descomentada y sea válida
from task_manager import TaskManager

def main():
    task_manager = TaskManager()

##Enters a loop to display a menu and handle user input for various operations andd executes operations based on user input
    while True:
        print("\n===== Task Manager =====")
        print("1. List Tasks")
        print("2. Create a Task")
        print("3. Update a Task")
        print("4. Delete a Task")
        print("5. Filter Tasks")
        print("6. Classify Tasks")
        print("7. Exit")
        print("====================")

        choice = input("Please select an option: ")

        if choice == "1":
            # Option 1: List all tasks
            task_manager.list_tasks()
        elif choice == "2":
            # Option 2: Create a new task
            description = input("Enter task description: ")
            deadline = input("Enter deadline: ")
            priority = input("Enter priority: ")
            category = input("Enter category: ")
            status = input("Enter status: ")
            task_manager.create_task(description, deadline, priority, category, status)
        elif choice == "3":
            # Option 3: Update an existing task
            task_id = input("Enter task ID to update: ")
            description = input("Enter new description (press Enter to keep current): ")
            deadline = input("Enter new deadline (press Enter to keep current): ")
            priority = input("Enter new priority (press Enter to keep current): ")
            category = input("Enter new category (press Enter to keep current): ")
            status = input("Enter new status (press Enter to keep current): ")
            update_data = {
                "description": description if description else None,
                "deadline": deadline if deadline else None,
                "priority": priority if priority else None,
                "category": category if category else None,
                "status": status if status else None
            }
            task_manager.update_task(task_id, **{k: v for k, v in update_data.items() if v is not None})
        elif choice == "4":
            # Option 4: Delete an existing task
            task_id = input("Enter task ID to delete: ")
            task_manager.delete_task(task_id)
        elif choice == "5":
            # Option 5: Filter tasks by status
            filter_type = input("Type the type of filter (category, priority, or deadline): ").lower()
            filter_value = input(f"Type the value to filter by {filter_type}: ")
            task_manager.filter_tasks(filter_type, filter_value)
        elif choice == "6":
            # Option 6: Classify tasks
            classification_type = input("Enter the classification type (priority, status, category, deadline): ").lower()
            task_manager.classify_tasks(classification_type)
        elif choice == "7":
            # Option 7: Exit the program
            print("Exiting, please wait...")
            break  
        else:
            # Handles invalid input
            print("Invalid choice. Please choose a number from the menu.")
    
    # After exiting the loop, save tasks to file
    print("Saving tasks...")
    task_manager.save_tasks()
    print("Tasks saved successfully.")

if __name__ == "__main__":
    main()
