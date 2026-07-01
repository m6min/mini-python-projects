# To-do Lists with .txt 

A simple, file-based **To-Do List Application** built with Python. This project holds fundamental CRUD (Create, Read, Update, Delete) operations and data storage using text files
## Features

* **Persistent Storage:** Tasks are saved in a `tasks.txt` file, so they remain available after restarting the program.
* **CRUD Operations:** You can Add, List, Remove, and Complete tasks.
* **Idempotency:** Prevents marking the same task as "Completed" multiple times.
* **Error Handling:** Robust input validation to prevent crashes (e.g., entering text instead of numbers).

## Tech Stack

* **Language:** Python 3.x

## How to Run

1.  Clone the repository:
    ```bash
    git clone [https://github.com/m6min/mini-python-projects.git](https://github.com/m6min/mini-python-projects.git)
    ```
2.  Navigate to the project directory:
    ```bash
    cd python-mini-projects/todo-app
    ```
3.  Run the script:
    ```bash
    python main.py
    ```

## Usage example

```text
Welcome!
1-Add a task | 2-List | 3-Remove | 4-Complete | 5-Count | q-Exit

Enter your choice: 1
Enter your work to do: Go shopping
Task: 'Go shopping' has added.
