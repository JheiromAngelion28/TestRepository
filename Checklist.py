import tkinter as tk
from tkinter import ttk

def toggle_task(button):
    """Toggle the task completion state and change button color."""
    current_color = button.cget("bg")
    if current_color == "lightgray":
        button.config(bg="lightgreen", text="Completed")
    else:
        button.config(bg="lightgray", text="Incomplete")

# Task list
tasks = [
    "Power",
    "Screens",
    "OBS",
    "Arm video Files",
    "Mic Test",
    "Organ test (Skip if needed)",
    "Camera test",
    "Powerpoint test (If live)",
    "Confirm time of start",
    "Confirm Live or no",
    "Test Sequence"
]

# Initialize the main window
root = tk.Tk()
root.title("Task Checklist")
root.geometry("400x400")

title_label = tk.Label(root, text="Task Checklist", font=("Times new roman", 14, "bold"))
title_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

# Create the task buttons
buttons = []
for task in tasks:
    task_frame = tk.Frame(frame)
    task_frame.pack(fill="x", padx=10, pady=2)
    
    task_label = tk.Label(task_frame, text=task, anchor="w", width=25, font=("Times new roman", 14, "bold"))
    task_label.pack(side="left")
    
    task_button = tk.Button(task_frame, text="Incomplete", bg="lightgray" )
    task_button.config(command=lambda b=task_button: toggle_task(b))
    task_button.pack(side="right")
    
    buttons.append(task_button)

# Run the Tkinter event loop
root.mainloop()