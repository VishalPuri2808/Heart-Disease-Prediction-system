# Heart Disease Prediction System

## Overview
This project is a **Heart Disease Prediction System** developed using **Machine Learning** and **Django**. The system predicts the likelihood of a patient having heart disease based on various medical parameters using the **Decision Tree Classifier**. It also incorporates the **Random Forest Algorithm** for model validation. The project includes a **web-based interface** built with **HTML, CSS, and JavaScript**, with Django handling the backend.

## Features
- **User Registration & Authentication** (Patients & Doctors)
- **Heart Disease Prediction** using Machine Learning (Decision Tree & Random Forest)
- **Patient Appointment Booking System**
- **Doctors' Dashboard** to manage appointments
- **Patient Record Management**
- **Web Application Interface** for user interaction

## Technologies Used
### Backend:
- **Django** (Python Web Framework)
- **Pandas** (Data Handling)
- **Scikit-learn** (Machine Learning)

### Frontend:
- **HTML, CSS, JavaScript** (User Interface Design)

### Database:
- **CSV Files** (for storing user and patient records)

## Installation and Setup
### Prerequisites:
- Python 3.x
- Django
- Pandas
- Scikit-learn
- Streamlit

### Steps to Run the Project:
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/heart-disease-prediction.git
   cd heart-disease-prediction
   ```
2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run Django migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Start the Django server:**
   ```bash
   python manage.py runserver
   ```
6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`

## How It Works
1. **User Registration/Login:** Patients and doctors can sign up and log in to the system.
2. **Data Input:** Patients provide their medical details, which are used for prediction.
3. **Machine Learning Model:** The system uses a Decision Tree model to classify heart disease risk.
4. **Result Display:** The prediction result (Positive/Negative) is displayed on the patient dashboard.
5. **Doctor Appointment:** Patients can book appointments with doctors based on their location.
6. **Doctor Dashboard:** Doctors can view and manage patient appointments.

## Dataset
- The system uses a dataset (`dataset.csv`) containing medical attributes such as **age, sex, cholesterol levels, blood pressure, heart rate**, and more.
- Predictions are made based on these attributes using the **Decision Tree Classifier**.

## Model Performance
- The model was evaluated using **accuracy score**.
- Random Forest was used as a secondary algorithm to verify the predictions.

## Future Enhancements
- Implement a **database (PostgreSQL/MySQL)** instead of CSV files.
- Improve the **User Interface** with a modern design.
- Add **more machine learning models** for better accuracy.
- Enable **email notifications** for doctor appointments.
- Deploy the application on a **cloud server**.

## Contributing
Feel free to contribute to this project by submitting issues, suggesting features, or making pull requests.

## License
This project is licensed under the **MIT License**.

---
**Developed by:** Vishal Mohan Puri  
**Email:** pmvishal2808@gmail.com

