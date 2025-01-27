import tkinter as tk
from tkinter import messagebox, filedialog
import json

# Initialize Window
root = tk.Tk()
root.title("Task Manager")
root.geometry("400x500")

tasks = []  # List to store tasks

# Define Functions
def add_task():
    task = task_entry.get() # Get text from entry box
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        tasks.pop(selected_task_index)
    except IndexError:
        messagebox.showwarning("Delete Error", "No task selected!")

def save_tasks():
    with filedialog.asksaveasfile(defaultextension=".json", filetypes=[("JSON Files", "*.json")]) as file:
        json.dump(tasks, file)
        messagebox.showinfo("Save Success", "Tasks saved successfully!")

def load_tasks():
    global tasks
    file = filedialog.askopenfile(mode='r', filetypes=[("JSON Files", "*.json")])
    if file:
        tasks = json.load(file)
        task_listbox.delete(0, tk.END)
        for task in tasks:
            task_listbox.insert(tk.END, task)

# Widgets
task_entry = tk.Entry(root, width=35)
task_entry.pack(pady=10)

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=20)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_button.pack(pady=5)

load_button = tk.Button(root, text="Load Tasks", command=load_tasks)
load_button.pack(pady=5)

# Run the Application
root.mainloop()
