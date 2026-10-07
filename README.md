# Django To-Do App

A simple and user-friendly **To-Do List web application** built using **Python and Django**.

This project allows users to manage their daily tasks by adding, completing, editing, and deleting tasks.

## Features

* Add new tasks
* Mark tasks as completed
* Undo completed tasks
* Edit existing tasks
* Delete tasks
* Filter tasks:

  * All
  * Pending
  * Completed
* Clear all completed tasks
* Task statistics:

  * Total tasks
  * Pending tasks
  * Completed tasks
* Clean and responsive interface

## Technologies Used

* **Python**
* **Django**
* **HTML**
* **CSS**
* **SQLite**
* **Git & GitHub**

## Project Structure

```text
ToDo/
│
├── manage.py
├── db.sqlite3
├── .gitignore
│
├── todo/
│   ├── migrations/
│   ├── static/
│   │   └── todo/
│   │       └── style.css
│   ├── templates/
│   │   └── todo/
│   │       ├── index.html
│   │       └── edit.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
└── todo_project/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/PrinceKumar829/ToDo.git
```

### 2. Open the project

```bash
cd ToDo
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

For macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install Django

```bash
pip install django
```

### 6. Apply migrations

```bash
python3 manage.py migrate
```

### 7. Start the development server

```bash
python3 manage.py runserver
```

### 8. Open the application

Open this in your browser:

```text
http://127.0.0.1:8000/
```

## Future Improvements

Some features that can be added in the future:

* User authentication
* Due dates for tasks
* Task priority
* Categories
* Search functionality
* Dark mode
* Better mobile UI
* REST API
* Deployment to a cloud platform

## Author

**Prince Kumar**

GitHub: https://github.com/PrinceKumar829

## License

This project is created for learning and educational purposes.
