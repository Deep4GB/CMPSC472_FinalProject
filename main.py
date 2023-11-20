import tkinter as tk
from tkinter import messagebox
import os
import time

reminders = []
health_data = []
reminders_file = "reminders.txt"
health_data_file = "health_data.txt"
reminders_frame = None
reminders_text = None
health_data_frame = None
health_data_text = None
reminder_time_entry = None
reminder_desc_entry = None
health_metric_entry = None
health_value_entry = None

def add_reminder():
    global reminders_frame, reminder_time_entry, reminder_desc_entry
    reset_frames()
    reminders_frame.pack()

    if not reminder_time_entry:
        reminder_time_label = tk.Label(reminders_frame, text="Time (HH:MM AM/PM):")
        reminder_time_label.pack()
        reminder_time_entry = tk.Entry(reminders_frame)
        reminder_time_entry.pack()

    if not reminder_desc_entry:
        reminder_desc_label = tk.Label(reminders_frame, text="Description:")
        reminder_desc_label.pack()
        reminder_desc_entry = tk.Entry(reminders_frame)
        reminder_desc_entry.pack()

    def save_reminder():
        global reminder_time_entry, reminder_desc_entry
        time = reminder_time_entry.get()
        description = reminder_desc_entry.get()
        if time and description:
            reminders.append((time, description))
            messagebox.showinfo("Success", "Reminder added successfully!")
            update_reminders_display()
            save_reminders_to_file()
            reset_entry_fields([reminder_time_entry, reminder_desc_entry])
            # schedule_notification(time, description)  # Uncomment if implementing notifications
        else:
            messagebox.showwarning("Warning", "Please enter both time and description.")

    save_button = tk.Button(reminders_frame, text="Save Reminder", command=save_reminder)
    save_button.pack()

def display_reminders():
    global reminders_frame, reminders_text
    reset_frames()
    reminders_frame.pack()
    reminders_text.pack()
    update_reminders_display()

def add_health_data():
    global health_data_frame, health_metric_entry, health_value_entry
    reset_frames()
    health_data_frame.pack()

    if not health_metric_entry:
        health_metric_label = tk.Label(health_data_frame, text="Health Metric:")
        health_metric_label.pack()
        health_metric_entry = tk.Entry(health_data_frame)
        health_metric_entry.pack()

    if not health_value_entry:
        health_value_label = tk.Label(health_data_frame, text="Value:")
        health_value_label.pack()
        health_value_entry = tk.Entry(health_data_frame)
        health_value_entry.pack()

    def save_health_data():
        global health_metric_entry, health_value_entry
        metric = health_metric_entry.get()
        value = health_value_entry.get()
        if metric and value:
            health_data.append((metric, value))
            messagebox.showinfo("Success", "Health data added successfully!")
            update_health_data_display()
            save_health_data_to_file()
            reset_entry_fields([health_metric_entry, health_value_entry])
        else:
            messagebox.showwarning("Warning", "Please enter both health metric and value.")

    save_button = tk.Button(health_data_frame, text="Save Health Data", command=save_health_data)
    save_button.pack()

def display_health_data():
    global health_data_frame, health_data_text
    reset_frames()
    health_data_frame.pack()
    health_data_text.pack()
    update_health_data_display()

def update_reminders_display():
    global reminders_text
    reminders_text.delete(1.0, tk.END)
    if reminders:
        for reminder in reminders:
            reminders_text.insert(tk.END, f"Time: {reminder[0]}, Description: {reminder[1]}\n")
    else:
        reminders_text.insert(tk.END, "No reminders set.")

def update_health_data_display():
    global health_data_text
    health_data_text.delete(1.0, tk.END)
    if health_data:
        for data in health_data:
            health_data_text.insert(tk.END, f"Metric: {data[0]}, Value: {data[1]}\n")
    else:
        health_data_text.insert(tk.END, "No health data recorded.")

def reset_frames():
    global reminders_frame, reminders_text, health_data_frame, health_data_text
    if reminders_frame:
        reminders_frame.pack_forget()
    if reminders_text:
        reminders_text.pack_forget()
    if health_data_frame:
        health_data_frame.pack_forget()
    if health_data_text:
        health_data_text.pack_forget()

def reset_entry_fields(entries):
    for entry in entries:
        entry.delete(0, tk.END)

def create_gui():
    global reminders_frame, reminders_text, health_data_frame, health_data_text

    root = tk.Tk()
    root.title("Elderly Reminder and Health Tracker")
    root.geometry("600x400")

    label = tk.Label(root, text="Welcome to Elderly Reminder and Health Tracker", font=("Arial", 16))
    label.pack(pady=10)

    reminders_frame = tk.Frame(root)
    reminders_frame.pack(pady=10)
    reminders_text = tk.Text(reminders_frame, height=5, width=50)
    reminders_text.pack()

    health_data_frame = tk.Frame(root)
    health_data_frame.pack(pady=10)
    health_data_text = tk.Text(health_data_frame, height=5, width=50)
    health_data_text.pack()

    button_add_reminder = tk.Button(root, text="Add Reminder", command=add_reminder)
    button_add_reminder.pack()

    button_display_reminders = tk.Button(root, text="Display Reminders", command=display_reminders)
    button_display_reminders.pack()

    button_add_health_data = tk.Button(root, text="Add Health Data", command=add_health_data)
    button_add_health_data.pack()

    button_display_health_data = tk.Button(root, text="Display Health Data", command=display_health_data)
    button_display_health_data.pack()

    load_reminders_from_file()
    load_health_data_from_file()
    root.mainloop()

def save_reminders_to_file():
    try:
        with open(reminders_file, "w") as file:
            for reminder in reminders:
                file.write(f"{reminder[0]},{reminder[1]}\n")
    except IOError as e:
        messagebox.showerror("Error", f"Failed to save reminders: {e}")

def save_health_data_to_file():
    try:
        with open(health_data_file, "w") as file:
            for data in health_data:
                file.write(f"{data[0]},{data[1]}\n")
    except IOError as e:
        messagebox.showerror("Error", f"Failed to save health data: {e}")

def load_reminders_from_file():
    try:
        if os.path.exists(reminders_file):
            with open(reminders_file, "r") as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(",")
                    reminders.append((data[0], data[1]))
    except IOError as e:
        messagebox.showerror("Error", f"Failed to load reminders: {e}")

def load_health_data_from_file():
    try:
        if os.path.exists(health_data_file):
            with open(health_data_file, "r") as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(",")
                    health_data.append((data[0], data[1]))
    except IOError as e:
        messagebox.showerror("Error", f"Failed to load health data: {e}")

# Uncomment and adjust to schedule notifications using an external library like 'plyer'
# def schedule_notification(time, description):
#     pass

if __name__ == "__main__":
    create_gui()
