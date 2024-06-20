
from task_management_copy_copy import TaskManager
def main():
    task_manager = TaskManager

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
            task_manager.list_tasks()
        elif choice == "2":
            description = input("Enter task description: ")
            deadline = input("Enter deadline: ")
            priority = input("Enter priority (A = CRUCIAL  B = IMPORTANT   C = SIGNIFICANT): ")
            category = input("Enter category: ")
            status = input("enter status")
            task_manager.create_task(description, deadline, priority, category,status)
        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            description = input("Enter new description (press Enter to keep current): ")
            deadline = input("Enter deadline (YYYY-MM-DD):  ")
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
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)
        elif choice == "5":
            filter_type = input("Type the type of filter (Category, Priority,status or Deadline): ").lower()
            filter_value = input(f"Type the value to filter by {filter_type}: ")
            task_manager.filter_tasks(filter_type, filter_value)
        elif choice == "6":
            classification_type = input("Enter the classification type: ")
            task_manager.classify_task(classification_type)
        elif choice == "7":
            print("Exiting, please wait...")
            break
        else:
            print("Invalid choice. Please choose a number from the menu.")

    print("Saving tasks...")
    task_manager.save_tasks()
    print("Tasks saved successfully.")

if __name__ == "__main__":
    main()
