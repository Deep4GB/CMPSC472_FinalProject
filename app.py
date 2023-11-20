from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import datetime

app = Flask(__name__)

# Data files path
MEDICATION_FILE = 'data/medications.json'
REMINDERS_FILE = 'data/reminders.json'
APPOINTMENTS_FILE = 'data/appointments.json'
HEALTH_DATA_FILE = 'data/health_data.json'

# Check and create data files if they don't exist
for file in [MEDICATION_FILE, REMINDERS_FILE, APPOINTMENTS_FILE, HEALTH_DATA_FILE]:
    try:
        with open(file, 'r') as f:
            pass
    except FileNotFoundError:
        with open(file, 'w') as f:
            json.dump([], f)

# Load data from files
def load_data(file):
    with open(file, 'r') as f:
        return json.load(f)

# Save data to files
def save_data(data, file):
    with open(file, 'w') as f:
        json.dump(data, f)

@app.route('/')
def index():
    medications = load_data(MEDICATION_FILE)
    reminders = load_data(REMINDERS_FILE)
    appointments = load_data(APPOINTMENTS_FILE)
    health_data = load_data(HEALTH_DATA_FILE)
    return render_template('index.html', medications=medications, reminders=reminders, appointments=appointments, health_data=health_data)

@app.route('/add_medication', methods=['POST'])
def add_medication():
    medication_name = request.form.get('medication_name')
    dosage = request.form.get('dosage')
    medications = load_data(MEDICATION_FILE)
    medications.append({"medication_name": medication_name, "dosage": dosage})
    save_data(medications, MEDICATION_FILE)
    return redirect(url_for('index'))

@app.route('/add_reminder', methods=['POST'])
def add_reminder():
    reminder_text = request.form.get('reminder_text')
    reminder_time = request.form.get('reminder_time')
    reminders = load_data(REMINDERS_FILE)
    reminders.append({"reminder_text": reminder_text, "reminder_time": reminder_time})
    save_data(reminders, REMINDERS_FILE)
    return redirect(url_for('index'))

@app.route('/add_appointment', methods=['POST'])
def add_appointment():
    appointment_info = request.form.get('appointment_info')
    appointment_time = request.form.get('appointment_time')
    appointments = load_data(APPOINTMENTS_FILE)
    appointments.append({"appointment_info": appointment_info, "appointment_time": appointment_time})
    save_data(appointments, APPOINTMENTS_FILE)
    return redirect(url_for('index'))

@app.route('/add_health_data', methods=['POST'])
def add_health_data():
    health_metric = request.form.get('health_metric')
    health_time = request.form.get('health_time')
    health_data = load_data(HEALTH_DATA_FILE)
    health_data.append({"timestamp": health_time, "health_metric": health_metric})
    save_data(health_data, HEALTH_DATA_FILE)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
