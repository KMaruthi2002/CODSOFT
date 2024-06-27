# todo_list_gui.py

import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        # Create frames
        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(padx=10, pady=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(padx=10, pady=10)

        # Create task list
        self.task_list = tk.Listbox(self.task_frame, width=40)
        self.task_list.pack(side=tk.LEFT, padx=10, pady=10)

        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.task_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_list.yview)

        # Create task entry field
        self.task_entry = tk.Entry(self.button_frame, width=40)
        self.task_entry.pack(padx=10, pady=10)

        # Create buttons
        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.update_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.save_button = tk.Button(self.button_frame, text="Save List", command=self.save_list)
        self.save_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.load_button = tk.Button(self.button_frame, text="Load List", command=self.load_list)
        self.load_button.pack(side=tk.LEFT, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a task")

    def update_task(self):
        task_num = self.task_list.curselection()
        if task_num:
            task_num = task_num[0]
            new_task = self.task_entry.get()
            if new_task:
                self.task_list.delete(task_num)
                self.task_list.insert(task_num, new_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Please enter a new task")
        else:
            messagebox.showerror("Error", "Please select a task to update")

    def delete_task(self):
        task_num = self.task_list.curselection()
        if task_num:
            task_num = task_num[0]
            self.task_list.delete(task_num)
        else:
            messagebox.showerror("Error", "Please select a task to delete")

    def save_list(self):
        with open("todo_list.txt", "w") as f:
            for i in range(self.task_list.size()):
                f.write(self.task_list.get(i) + "\n")
        messagebox.showinfo("Success", "To-Do List saved successfully")

    def load_list(self):
        try:
            with open("todo_list.txt", "r") as f:
                tasks = [line.strip() for line in f.readlines()]
                self.task_list.delete(0, tk.END)
                for task in tasks:
                    self.task_list.insert(tk.END, task)
            messagebox.showinfo("Success", "To-Do List loaded successfully")
        except FileNotFoundError:
            messagebox.showerror("Error", "To-Do List file not found")

root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()
