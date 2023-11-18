import tkinter as tk
from tkinter import messagebox

reminders = []
health_data = []
reminders_frame = None
reminders_text = None
health_data_frame = None
health_data_text = None

def add_reminder():
    global reminders_frame, reminders_text
    reset_frames()
    reminders_frame.pack()

    reminder_time_label = tk.Label(reminders_frame, text="Time (HH:MM):")
    reminder_time_label.pack()
    reminder_time_entry = tk.Entry(reminders_frame)
    reminder_time_entry.pack()

    reminder_desc_label = tk.Label(reminders_frame, text="Description:")
    reminder_desc_label.pack()
    reminder_desc_entry = tk.Entry(reminders_frame)
    reminder_desc_entry.pack()

    def save_reminder():
        time = reminder_time_entry.get()
        description = reminder_desc_entry.get()
        if time and description:
            reminders.append((time, description))
            messagebox.showinfo("Success", "Reminder added successfully!")
            update_reminders_display()
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
    global health_data_frame, health_data_text
    reset_frames()
    health_data_frame.pack()

    health_metric_label = tk.Label(health_data_frame, text="Health Metric:")
    health_metric_label.pack()
    health_metric_entry = tk.Entry(health_data_frame)
    health_metric_entry.pack()

    health_value_label = tk.Label(health_data_frame, text="Value:")
    health_value_label.pack()
    health_value_entry = tk.Entry(health_data_frame)
    health_value_entry.pack()

    def save_health_data():
        metric = health_metric_entry.get()
        value = health_value_entry.get()
        if metric and value:
            health_data.append((metric, value))
            messagebox.showinfo("Success", "Health data added successfully!")
            update_health_data_display()
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

    health_data_frame = tk.Frame(root)
    health_data_frame.pack(pady=10)
    health_data_text = tk.Text(health_data_frame, height=5, width=50)

    button_add_reminder = tk.Button(root, text="Add Reminder", command=add_reminder)
    button_add_reminder.pack()

    button_display_reminders = tk.Button(root, text="Display Reminders", command=display_reminders)
    button_display_reminders.pack()

    button_add_health_data = tk.Button(root, text="Add Health Data", command=add_health_data)
    button_add_health_data.pack()

    button_display_health_data = tk.Button(root, text="Display Health Data", command=display_health_data)
    button_display_health_data.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
