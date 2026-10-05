# TaskFlow – Smart To-Do Management System

![TaskFlow Screenshot](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

TaskFlow is a modern, responsive, and fully functional To-Do Management System built with **Django** and **Tailwind CSS**. It is designed to act as a premium SaaS productivity application with a focus on UI/UX, robust backend architecture, and seamless user experience.

This project was built for a 3rd-year college presentation to demonstrate a thorough understanding of Django fundamentals, ORM queries, authentication, and templating.

## 🌟 Key Features

* **Secure User Authentication**: Full registration, login, and logout capabilities leveraging Django's robust built-in authentication system.
* **Strict Data Isolation**: Each authenticated user has their own private dashboard. You cannot access or modify tasks belonging to other users.
* **Smart Dashboard**: 
  * Interactive statistics cards calculating Total, Pending, and Completed tasks.
  * Real-time completion progress tracking.
* **Task Management (CRUD)**: Create, Read, Update, and Delete tasks seamlessly via beautifully designed modal dialogues without navigating away from the dashboard.
* **Dynamic Views & Filtering**: Easily filter tasks by "Today", "Upcoming", or "Completed". Advanced filtering by Priority and Category, alongside text-based searching.
* **Interactive UI**: Built with Tailwind CSS via CDN, featuring smooth transitions, auto-dismissing toast notifications, and a responsive sidebar for mobile devices.
* **Dark Mode**: Fully supported, persistent dark/light mode toggle.
* **Django Admin Integration**: Fully registered models allow administrators to manage users and tasks from a dedicated backend interface.

---

## 🛠️ Technology Stack

* **Backend**: Python 3.x, Django 5.x/6.x
* **Database**: SQLite (default)
* **Frontend**: HTML5, Django Templates, Tailwind CSS (CDN), Vanilla JavaScript
* **Icons**: Lucide Icons (CDN)

---

## 🚀 Getting Started (Local Setup)

To get a local copy up and running, follow these simple steps.

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/taskflow.git
cd taskflow
```

### 2. Set up the virtual environment
```bash
python -m venv venv
```
Activate the environment:
* **Windows**: `.\venv\Scripts\activate`
* **Mac/Linux**: `source venv/bin/activate`

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Populate Sample Data (Optional)
To quickly see the application in action without manually creating data, you can run the provided population script:
```bash
python populate_db.py
```
*This will create a demo user (`Username: demo`, `Password: password123`) with sample tasks across different categories.*

### 6. Create an Admin User (Optional)
To access the Django Admin panel:
```bash
python manage.py createsuperuser
```
*(Follow the prompts to set your username and password)*

### 7. Run the development server
```bash
python manage.py runserver
```

Open your browser and navigate to **`http://127.0.0.1:8000`**.

---

## 📂 Project Structure

```text
taskflow/
│
├── manage.py                # Django's command-line utility
├── populate_db.py           # Custom script to inject sample data
├── requirements.txt         # Project dependencies
├── .gitignore               # Files ignored by git
│
├── taskflow/                # Main project configuration folder
│   ├── settings.py          # Project settings
│   ├── urls.py              # Root URL configurations
│   └── ...
│
└── tasks/                   # The main Task application
    ├── models.py            # Database schema (Task model)
    ├── views.py             # Request handlers and business logic
    ├── forms.py             # UserRegistrationForm & TaskForm
    ├── urls.py              # App-level routing
    ├── context_processors.py# Dynamic notification logic
    ├── templates/tasks/     # HTML templates (base, dashboard, partials, etc.)
    └── static/              # Custom CSS and JavaScript
```

---

## 🎓 Academic Presentation Notes
If you are demonstrating this project, be prepared to highlight:
- The **MVT (Model-View-Template)** architecture.
- How `@login_required` and `user=request.user` secure the views.
- The use of Django `Q()` objects for the search functionality in `views.py`.
- The custom **Context Processor** (`context_processors.py`) used to inject dynamic notifications into `base.html` globally.
- The **Django Admin panel** (`/admin/`), showcasing the backend database tables.
