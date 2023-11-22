import datetime
import subprocess
import threading
import time
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Function to load reminders from JSON files
def load_reminders(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save reminders to JSON files
def save_reminders(file_name, reminders):
    with open(file_name, 'w') as file:
        json.dump(reminders, file)

# Function to load journal entries from JSON file
def load_journal_entries():
    try:
        with open('data/journal_entries.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save journal entries to JSON file
def save_journal_entry(entry):
    journal_entries = load_journal_entries()
    journal_entries.append(entry)
    with open('data/journal_entries.json', 'w') as file:
        json.dump(journal_entries, file)

# Variables to hold the current reminders
current_general_reminders = load_reminders('data/general_reminders.json')
current_medications = load_reminders('data/medications.json')
current_appointments = load_reminders('data/appointments.json')

# Dictionary to hold the current reminders
current_reminders = {'general': None, 'medications': None, 'appointments': None}

# Function to schedule notification for reminders
def schedule_notification(reminder_text, reminder_time):
    while True:
        current_time = datetime.datetime.now().strftime('%H:%M')  # Get current time in 24-hour format
        if current_time == reminder_time:
            notification_title = 'Reminder'
            notification_text = f"Don't forget: {reminder_text}"
            subprocess.run(['osascript', '-e', f'display notification "{notification_text}" with title "{notification_title}"'])
            break
        # Check every second
        time.sleep(1)

# Function to add a reminder
def add_reminder(reminder_type, reminder_text, reminder_time):
    global current_reminders
    reminder = (reminder_text, reminder_time)
    if reminder_type == 'general':
        current_reminders['general'] = reminder
        current_general_reminders.append(reminder)
        save_reminders('data/general_reminders.json', current_general_reminders)
    elif reminder_type == 'medications':
        current_reminders['medications'] = reminder
        current_medications.append(reminder)
        save_reminders('data/medications.json', current_medications)
    elif reminder_type == 'appointments':
        current_reminders['appointments'] = reminder
        current_appointments.append(reminder)
        save_reminders('data/appointments.json', current_appointments)

    # Start a thread for the new reminder
    thread = threading.Thread(target=schedule_notification, args=(reminder_text, reminder_time))
    thread.daemon = True
    thread.start()

@app.route('/', methods=['GET', 'POST'])
def index():
    global current_reminders
    if request.method == 'POST':
        reminder_type = request.form['reminder_type']
        reminder_text = request.form['reminder']
        reminder_time = request.form['time']
        add_reminder(reminder_type, reminder_text, reminder_time)
    current_journal_entries = load_journal_entries()
    return render_template('index.html', current_general=current_general_reminders, current_medications=current_medications, current_appointments=current_appointments, current_reminders=current_reminders, current_journal_entries=current_journal_entries)

@app.route('/delete_reminder', methods=['POST'])
def delete_reminder():
    reminder_type = request.json['reminder_type']
    if reminder_type == 'general':
        global current_general_reminders
        current_general_reminders = []
        save_reminders('data/general_reminders.json', current_general_reminders)
        current_reminders['general'] = None
    elif reminder_type == 'medications':
        global current_medications
        current_medications = []
        save_reminders('data/medications.json', current_medications)
        current_reminders['medications'] = None
    elif reminder_type == 'appointments':
        global current_appointments
        current_appointments = []
        save_reminders('data/appointments.json', current_appointments)
        current_reminders['appointments'] = None
    return jsonify({'success': True})

@app.route('/save_journal_entry', methods=['POST'])
def save_journal_entry_route():
    entry = request.json.get('entry')
    date = datetime.datetime.now().strftime('%Y-%m-%d')  # Get current date in YYYY-MM-DD format

    journal_entry = {'date': date, 'entry': entry}
    save_journal_entry(journal_entry)
    
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
