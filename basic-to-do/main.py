''' OS module for the control of the save file'''
import os

FILE_NAME = "tasks.txt"

def file_control():
    """Checks if the file exists, creates an empty one if not."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", encoding="utf-8"):
            pass

def read_tasks():
    """Reads all lines from the file."""
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        rows = f.readlines()
        return rows

def print_tasks():
    """Prints all tasks with index numbers."""
    rows = read_tasks()
    if not rows:
        print("There is no task for today.")
    else:
        print("Your Tasks: ")
        for i, row in enumerate(rows, start=1):
            print(f"{i}- {row.strip()}")
        print("-" * 40)

def add_task(task):
    """Appends a new task to the file."""
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(f"{task}\n")
        print(f"Task: '{task}' has added.")

def remove_task(i):
    """Removes the task at the given index and updates the file."""
    task_list = read_tasks()
    removed_task = task_list.pop(i - 1).strip()
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        f.writelines(task_list)
    print(f"Task: '{removed_task}' has been removed.")

def count_tasks():
    """Returns the total count of tasks."""
    task_list = read_tasks()
    return len(task_list)

def complete_task(k):
    """Marks the specified task as [DONE]."""
    task_list = read_tasks()
    task_to_complete = task_list[k - 1].strip()
    if "[DONE]" in task_to_complete:
        print("This task is already completed.")
    else:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            for i, task in enumerate(task_list, start=1):
                if i == k:
                    f.write(f"{task.strip()} [DONE]\n")
                else:
                    f.write(task)
        print(f"Task: '{task_to_complete}' has been completed. Well done!")

file_control()

def main():
    """Runs the main application loop."""
    print("\nWelcome!")
    while True:
        print(
            "\n1-Add a task | 2-Show the task list | 3-Remove a task from list"
              "| 4- Complete a task | 5- See how many tasks left | q- Exit from the app"
              )
        choice = input("Enter your choice: ")
        match choice.lower():
            case "1":
                new_task = input("Enter your work to do: ")
                add_task(new_task)
            case "2":
                print_tasks()
            case "3":
                task_list = read_tasks()
                if not task_list:
                    print("The list is already empty!")
                else:
                    number_of_tasks = count_tasks()
                    try:
                        number_of_tasks = count_tasks()
                        msg = (
                            "Enter 1 (Only task)"
                            if number_of_tasks == 1
                            else f"Enter between 1-{number_of_tasks}"
                        )
                        index = int(input(f"Which task you want to remove? ({msg}):"))
                        if index < 1 or index > number_of_tasks:
                            print("Task index is out of bounds!")
                        else:
                            remove_task(index)
                    except ValueError:
                        print("Please enter a valid number!")
            case "4":
                task_list = read_tasks()
                if not task_list:
                    print("The list is already empty!")
                else:
                    number_of_tasks = count_tasks()
                    try:
                        number_of_tasks = count_tasks()
                        msg = (
                            "Enter 1 (Only task)"
                            if number_of_tasks == 1
                            else f"Enter between 1-{number_of_tasks}"
                        )
                        index = int(input(f"Which task you want to complete? ({msg}):"))
                        if index < 1 or index > number_of_tasks:
                            print("Task index is out of bounds!")
                        else:
                            complete_task(index)
                    except ValueError:
                        print("Please enter a valid number!")
            case "5":
                counter = count_tasks()
                print(f"You have {counter} tasks to do.")
            case "q":
                print("Program is being exited..")
                break
            case _:
                print("Invalid choice!")


if __name__ == "__main__":
    main()
