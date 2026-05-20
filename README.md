# Bethal ERP - School Management System

Bethal ERP is a modern Django-based School Management System designed to manage students, teachers, attendance, examinations, fees, and timetable operations through a clean and professional web interface.

---

# Features

## Authentication & Role Management
- Secure Login System
- Logout Functionality
- Role-Based Access Control
- Custom User Model
- Roles:
  - Admin
  - Teacher
  - Student
  - Parent

---

# Student Management
- Add Students
- Edit Student Details
- Delete Students
- Student Profile Pictures
- Search Students
- Pagination System

---

# Attendance Management
- Mark Attendance
- Present / Absent Status
- Attendance Records
- Attendance Dashboard UI

---

# Examination System
- Add Exam Results
- Multiple Subject Marks
- Auto Total Calculation
- Percentage Calculation
- Grade Calculation
- Printable Report Cards

---

# Timetable Management
- Class-Based Timetable
- Teacher Assignment
- Day-Wise Schedule
- Student Timetable Access
- Modern Timetable UI

---

# Dashboard System
- Modern ERP Dashboard
- Analytics Cards
- Quick Actions
- Responsive UI
- Sidebar Navigation
- Bootstrap Icons Integration

---

# Technologies Used

## Backend
- Django
- Python
- SQLite

## Frontend
- HTML5
- CSS3
- Bootstrap 5
- Bootstrap Icons
- Google Fonts

---

# Project Structure

```bash
school_erp/
│
├── accounts/
├── students/
├── attendance/
├── fees/
├── exams/
├── timetable/
│
├── templates/
├── media/
├── static/
│
├── config/
├── manage.py
└── db.sqlite3
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/Mugilan-11/School_erp_system.git
```

## 2. Move Into Project

```bash
cd school_erp
```

## 3. Create Virtual Environment

```bash
python -m venv env
```

## 4. Activate Virtual Environment

### Windows

```bash
env\Scripts\activate
```

### Linux / Mac

```bash
source env/bin/activate
```

## 5. Install Dependencies

```bash
pip install django pillow
pip install crispy-bootstrap5
pip install django-crispy-forms
```

## 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## 7. Create Superuser

```bash
python manage.py createsuperuser
```

## 8. Run Server

```bash
python manage.py runserver
```

---

# Default URL

```bash
http://127.0.0.1:8000/
```

---

# Main Modules

| Module | Description |
|---|---|
| Accounts | Authentication and role management |
| Students | Student CRUD management |
| Attendance | Attendance tracking system |
| Fees | Fee collection and payment records |
| Exams | Multi-subject result management |
| Timetable | Class-wise timetable management |

---

# Django Concepts Used

- Custom User Model
- Authentication System
- Role-Based Access
- CRUD Operations
- Model Forms
- Template Inheritance
- ForeignKey Relationships
- Pagination
- Media File Handling
- Dynamic URL Routing
- Django ORM
- Bootstrap UI Integration

---

# Current Features Completed

- Modern Login Page
- Professional ERP Dashboard
- Sidebar Navigation
- Student Management
- Attendance System
- Examination System
- Timetable System
- Report Card Printing
- Modern Responsive UI
- GitHub Integration

---

# Future Improvements

- Teacher Management Module
- Parent Portal
- Student Portal
- Assignment Upload System
- Notifications System
- Email/SMS Integration
- Analytics Charts
- Online Fee Payments
- PDF Exports
- API Integration

---

# Screenshots

Add screenshots here later.

---

# Author

Developed by B Mugilan

---

# License

This project is for educational and learning purposes.
