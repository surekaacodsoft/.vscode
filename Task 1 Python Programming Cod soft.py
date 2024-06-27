class Task:
    def __init__(self, title, description='', due_date=None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def __str__(self):
        return f"{'[x]' if self.completed else '[ ]'} {self.title} - {self.description} (Due: {self.due_date})"
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task(self, index, title=None, description=None, due_date=None, completed=None):
        if 0 <= index < len(self.tasks):
            if title:
                self.tasks[index].title = title
            if description:
                self.tasks[index].description = description
            if due_date:
                self.tasks[index].due_date = due_date
            if completed is not None:
                self.tasks[index].completed = completed

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")
def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            task = Task(title, description, due_date)
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.list_tasks()
        elif choice == '3':
            index = int(input("Enter task number to update: ")) - 1
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            due_date = input("Enter new due date (leave blank to keep current): ")
            completed = input("Mark as completed? (yes/no): ").lower() == 'yes'
            todo_list.update_task(index, title, description, due_date, completed)
        elif choice == '4':
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.update_task(index, completed=True)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import messagebox
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.todo_list = ToDoList()

        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack()

        self.add_task_frame = tk.Frame(self.root)
        self.add_task_frame.pack()

        self.title_label = tk.Label(self.add_task_frame, text="Title")
        self.title_label.pack(side=tk.LEFT)
        self.title_entry = tk.Entry(self.add_task_frame)
        self.title_entry.pack(side=tk.LEFT)

        self.desc_label = tk.Label(self.add_task_frame, text="Description")
        self.desc_label.pack(side=tk.LEFT)
        self.desc_entry = tk.Entry(self.add_task_frame)
        self.desc_entry.pack(side=tk.LEFT)

        self.due_date_label = tk.Label(self.add_task_frame, text="Due Date")
        self.due_date_label.pack(side=tk.LEFT)
        self.due_date_entry = tk.Entry(self.add_task_frame)
        self.due_date_entry.pack(side=tk.LEFT)

        self.add_button = tk.Button(self.add_task_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        self.list_tasks()

    def add_task(self):
        title = self.title_entry.get()
        description = self.desc_entry.get()
        due_date = self.due_date_entry.get()
        task = Task(title, description, due_date)
        self.todo_list.add_task(task)
        self.list_tasks()

    def list_tasks(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for i, task in enumerate(self.todo_list.tasks):
            task_label = tk.Label(self.task_frame, text=f"{i + 1}. {task}")
            task_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
