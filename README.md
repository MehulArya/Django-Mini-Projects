# Django-Mini-Projects
Trying to learn Django from projects and documenting what did I learn from each project.

# Hello Pages App — Phase 1: Core Django Syntax

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
