class TodoListApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                status = "Done" if task["done"] else "Not Done"
                print(f"{i}. {task['task']} - {status}")

    def mark_done(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task index.")

def main():
    todo_list = TodoListApp()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added.")

        elif choice == "2":
            todo_list.list_tasks()

        elif choice == "3":
            task_index = int(input("Enter the task number to mark as done: "))
            todo_list.mark_done(task_index)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()