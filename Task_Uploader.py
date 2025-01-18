# Create a simple task manager program using Python that allows users to add, view, update, and delete the task.
tasks = []


def add_the_task():
    x = input("What is your task: ").lower()
    tasks.append(x)
    print("task added successfully")


def view_all_Task():
    if tasks:
        print("All tasks")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}.{task}")
    else:
        print("No task available")


def update_the_task():
    view_all_Task()
    if tasks:
        n = int(input("Please enter the task number for update: ")) - 1
        if 0 <= n < len(tasks):
            new_task = input("Please enter the new task name: ").lower()
            tasks[n] = new_task
            print("Task updated successfully")
        else:
            print("Invalid task number")
    else:
        print("No task available")


def delete_the_task():
    view_all_Task()
    if tasks:
        v = int(input("Please enter the task number for delete: ")) - 1
        if 0 <= v < len(tasks):
            x = tasks.pop(v)
            print(f"task {x} deleted successfully")
        else:
            print("Invalid task number")
    else:
        print("nothing in there")


def main():
    while True:
        z = """
            Simple task manager
            1) Add task
            2) View task
            3) Update task
            4) Delete task
            5) Exit task
            """
        print(z)
        choice = input("Please enter the choice: ")
        if choice == "1":
            add_the_task()
        elif choice == "2":
            view_all_Task()
        elif choice == "3":
            update_the_task()
        elif choice == "4":
            delete_the_task()
        elif choice == "5":
            print("Exit")
            break
        else:
            print("Invalid choice")


main()