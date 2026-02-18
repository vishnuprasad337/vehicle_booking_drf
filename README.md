
Vehicle Inventory & Booking System (Django REST API)

A complete Vehicle Inventory & Booking REST API built using Django and Django REST Framework.
This project demonstrates backend development skills including API design, validations, business logic, filtering, and deployment readiness.Here i give more importance to api structuring rather than user templates

1. Project Overview

The system allows users to:

Manage vehicles (CRUD operations)

Create vehicle bookings with real-life validation rules

Prevent double bookings

Automatically calculate booking cost

Filter vehicles by brand, fuel type, and availability


2. Tech Stack

Python 3.x

Django

Django REST Framework

SQLite 

python-dotenv

3. installation guide

python --version
python -m venv venv
venv\Scripts\activate
pip install djangorestframework
pip install python-dotenv

4. migration comands
python manage.py makemigrations
python manage.py migrate

5. run the project
python manage.py runserver

6. test apis
base urls http://127.0.0.1:8000/
http://127.0.0.1:8000/api/vehicles

7. api end ponints
http://127.0.0.1:8000/api/vehicles/ #list and post vehicle
http://127.0.0.1:8000/api/vehicles/1 #list based on id
http://127.0.0.1:8000/api/bookings # list and post bookings
http://127.0.0.1:8000/api/bookings/1 # booking based on id

8. sample json booking

{
    "id": 1,
    "customer_name": "Vishnu Prasad",
    "customer_phone": "9123456780",
    "start_date": "2026-03-05",
    "end_date": "2026-03-08",
    "total_amount": "15000.00",
    "vehicle": 2
}

