import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.config(bg="white")

tasks = []

# Functions
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

def mark_done():
    try:
        selected = listbox.curselection()[0]
        task = tasks[selected] + " ✅"
        tasks[selected] = task
        listbox.delete(selected)
        listbox.insert(selected, task)
    except:
        messagebox.showwarning("Warning", "Select a task to mark done!")

# Title
title_label = tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"), bg="#f5f5f5")
title_label.pack(pady=10)

# Listbox
listbox = tk.Listbox(root, width=40, height=15, bd=0, font=("Arial", 12))
listbox.pack(pady=10)

# Entry box
task_entry = tk.Entry(root, font=("Arial", 12))
task_entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, width=10, bg="#4CAF50", fg="white")
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, width=10, bg="#f44336", fg="white")
delete_button.grid(row=0, column=1, padx=5)

done_button = tk.Button(button_frame, text="Mark Done", command=mark_done, width=10, bg="#2196F3", fg="white")
done_button.grid(row=0, column=2, padx=5)

root.mainloop()
