import datetime
import subprocess
import threading
import time
import json
from flask import Flask, render_template, request, jsonify
from plyer import notification

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
current_reminders = {'general': None,
                     'medications': None, 'appointments': None}


def add_reminder_with_date(reminder_type, reminder_text, reminder_date, reminder_time):
    global current_general_reminders, current_appointments

    reminder_datetime = datetime.datetime.strptime(
        f"{reminder_date} {reminder_time}", "%Y-%m-%d %H:%M")
    current_time = datetime.datetime.now()

    if reminder_datetime > current_time:
        reminder = (reminder_text,
                    reminder_datetime.strftime('%Y-%m-%d %H:%M'))

        if reminder_type == 'general':
            current_general_reminders.append(reminder)
            save_reminders('data/general_reminders.json',
                           current_general_reminders)
        elif reminder_type == 'appointments':
            current_appointments.append(reminder)
            save_reminders('data/appointments.json', current_appointments)

        # Schedule reminders for the specified date and time
        thread = threading.Thread(target=schedule_notification, args=(
            reminder_type, reminder_text, reminder_date, reminder_time))  # Pass reminder_type here
        thread.daemon = True
        thread.start()


def schedule_notification(reminder_type, reminder_text, reminder_date, reminder_time):
    while True:
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.strftime('%Y-%m-%d')
        current_time = current_datetime.strftime('%H:%M')

        if current_date == reminder_date and current_time == reminder_time:
            notification_title = 'Reminder'
            if reminder_type == 'general':
                notification_text = f"Do not forget: {reminder_text}"
            elif reminder_type == 'appointments':
                notification_text = f"Appointment reminder: {reminder_text}"
            elif reminder_type == 'medication':
                notification_text = f"Medication reminder: {reminder_text}"

            notification.notify(
                title=notification_title,
                message=notification_text,
                app_name="Reminder App",
                timeout=10  # Notification timeout in seconds
            )
            break

        time.sleep(1)


# Updated route to handle adding reminders with date and time
@app.route('/', methods=['GET', 'POST'])
def index():
    global current_general_reminders, current_medications, current_appointments

    if request.method == 'POST':
        reminder_type = request.form['reminder_type']
        reminder_text = request.form['reminder']
        reminder_date = request.form['date']  # Get the date from the form
        reminder_time = request.form['time']

        add_reminder_with_date(reminder_type, reminder_text,
                               reminder_date, reminder_time)

    return render_template('index.html', current_general=current_general_reminders, current_medications=current_medications, current_appointments=current_appointments)


@app.route('/medication', methods=['GET', 'POST'])
def medication_reminder():
    global current_medications

    if request.method == 'POST':
        reminder_type = request.form['reminder_type']
        medication_name = request.form['medication_name']
        medication_dose = request.form['medication_dose']
        reminder_date = request.form['date']  # Get the date from the form
        # Get a list of reminder times selected by the user
        reminder_times = request.form.getlist('reminder_times')

        # Format the medication details
        medication_details = {
            'medication_name': medication_name,
            'medication_dose': medication_dose,
            'reminder_date': reminder_date,  # Include the reminder date
            'reminder_times': reminder_times
        }

        # Save medication details to the current_medications list
        current_medications.append(medication_details)
        save_reminders('data/medications.json', current_medications)

        # Schedule reminders for each selected time
        for time in reminder_times:
            add_reminder_with_date(
                reminder_type, f"Take {medication_name} ({medication_dose})", reminder_date, time)

    return render_template('index.html', current_medications=current_medications)


@app.route('/appointment', methods=['POST'])
def add_appointment_reminder():
    global current_appointments

    if request.method == 'POST':
        reminder_type = request.form['reminder_type']
        reminder_text = request.form['reminder']
        reminder_date = request.form['date']  # Get the date from the form
        reminder_time = request.form['time']

        add_reminder_with_date(reminder_type, reminder_text,
                               reminder_date, reminder_time)

    return render_template('index.html', current_general=current_general_reminders, current_medications=current_medications, current_appointments=current_appointments)


@app.route('/delete_reminder', methods=['POST'])
def delete_reminder():
    reminder_type = request.json['reminder_type']
    index = int(request.json['index'])

    if reminder_type == 'general':
        global current_general_reminders
        if 0 <= index < len(current_general_reminders):
            del current_general_reminders[index]
            save_reminders('data/general_reminders.json',
                           current_general_reminders)
    elif reminder_type == 'medications':
        global current_medications
        if 0 <= index < len(current_medications):
            del current_medications[index]
            save_reminders('data/medications.json', current_medications)
    elif reminder_type == 'appointments':
        global current_appointments
        if 0 <= index < len(current_appointments):
            del current_appointments[index]
            save_reminders('data/appointments.json', current_appointments)

    return jsonify({'success': True})


# --------------------------Health Page--------------------------

# Function to load health metrics from JSON file
def load_health_metrics(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save health metrics to JSON file


def save_health_metrics(file_name, health_metrics):
    with open(file_name, 'w') as file:
        json.dump(health_metrics, file)


# Load health metrics once when the app starts
health_metrics = load_health_metrics('data/health_data.json')

# Function to handle health metrics


def add_health_metrics(blood_pressure, heart_rate, other_metric, health_date):
    global health_metrics
    metrics = {
        'blood_pressure': blood_pressure,
        'heart_rate': heart_rate,
        'other_metric': other_metric,
        'health_date': health_date  # Include the health date
    }
    health_metrics.append(metrics)
    save_health_metrics('data/health_data.json', health_metrics)

# Flask route for health metrics with search functionality


@app.route('/health', methods=['GET', 'POST'])
def health_tracker():
    global health_metrics

    if request.method == 'POST':
        blood_pressure = request.form['blood_pressure']
        heart_rate = request.form['heart_rate']
        other_metric = request.form['other_metric']
        # Retrieve the health date from the form
        health_date = request.form['date']

        # Add health metrics along with the date
        add_health_metrics(blood_pressure, heart_rate,
                           other_metric, health_date)
        # Reload the health metrics after adding new data
        health_metrics = load_health_metrics('data/health_data.json')

    # Search health metrics by date if a date parameter is present in the request
    search_date = request.args.get('date')
    if search_date:
        filtered_metrics = [
            metric for metric in health_metrics if metric['health_date'] == search_date]
        return jsonify(filtered_metrics)

    return render_template('health.html', health_metrics=health_metrics)


if __name__ == '__main__':
    app.run(debug=True)
