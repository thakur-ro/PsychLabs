import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
import json

# Load existing patient data
DATA_FILE = "data/patients.json"
data = []

st.title("Psychlabs")

# Sidebar for navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Dashboard", "Add Patient", "View Patients", "Appointment Scheduler"])

if section == "Dashboard":
    st.subheader("Welcome back!")
    st.write("Use the sidebar to manage your patients and appointments.")
    
    # Sample data
    appointments = [
        {"id": 1, "name": "John Doe", "date": datetime.now() - timedelta(days=2)},
        {"id": 2, "name": "Jane Smith", "date": datetime.now() + timedelta(days=3)},
        {"id": 3, "name": "Alice Brown", "date": datetime.now() - timedelta(days=5)},
        {"id": 4, "name": "Bob White", "date": datetime.now() + timedelta(days=1)},
    ]

    # Convert data to a DataFrame
    df = pd.DataFrame(appointments)

    # Separate past and upcoming appointments
    current_time = datetime.now()
    past_appointments = df[df["date"] < current_time]
    upcoming_appointments = df[df["date"] >= current_time]
    
    # Streamlit tabs
    tab1, tab2 = st.tabs(["Past Appointments", "Upcoming Appointments"])

    # Past Appointments
    with tab1:
        if not past_appointments.empty:
            st.table(past_appointments)
        else:
            st.write("No past appointments.")

    # Upcoming Appointments
    with tab2:
        if not upcoming_appointments.empty:
            st.table(upcoming_appointments)
        else:
            st.write("No upcoming appointments.")

elif section == "Add Patient":
    st.subheader("Add a New Patient")
    with st.form("patient_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=1, max_value=120)
        contact = st.text_input("Contact Details")
        history = st.text_area("Medical History")
        submitted = st.form_submit_button("Add Patient")
    
    if submitted:
        data.append({
            "name": name,
            "age": age,
            "contact": contact,
            "history": history,
            "sessions": []
        })
        st.success(f"Patient {name} added successfully!")

elif section == "View Patients":
    st.subheader("Patient Records")
    if data:
        for patient in data:
            st.write(f"### {patient['name']}")
            st.write(f"Age: {patient['age']}")
            st.write(f"Contact: {patient['contact']}")
            st.write(f"History: {patient['history']}")
            st.write("---")
    else:
        st.warning("No patient records found.")

elif section == "Appointment Scheduler":
    st.subheader("Schedule Appointments")
    st.write("Feature under development...")

# Footer
st.sidebar.write("Made with Patience by Rohit")