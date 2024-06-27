def display_menu():
    print("\nTo-Do List")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            status = "Done" if task['completed'] else "Not Done"
            print(f"{i + 1}. {task['description']} - {status}")

def add_task(tasks):
    description = input("Enter the task description: ")
    tasks.append({'description': description, 'completed': False})

def update_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]['description'] = input("Enter the new description: ")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
    else:
        print("Invalid task number.")

def mark_task_completed(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]['completed'] = True
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            mark_task_completed(tasks)
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
        self.root.title("To-Do List")

        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.task_listbox = tk.Listbox(self.frame, height=15, width=50)
        self.task_listbox.pack(side=tk.LEFT)
        
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.complete_task)
        self.complete_button.pack()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append({'description': task, 'completed': False})
            self.update_task_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task['completed'] else "Not Done"
            self.task_listbox.insert(tk.END, f"{task['description']} - {status}")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_description = self.entry.get()
            if new_description:
                self.tasks[selected_task_index[0]]['description'] = new_description
                self.update_task_listbox()
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a new description.")
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]]['completed'] = True
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()




