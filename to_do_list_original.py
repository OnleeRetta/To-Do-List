# To-Do List Application

# Initialize an empty list to store tasks
tasks = []


def display_menu():  # Displays the main menu with options.
    print(
        "---Welcome to Your To-Do List.---\n---Please select an option from the Menu---"
    )
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")


def add_task():  # Adds a new task to the task list.

    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' has been added.")


def view_tasks():  # Displays all tasks in the list.
    if tasks:
        print("\nYour Tasks:")
        # Use a manual counter to track the task number
        i = 1
        for task in tasks:
            print(f"{i}. {task}")
            i += 1  # Increment the counter with each task
    else:
        print("Your task list is empty.")


def delete_task():  # Deletes a specified task from the list.
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' has been deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks to delete.")


def main():  # Main function to run the To-Do List application.
    while True:
        display_menu()
        try:
            choice = int(input("Choose an option (1-4): "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        finally:
            print("\nReturning to the main menu...")


# Run the application
if __name__ == "__main__":
    main()
