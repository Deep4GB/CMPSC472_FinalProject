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

# Variables to hold the current reminders
current_general_reminders = []
current_medications = []
current_appointments = []

# Clear the reminder lists before loading from JSON files
current_general_reminders.clear()
current_general_reminders.extend(load_reminders('data/general_reminders.json'))

current_medications.clear()
current_medications.extend(load_reminders('data/medications.json'))

current_appointments.clear()
current_appointments.extend(load_reminders('data/appointments.json'))

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
    global current_reminders, current_general_reminders, current_medications, current_appointments
    if request.method == 'POST':
        reminder_type = request.form['reminder_type']
        reminder_text = request.form['reminder']
        reminder_time = request.form['time']
        add_reminder(reminder_type, reminder_text, reminder_time)
    return render_template('index.html', current_general=current_general_reminders, current_medications=current_medications, current_appointments=current_appointments, current_reminders=current_reminders)

@app.route('/medication', methods=['GET', 'POST'])
def medication_reminder():
    global current_medications
    
    if request.method == 'POST':
        reminder_type = request.form['reminder_type']
        medication_name = request.form['medication_name']
        medication_dose = request.form['medication_dose']
        # Get a list of reminder times selected by the user
        reminder_times = request.form.getlist('reminder_times')

        # Format the medication details
        medication_details = {
            'medication_name': medication_name,
            'medication_dose': medication_dose,
            'reminder_times': reminder_times
        }

        # Save medication details to the current_medications list
        current_medications.append(medication_details)
        save_reminders('data/medications.json', current_medications)

        # Schedule reminders for each selected time
        for time in reminder_times:
            add_reminder(reminder_type, f"Take {medication_name} ({medication_dose})", time)

    return render_template('medication.html', current_medications=current_medications)

@app.route('/appointment', methods=['POST'])
def add_appointment_reminder():
    if request.method == 'POST':
        reminder_type = request.form['reminder_type']
        reminder_text = request.form['reminder']
        reminder_time = request.form['time']
        add_reminder(reminder_type, reminder_text, reminder_time)
    return render_template('index.html', current_general=current_general_reminders, current_medications=current_medications, current_appointments=current_appointments, current_reminders=current_reminders)


@app.route('/delete_reminder', methods=['POST'])
def delete_reminder():
    reminder_type = request.json['reminder_type']
    index = int(request.json['index'])  # Convert index to integer
    
    if reminder_type == 'general':
        global current_general_reminders
        if 0 <= index < len(current_general_reminders):
            del current_general_reminders[index]  # Delete the specific reminder
            save_reminders('data/general_reminders.json', current_general_reminders)
            current_reminders['general'] = None if not current_general_reminders else current_general_reminders[0]
    elif reminder_type == 'medications':
        global current_medications
        if 0 <= index < len(current_medications):
            del current_medications[index]  # Delete the specific reminder
            save_reminders('data/medications.json', current_medications)
            current_reminders['medications'] = None if not current_medications else current_medications[0]
    elif reminder_type == 'appointments':
        global current_appointments
        if 0 <= index < len(current_appointments):
            del current_appointments[index]  # Delete the specific reminder
            save_reminders('data/appointments.json', current_appointments)
            current_reminders['appointments'] = None if not current_appointments else current_appointments[0]
    return jsonify({'success': True})


# Variable to hold health metrics
health_metrics = []

# Function to add health metrics
def add_health_metrics(blood_pressure, heart_rate, other_metric):
    global health_metrics
    metrics = {
        'blood_pressure': blood_pressure,
        'heart_rate': heart_rate,
        'other_metric': other_metric  # Add more metrics as needed
    }
    health_metrics.append(metrics)

@app.route('/health', methods=['GET', 'POST'])
def health_tracker():
    if request.method == 'POST':
        blood_pressure = request.form['blood_pressure']
        heart_rate = request.form['heart_rate']
        other_metric = request.form['other_metric']
        add_health_metrics(blood_pressure, heart_rate, other_metric)
    
    return render_template('health.html', health_metrics=health_metrics)


if __name__ == '__main__':
    app.run(debug=True)
