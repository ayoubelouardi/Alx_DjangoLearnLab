# Library Management System

A Django-based web application for managing books, libraries, and user roles.

## Features

- **Authentication**: User registration, login, logout
- **Role-Based Access**: Admin, Librarian, Member roles
- **Book Management**: CRUD operations for books
- **Library Relationships**: Manage books, authors, and libraries

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Access at `http://127.0.0.1:8000/`

## Project Structure

- `LibraryProject/` - Django project config
- `bookshelf/` - Book CRUD operations
- `relationship_app/` - User profiles, roles, relationships

## Models

- **Book**: title, author, published_date, isbn
- **Author**: name, biography
- **Library**: name, location
- **UserProfile**: extends User with role field

## URLs

- `/books/` - List books
- `/library/<id>/` - Library details
- `/login/`, `/logout/`, `/register/` - Auth
- `/admin/`, `/librarian/`, `/member/` - Role views
- `/book/add/`, `/book/<id>/edit/`, `/book/<id>/delete/` - Book operations
