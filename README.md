<h2 align="center"> ━━━━━━  ❖  ━━━━━━ </h2>
<h1 align="center"> Elderly Reminders and Health Tracker </h1>

<div align="center">
   <p></p>
   <a href="https://github.com/Deep4GB">
     <img src="https://github.com/Deep4GB.png" width="50px">
   </a>
     <a href="https://github.com/devv64bit">
    <img src="https://github.com/devv64Bit.png?size=50" width="50px">
   </a>
   </a>
</div>
<h3 align="center"> Members: Deep Patel and Dev Patel</h5>

## Table of Contents
- [Installation and Usage Instructions](#installation-and-usage-instructions)
- [Project Overview](#project-overview)
- [Project Goals](#project-goals)
- [Significance of the Project](#significance-of-the-project)
- [Code Structure](#code-structure)
- [Functionality and Test Results](#functionality-and-test-results)
- [Discussion and Conclusions](#discussion-and-conclusions)

## Installation and Usage Instructions

### Installation
#### 1. Ensure you have Python 3.11.6 installed. You can download Python 3.11.6 from the official Python website: [Python Downloads page](https://www.python.org/downloads/)

#### 2. Clone the repository to your local machine using the following Git command:
```bash
git clone git@github.com:Deep4GB/CMPSC472_FinalProject.git
cd CMPSC472_FinalProject
```
#### 3. Create a Virtual Environment (recommended):
Open the Command Prompt or Terminal and navigate to the project directory using the ``cd`` command.

* Install `virtualenv` (if not installed) :
   ```bash
   pip install virtualenv
   ```

* Activate `virtualenv`:
   ```bash
   virtualenv venv
   ```

- On Windows:
  * Activate the virtual environment
    ```bash
    venv\Scripts\activate
    ```
- On macOS and Linux:
  * Activate the virtual environment
    ```bash
    source venv/bin/activate
    ```
- To deactivate the virtual environment:
  ```bash
  deactivate
  ```
#### 4. Install the required packages using the following command:
```bash
pip install -r requirements.txt
```

#### 5. Run the application using the following command:
```bash
python app.py
```
### Usage Instructions
#
### General Reminders

#### Adding a General Reminder:
- Navigate to the "General Reminders" section.
- Enter the reminder details: reminder text, date, and time in 24-hour format.
- Click "Set Reminder" to add the reminder.

#### Deleting a General Reminder:
- In the list of general reminders, click the "Delete" button next to the reminder you want to remove.
#
### Medication Reminders

#### Adding a Medication Reminder:
- Go to the "Medication Reminders" section.
- Enter medication details: name, dose, date, and select reminder times.
- Click "Add Medication Reminder" to add the medication and set reminders.

#### Deleting a Medication Reminder:
- In the list of medication reminders, click the "Delete" button next to the medication you want to remove.
#
### Appointment Reminders

#### Adding an Appointment Reminder:
- Visit the "Appointment Reminders" section.
- Enter appointment details: text, date, and time in 24-hour format.
- Click "Set Appointment Reminder" to add the appointment.

#### Deleting an Appointment Reminder:
- In the list of appointment reminders, click the "Delete" button next to the appointment you want to remove.
#
### Health Metrics Tracking

#### Adding Health Metrics:
- Go to the "Health Tracking" section.
- Enter health metrics: date, blood pressure, heart rate, and an optional additional metric.
- Click "Add Health Metrics" to record the health data.

#### Searching Health Metrics:
- Use the "Search by Date" input to find health metrics for a specific date.
- Click "Search" to display metrics for the selected date.

#### Deleting Health Records:
- In the list of health metrics, click the "Delete" button next to the record you want to remove.
#
### Refreshing Data

- Click on "Check Your Health Metrics!!" to access the Health Metrics page and refresh the data.
#
### Note:

- The time format for reminders is in 24-hour (military) format. Ensure to input the time accordingly; otherwise, the program won't accept the input.
#
### Closing the App

- To stop the application, press Ctrl+C in the terminal where the Flask app is running.
## Project Overview

This project aims to develop a software application designed to assist the elderly in managing their health and daily tasks efficiently. The application serves as a reminder system for medication, appointments, and other crucial tasks. Additionally, it includes a health tracking feature allowing users to input and monitor vital health metrics such as blood pressure and heart rate.

This Flask project incorporates several Operating System (OS) concepts:

1. **Threads:** Utilized for asynchronous tasks, such as scheduling reminders and checking health metrics, to prevent blocking the main application.

2. **File Handling:** Reading and writing JSON files to store and retrieve reminders, medications, appointments, and health metrics.

3. **Synchronization:** Implementing locks (`threading.Lock`) to manage access to shared resources (e.g., reminders and health metrics) to avoid data corruption when multiple threads access them concurrently.

4. **Process Control:** Flask handles multiple HTTP requests and responses as separate processes to manage the web application's functionalities.

5. **Timers and Polling:** Employing time-based functions (`time.sleep()`) for scheduling reminders and continuously checking the current time against scheduled reminder times.

6. **Inter-Process Communication (IPC):** Using HTTP methods like POST, GET, and DELETE for communication between the client (browser) and the server (Flask application) to perform actions like adding reminders, deleting records, and retrieving health metrics.

These concepts work together to facilitate the functioning of the application, manage data, handle user requests, and ensure concurrent operations without conflicts or data loss.

## Project Goals

1. **Enhance Daily Task Management:**
   - **Objective:** Develop a user-friendly interface to enable elderly individuals to easily add, view, and manage daily reminders for tasks, appointments, health metrics, and medication schedules.
   - **Rationale:** Empowering users to organize their daily activities fosters a sense of independence and reduces stress associated with memory lapses.

2. **Facilitate Health Data Tracking:**
   - **Objective:** Implement a system for tracking and recording health metrics, including blood pressure and heart rate, allowing users to monitor their health over time.
   - **Rationale:** Providing a tool for health data tracking contributes to proactive health management and encourages individuals to stay informed about their well-being.

3. **Ensure User-Friendly Interface:**
   - **Objective:** Design a graphical user interface (GUI) that is intuitive, accessible, and tailored to the needs of the elderly population.
   - **Rationale:** An easy-to-use interface ensures that the project is inclusive, accommodating users with varying levels of technological familiarity.

4. **Implement Persistent Data Storage:**
   - **Objective:** Develop mechanisms for persistent storage of reminders and health data, allowing users to access historical information.
   - **Rationale:** Persistent storage ensures that users can review past information, aiding in continuity of care and promoting long-term health tracking.

5. **Support Caregiver Collaboration:**
   - **Objective:** Provide features that allow caregivers to remotely view and manage reminders, fostering collaboration and support for elderly individuals.
   - **Rationale:** Inclusion of caregiver features ensures a holistic approach to elderly care, involving family members or support networks in the well-being of the user.

6. **Promote Mental Health Awareness:**
   - **Objective:** Implement features that encourage users and caregivers to stay aware of mental health through health data trends and proactive reminders.
   - **Rationale:** By promoting mental health awareness, the project contributes to a holistic approach to well-being, considering both physical and mental health aspects.

7. **Bridge Generational Digital Divide:**
   - **Objective:** Introduce technology in a manner that is accessible to older individuals, bridging the digital divide and ensuring inclusivity.
   - **Rationale:** Making technology accessible fosters social connection, reduces isolation, and encourages the elderly to engage with modern tools for their benefit.

8. **Create a Collaborative Health Ecosystem:**
   - **Objective:** Establish a platform that encourages collaboration among users, caregivers, and healthcare professionals, creating a supportive health ecosystem.
   - **Rationale:** Collaboration ensures a comprehensive approach to health management, involving multiple stakeholders for the benefit of the elderly individual.


## Significance of the Project

1. **Improved Quality of Life:**
   - The project addresses the specific needs of the elderly by providing a user-friendly interface for managing reminders and health data.
   - By assisting in the organization of daily tasks and health-related information, the project contributes to an improved quality of life for the elderly.

2. **Enhanced Independence:**
   - Empowering the elderly to manage their reminders and health metrics fosters a sense of independence.
   - The ability to add, view, and delete reminders or track health metrics autonomously promotes self-sufficiency.

3. **Reduced Anxiety and Stress:**
   - The project helps in minimizing the anxiety and stress associated with memory lapses or missed appointments.
   - Reminders serve as proactive prompts, alleviating concerns about forgetting essential tasks or medications.

4. **Positive Impact on Mental Health:**
   - Providing a centralized platform for health data tracking allows individuals and their caregivers to monitor trends over time.
   - This feature aids in maintaining mental health awareness, fostering a proactive approach to well-being.

5. **Facilitation of Caregiver Support:**
   - The project supports caregivers in ensuring the well-being of their elderly loved ones.
   - Caregivers can remotely view and manage reminders, offering a collaborative and supportive approach to elderly care.

6. **Integration of Technology and Social Connection:**
   - The project introduces technology in a user-friendly manner, bridging the digital divide for older individuals.
   - It incorporates features that encourage social connections, such as shared health data or collaborative reminders.

## Code Structure

### The code is structured as follows:

**app.py:**

- Implements a Flask web application to manage reminders and health metrics.
- Defines routes for different functionalities (add, delete, display reminders, health tracker).
- Uses JSON files to store reminders and health metrics.

**index.html:**
- This structured HTML file ensures a clear organization of the user interface components, including forms for adding reminders, displaying existing reminders, and facilitating user interaction.
- The use of Tailwind CSS contributes to a visually appealing and responsive design.
- The integrated JavaScript enhances the user experience by allowing the deletion of reminders without the need for page refresh.

**health.html:**
- This structured HTML file is made for health metrics page of the app. 
- It has container for health tracking with a reminder card, health tracking form for adding metrics, search feature for filtering metrics by date, list displaying existing health metrics, and javascript functions for searching, displaying, and deleting health records.

**Note:**

- Data Storage:

  * Reminders are stored in text files (`reminders.txt`, `health_data.txt`) in main.py.
  * Reminders are stored as JSON files (`general_reminders.json`, `medications.json`, `appointments.json`) in app.py.

**Communication:**
- The `app.py` script uses Flask to create a web interface and the logic is implemented in there.

- The `index.html` file is the main page of the web application. It contains the HTML code for the web interface. It is frontend of the program.

- The `health.html` file is the health metrics page of the web application. It contains the HTML code for the web interface. It is frontend of the program.

This outline provides an overview of the code structure, highlighting key functions, data storage, and the interaction between different components.


## Functionality and Test Results

### Functionalities
#### 1. **Reminder Management:**
  - **Functionality:**
     - Users can add reminders for tasks and appointments.
     - Reminders are displayed in an organized manner.
     - Users can delete reminders.
  - **Test Results:**
     - **Add Reminder:** Successfully added reminders for various tasks.
     - **Display Reminders:** Reminders displayed accurately in the form of notification.
     - **Delete Reminder:** Successfully deleted reminders without errors.
   ![Alt text](Images/image.png)
   ![Alt text](Images/image-4.png)
   ![Alt text](Images/image-5.png)
#### 2. **Health Data Tracking:**
  - **Functionality:**
     - Users can input and track health metrics (blood pressure, heart rate).
     - Health data is displayed clearly.
     - Historical health data can be accessed.
  - **Test Results:**
     - **Input Health Metrics:** Successfully inputted various health metrics.
     - **Display Health Data:** Health data displayed accurately in the web app.
     - **Access Historical Data:** Successfully accessed and reviewed historical health data.
   ![Alt text](Images/Health_Tracking.png)

#### 3. **User-Friendly Web GUI:**
  - **Functionality:**
     - Web app is designed to be intuitive and accessible.
     - Clear navigation for all functionalities.
  - **Test Results:**
     - **Intuitiveness:** Users found the application easy to navigate and understand.
     - **Accessibility:** application accommodates varying levels of technological familiarity.
   ![Alt text](Images/image-1.png)
   ![Alt text](Images/image-2.png)
   ![Alt text](Images/image-3.png)
#### 4. **Bridging Digital Divide:**
   - **Functionality:**
     - Technology introduced in an accessible manner.
     - User-friendly design for older individuals.
   - **Test Results:**
     - **Accessibility:** Users of varying technological familiarity successfully engaged with the system.
     - **Inclusivity:** Project successfully bridged the digital divide.

## Discussion and Conclusions

### Project Issues and Limitations:

During the development process, the team encountered a few challenges and limitations, including:
- Integration complexities while synchronizing reminders with different time zones.
- Ensuring a seamless user experience across various devices and screen sizes.

### Application of Course Learnings:

The project benefited significantly from the learnings acquired during the course:
- Implemented robust algorithms for reminder notifications based on scheduling principles learned in class.
- Employed secure authentication methods and data encryption techniques covered in course modules.
- Implemented OS concepts such as threads, file handling, and synchronization to ensure concurrent operations without data loss.

### Future Improvements:

For future iterations, the following enhancements or features could be considered:
- Incorporating AI-based predictive analysis for health trends based on input health metrics.
- Implementing a more intuitive and customizable user interface to cater to individual preferences.


<h3 align="center"> ━━━━━━ End of Document ━━━━━━ </h3>
