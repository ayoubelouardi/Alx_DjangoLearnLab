# Deep Dive into Django Models and Views

A comprehensive learning project designed to advance your skills in Django ORM, views, and user authentication.

## Overview

This project focuses on building robust web applications using Django's powerful features. Through hands-on tasks, you will implement complex model relationships, develop both function-based and class-based views, and manage user authentication and permissions.

## Learning Objectives

By the end of this project, you will be able to:

### 1. Implement Advanced Model Relationships in Django
- Master Django's ORM capabilities by creating models that demonstrate:
  - **ForeignKey** relationships
  - **ManyToMany** relationships
  - **OneToOne** relationships
- Effectively model complex data relationships in a Django project

### 2. Develop Django Views and URL Configuration
- Gain proficiency in creating:
  - **Function-based views (FBVs)**
  - **Class-based views (CBVs)**
- Configure URL patterns to handle web requests effectively, routing them to the appropriate views

### 3. Manage User Authentication in Django
- Set up user login, logout, and registration functionalities using Django's built-in authentication system
- Develop views and templates to demonstrate user session and permission management

### 4. Implement Role-Based Access Control in Django
- Extend the Django User model to include user roles
- Create views that restrict access based on these roles
- Utilize Django signals to automatically create a UserProfile when a new user is registered

### 5. Implement Custom Permissions in Django
- Add custom permissions to the Book model to control actions such as:
  - Adding books
  - Editing books
  - Deleting books
- Enforce these permissions in views, ensuring only authorized users can perform specific actions

## Project Duration

- **Start Date:** January 12, 2026
- **End Date:** January 18, 2026

## Prerequisites

- Python 3.x
- Django (latest stable version)
- Basic understanding of Python and web concepts
- Familiarity with HTML/CSS templates

## Getting Started

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the development server: `python manage.py runserver`

## Key Features

- Complex model relationships (ForeignKey, ManyToMany, OneToOne)
- Function-based and Class-based Views
- User authentication (login, logout, registration)
- Role-based access control (RBAC)
- Custom permissions system
- Automatic UserProfile creation using Django signals

## License

This is a learning project for educational purposes.
