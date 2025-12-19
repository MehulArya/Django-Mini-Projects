# Django-Mini-Projects
Trying to learn Django from projects and documenting what did I learn from each project.

## Hello Pages App — Phase 1: Core Django Syntax

**Concepts covered:**  
- URL routing: project-level & app-level (`''` = root path)  
- Views: `HttpResponse` and `render()`  
- Templates: app-based structure (`app_name/templates/app_name/`)  
- Base templates & inheritance: `{% block %}` / `{% extends %}`  
- Common mistakes: wrong path, wrong import, block name mismatch  

**Project structure:**

pages/

├── urls.py

├── views.py

└── templates/pages/

├── base.html

└── home.html


**Outcome:**  
Visiting `root/` renders the home page with base layout. Demonstrates the full flow: URL → View → Template → Browser.

## Guess / Feedback App — Phase 1: Forms, GET vs POST

**Concepts covered:**
- HTML forms and browser request behavior
- GET vs POST requests (`request.GET` vs `request.POST`)
- Form field handling using `name` attributes
- CSRF protection for POST requests (`{% csrf_token %}`)
- Context passing from view to template
- Post-Redirect-Get (PRG) pattern using redirects
- Debugging techniques (URL params, print statements)

**Flow implemented:**
- GET request renders the form
- POST request processes user input
- Successful POST redirects to a GET URL with query parameters
- GET request displays the submitted value safely

**Outcome:**
Built a secure form-based app that handles user input correctly, avoids duplicate submissions, and follows Django’s recommended request-handling pattern.

