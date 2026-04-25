import os

def load_tasks(filename = "todo_list.txt"):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
    return tasks

def save_tasks(tasks, filename= "todo_list.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()

while True:
    task_count = len(tasks)
    if task_count == 0:
        print("\nYour to-do list is currently empty.")
    else:
        print(f"\nCurrent to-do list ({task_count} tasks):")
    for index, task in enumerate(tasks, start=1):
        print(index, task)

    user_input = input("\nWould you like to add, edit, remove, or exit?: ").lower()

    if user_input == "add":
        new_task = input("\nWhat task would you like to add?: ")
        tasks.append(new_task)
        print("Task added")

    elif user_input == "edit":
        edit_task = input("\nWhat task would you like to edit?: ")
        if edit_task.isdigit():
            edit_task = int(edit_task) - 1
            if 0 <= edit_task < len(tasks):
                print(f"Task to edit: {tasks[edit_task]}")
                updated_task = input("Update task (Press enter to keep original): ")
                if updated_task.strip() == "":
                    print("No changes made.")
                else:
                    tasks[edit_task] = updated_task
                    print("Updated task successfully.")
            else:
                print("Task does not exist.")
        elif edit_task in tasks:
            edit_task = tasks.index(edit_task)
            print(f"Task to edit: {tasks[edit_task]}")
            updated_task = input("Update task (Press enter to keep original): ")
            if updated_task.strip() == "":
                print("No changes made.")
            else:
                tasks[edit_task] = updated_task
                print("Updated task successfully.")
        else:
            print("Task does not exist.")
            

    elif user_input == "remove":
        remove_task = input("\nWhat task would you like to remove?: ")
        if  remove_task.isdigit():
            remove_task = int(remove_task) - 1
            if 0 <= remove_task < len(tasks):
                tasks.pop(remove_task)
                print("Task removed")
            else:
                print("Task does not exist")
        elif remove_task in tasks:
            tasks.remove(remove_task)
            print("Task removed")
        else:
            print("Task does not exist")

    elif user_input == "exit":
        save_tasks(tasks)
        print("\nGoodbye")
        break

    else:
        print("\nPlease enter a valid action (add, remove, edit or exit.")