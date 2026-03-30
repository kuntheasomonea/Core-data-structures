# Memory-Based To-Do List

tasks = []

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    # Add Task
    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)        
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    # Remove Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            index = int(input("Enter task number to remove: "))
            
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")