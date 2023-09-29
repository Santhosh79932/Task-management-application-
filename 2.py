import os
import pickle

class Task:
    def __init__(self, title, priority, due_date, completed=False):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

class TaskManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, 'rb') as file:
                return pickle.load(file)
        return []

    def save_tasks(self):
        with open(self.db_file, 'wb') as file:
            pickle.dump(self.tasks, file)

    def add_task(self, title, priority, due_date):
        task = Task(title, priority, due_date)
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            self.save_tasks()

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            self.save_tasks()

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Task List:")
            for i, task in enumerate(self.tasks):
                status = "Completed" if task.completed else "Not Completed"
                print(f"{i + 1}. {task.title} (Priority: {task.priority}, Due Date: {task.due_date}, Status: {status})")

def main():
    db_file = "task_manager.db"
    task_manager = TaskManager(db_file)

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            priority = input("Enter task priority (high/medium/low): ")
            due_date = input("Enter due date (yyyy-mm-dd): ")
            task_manager.add_task(title, priority, due_date)
        elif choice == '2':
            task_index = int(input("Enter task index to remove: ")) - 1
            task_manager.remove_task(task_index)
        elif choice == '3':
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            task_manager.mark_completed(task_index)
        elif choice == '4':
            task_manager.list_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
