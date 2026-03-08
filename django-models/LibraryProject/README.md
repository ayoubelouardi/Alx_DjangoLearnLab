# LibraryProject – Introduction to Django

## Objective
Gain familiarity with **Django** by setting up a Django development environment and creating a basic Django project.  
This task introduces you to the workflow of Django projects, including project creation and running the development server.

---

## Task Description
- Install Django and create a new project named **LibraryProject**.
- Explore the project’s default structure to understand the roles of various components.
- Run the development server and view the default Django welcome page.

---

## Steps

### 1. Install Django
Ensure Python is installed on your system.  
Install Django using pip:

```
pip install django
```

### 2. Create Your Django Project
Run the following command to create a new Django project named **LibraryProject**:

```
django-admin startproject LibraryProject
```

### 3. Run the Development Server
Navigate into your project directory:

```
cd LibraryProject
```

Create a `README.md` file inside the **LibraryProject** directory.  
Start the development server:

```
python manage.py runserver
```

Open a web browser and go to:

```
http://127.0.0.1:8000/
```

You should see the default Django welcome page.

### 4. Explore the Project Structure
Key files to review:
- **`settings.py`** → Configuration for the Django project.
- **`urls.py`** → URL declarations; acts as the “table of contents” for your site.
- **`manage.py`** → Command-line utility to interact with the Django project.

---

## Resources
- [Django Official Documentation](https://docs.djangoproject.com/en/stable/)
- [MDN Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)

---
