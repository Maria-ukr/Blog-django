# News & Blog Web Application (Django)

A full-stack web application built with **Django**, featuring a custom blog/news system, media file management, and a pre-configured Django Admin panel with saved articles and images.

## Project Structure

```text
web-django/
├── blog/               # Blog & articles application
├── main/               # Main pages, routing, and static assets
├── news/               # Core project settings and URL configurations
├── media/              # Uploaded article images
├── db.sqlite3          # Pre-populated SQLite database
├── manage.py           # Django management script
└── requirements.txt    # Project dependencies
```

## Features

- **Content Management:** Create, edit, and delete articles via the built-in Django Admin panel.
- **Media Handling:** Full support for image uploads and rendering (`media/`).
- **Ready-to-Use Data:** Includes a pre-populated `db.sqlite3` database and media assets so the application works immediately upon setup.

---

## 🚀 Step-by-Step Local Setup

Open your terminal in the root project folder (`web-django`, where `manage.py` is located) and run the following commands in order:

### Step 1. Clone the repository
```bash
git clone 
cd web-django
```

### Step 2. Create a virtual environment
```bash
python -m venv .venv
```

### Step 3. Activate the virtual environment
Choose the command that matches your operating system and terminal:

* **Windows (Git Bash):**
  ```bash
  source .venv/Scripts/activate
  ```

* **Windows (PowerShell):**
  ```bash
  .venv\Scripts\Activate.ps1
  ```

* **Windows (Command Prompt / CMD):**
  ```bash
  .venv\Scripts\activate.bat
  ```

* **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

### Step 4. Install dependencies
```bash
pip install -r requirements.txt
```

### Step 5. Apply migrations (Optional)
Since the pre-populated `db.sqlite3` database is already included, you can skip this or run it to verify everything is up to date:
```bash
python manage.py migrate
```

### Step 6. Run the local development server
```bash
python manage.py runserver
```

---

## Accessing the Application

Once the server is running, open your browser and navigate to:

- **Main Website:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### 💡 Admin Panel Login
- **Username:** `admin` *(ask me for the username)*
- **Password:** `your_password` *(ask me for the password, or create a new user via `python manage.py createsuperuser`)*