def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks yet.")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks file found!")

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added!")

def remove_task(task_no):
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if 0 < task_no <= len(tasks):
        tasks.pop(task_no - 1)
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task removed!")
    else:
        print("Invalid task number!")

while True:
    print("\n--- To-Do List ---")
    print("1. View tasks\n2. Add task\n3. Remove task\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "3":
        task_no = int(input("Enter task number to remove: "))
        remove_task(task_no)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option! Try again.")
