import json
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stylish To-Do App")
        self.root.geometry("500x500")
        
        self.tasks = []
        self.load_tasks()
        
        self.create_header()
        self.create_widgets()
        self.create_footer()

    def create_header(self):
        header = ttk.Frame(self.root, padding=(10, 10))
        header.pack(fill=tk.X)

        title = ttk.Label(header, text="My To-Do List", font=("Helvetica", 24, "bold"), bootstyle="primary")
        title.pack()

    def create_widgets(self):
        self.task_entry = ttk.Entry(self.root, bootstyle="info")
        self.task_entry.pack(pady=10, padx=10, fill=tk.X)

        add_task_button = ttk.Button(self.root, text="Add Task", command=self.add_task, bootstyle="success")
        add_task_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, height=15, bg="white", font=("Helvetica", 12))
        self.task_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        complete_task_button = ttk.Button(self.root, text="Complete Task", command=self.complete_task, bootstyle="primary")
        complete_task_button.pack(pady=5)

        delete_task_button = ttk.Button(self.root, text="Delete Task", command=self.delete_task, bootstyle="danger")
        delete_task_button.pack(pady=5)

        self.load_task_list()

    def create_footer(self):
        footer = ttk.Frame(self.root, padding=(10, 10))
        footer.pack(side=tk.BOTTOM, fill=tk.X)

        footer_label = ttk.Label(footer, text="Powered by Python & Tkinter", bootstyle="dark")
        footer_label.pack()

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append({"task": task_text, "completed": False})
            self.save_tasks()
            self.load_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]['completed'] = True
            self.save_tasks()
            self.load_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to complete.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.save_tasks()
            self.load_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def load_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✔️" if task['completed'] else "❌"
            self.task_listbox.insert(tk.END, f"{status} {task['task']}")

    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []

if __name__ == "__main__":
    root = ttk.Window(themename="darkly")
    app = ToDoApp(root)
    root.mainloop()
