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

## Notes App — Phase 2: Models, Forms, and Full CRUD with CBVs

**Concepts covered:**
- Django models and database persistence
- Django ORM basics (`objects.all()`, `get()`, `get_object_or_404`)
- ModelForms (`forms.py`) and form–model binding
- Class-Based Views (CBVs): `View`, `ListView`
- URL parameters and dynamic routing (`<int:id>`)
- GET vs POST handling inside CBVs
- Reusing the same form for Create & Update
- Using `instance` to update existing objects
- Safe delete patterns (confirmation + POST only)
- Redirects using URL `name` instead of template paths

---

### Features implemented (CRUD)

#### 1. List Notes (Read — List)
- Implemented using `generic.ListView`
- Automatically fetches all `Note` objects
- Custom `context_object_name` used in template

**Flow:**  
URL → ListView → ORM query → Template → Browser

---

#### 2. View Single Note (Read — Detail)
- Implemented using a custom `View`
- Note fetched via URL parameter (`title_id`)
- Used `get_object_or_404` for safety

**Key learning:**  
How URL parameters are passed to views and why `get_object_or_404` is preferred over `.get()`.

---

#### 3. Create Note (Create)
- Implemented using a custom `View`
- Uses `ModelForm` (`BasicForm`) from `forms.py`
- Handles:
  - `GET` → render empty form
  - `POST` → validate & save note
- Redirects after successful POST (PRG pattern)

**Key learning:**  
Why `forms.save()` works only with `ModelForm` and why redirecting after POST prevents duplicate submissions.

---

#### 4. Edit Note (Update)
- Uses the same form as Create
- Existing note passed using `instance=note`
- Handles:
  - `GET` → form pre-filled with existing data
  - `POST` → updates the same database row

**Key learning:**  
Difference between creating a new object vs updating an existing one using `instance`.
---

#### 5. Delete Note (Delete)
- Implemented with a confirmation page
- Deletion happens **only on POST**
- Redirects after successful delete

**Key learning:**  
Why delete operations must never happen on GET requests and how to design safe delete flows.

---

### Project structure (Notes App)
notes/
├── models.py

├── forms.py

├── views.py

├── urls.py

└── templates/notes/

├── list.html

├── detail_view.html

├── create_blog.html

├── edit_blog.html

└── confirm_delete.html


---

### Outcome

Built a complete **CRUD application** using Django fundamentals without shortcuts.

By the end of this phase:
- I can confidently move data between **URL → View → Form → Model → Template**
- I understand how Django handles requests internally
- I can reason about bugs instead of guessing syntax
- I can build real Django apps instead of demo pages

