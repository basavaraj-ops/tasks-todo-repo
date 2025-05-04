# Django Task Management API

A Django-based RESTful Task Management System to create, read, update, and delete tasks. Built using Django and Django REST Framework, with support for an admin interface, full API documentation, and clear project structure.

---

##  Features

- CRUD operations for tasks
- RESTful API using Django REST Framework
- Admin interface for managing tasks
- Filtering, searching, and ordering
- Easy setup and extensible codebase

---

##  Tech Stack

- Python 3.x
  pip install python 
- Django
  pip install Django
- Django REST Framework
- SQLite3 (default)
- HTML (Admin Panel)
- Postman (for API testing)

---

## Installation steps

# 1. Clone the repository (or download it)
git clone https://github.com/basavaraj-ops/task-.git 
cd task-manager

# 2. Create and activate a virtual environment
python -m venv env
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate

# 3. Install the required packages
pip install -r requirements.txt

# 4. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create a superuser for admin access
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver


##  Project Setup

### `manage.py`
This file is used to execute Django's command-line tasks. You can use it for running the server, applying migrations, and performing other administrative actions.

### `requirements.txt`
This file contains a list of Python packages that your project depends on. You can install all dependencies by running:
```bash
pip install -r requirements.txt


### 1. Clone the Repository

```bash
git clone https://github.com/basavaraj-ops/task-.git 
cd task-manager
