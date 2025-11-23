import json
import os
from datetime import datetime

DATA_FILE = "appointments.json"


class Appointment:
    def __init__(self, patient_name, doctor_name, date, time, contact):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.date = date
        self.time = time
        self.contact = contact

    def to_dict(self):
        return {
            "patient_name": self.patient_name,
            "doctor_name": self.doctor_name,
            "date": self.date,
            "time": self.time,
            "contact": self.contact,
        }


def load_appointments():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_appointments(appointments):
    with open(DATA_FILE, "w") as f:
        json.dump(appointments, f, indent=2)


def book_appointment():
    patient_name = input("Enter patient name: ")
    doctor_name = input("Enter doctor name: ")
    date = input("Enter appointment date (YYYY-MM-DD): ")
    time = input("Enter appointment time (HH:MM): ")
    contact = input("Enter contact number: ")
    new_appointment = Appointment(patient_name, doctor_name, date, time, contact)
    appointments = load_appointments()
    appointments.append(new_appointment.to_dict())
    save_appointments(appointments)
    print("Appointment booked successfully.")


def view_appointments():
    appointments = load_appointments()
    if not appointments:
        print("No appointments found.")
        return
    for i, app in enumerate(appointments, 1):
        print(f"\nAppointment {i}")
        print(f"Patient Name: {app['patient_name']}")
        print(f"Doctor Name: {app['doctor_name']}")
        print(f"Date: {app['date']}")
        print(f"Time: {app['time']}")
        print(f"Contact: {app['contact']}")


def cancel_appointment():
    appointments = load_appointments()
    if not appointments:
        print("No appointments to cancel.")
        return
    view_appointments()
    idx = input("\nEnter appointment number to cancel: ")
    if not idx.isdigit() or int(idx) < 1 or int(idx) > len(appointments):
        print("Invalid selection.")
        return
    appointments.pop(int(idx) - 1)
    save_appointments(appointments)
    print("Appointment cancelled.")


def main_menu():
    while True:
        print("\nClinic Appointment Booking System")
        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. Cancel Appointment")
        print("4. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            book_appointment()
        elif choice == "2":
            view_appointments()
        elif choice == "3":
            cancel_appointment()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main_menu()
