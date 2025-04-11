# Artisan Academy

## 📌 Project Overview

Artisan Academy is a web-based platform that connects artisans with students, allowing artisans to create profiles, offer courses, and manage their content while students can enroll and learn from skilled professionals.

## 🚀 Features

- **User Authentication**: Separate registration and login for students and artisans.
- **Profile Management**: Artisans can create and manage their profiles.
- **Course Management**: Artisans can post courses, and students can enroll.
- **Student Dashboard**: View registered courses.
- **Artisan Dashboard**: Manage created courses.
- **Admin Panel**: Manage users, courses, and enrollments.

## 🛠 Tech Stack

- **Backend:** Django (Python), Django ORM
- **Database:** MySQL
- **Frontend:** HTML, CSS (Bootstrap)
- **Version Control:** Git & GitHub

## 📥 Installation & Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/JeromeMberia/Artisan-Academy.git
   ```

   ```sh
   cd artisan-academy
   ```

2. Create a virtual environment & activate it:

   ```sh
   python -m venv venv
   ```

   ```sh
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Create the database 'artisan_db'

    - In `MySQL 8.0 Command Line Client` type

    ```sh
    CREATE DATABASE artisan_db;
    ```

    ```sh
    CREATE USER 'artisan_user'@'localhost' IDENTIFIED BY 'password';
    ```

    ```sh
    GRANT ALL PRIVILEGES ON artisan_db.* TO 'artisan_user'@'localhost';
    ```

5. Configure `.env` for MySQL database:

    ```env
    SECRET_KEY = 'django-insecure-5hq09nbv%4t074u%g+h6xj!m2m@vr3zkstxzl7sl9(0i+hus5^'
    DEBUG = True
    ENGINE = 'django.db.backends.mysql'
    NAME = 'artisan_db'
    USER = 'artisan_user'
    PASSWORD = 'password'
    HOST = 'localhost'
    PORT = 3307
    ```

6. Run migrations:

   ```sh
   python manage.py migrate
   ```

7. Create a superuser (for admin access):

   ```sh
   python manage.py createsuperuser
   ```

8. Run the server:

   ```sh
   python manage.py runserver
   ```

## 📂 Project Structure

```bash
artisan-academy/
│── artisan_academy/       # Main Django project files
│── users/                 # User authentication & profiles
│── students/              # Student-related functionality
│── artisans/              # Artisan-related functionality
│── courses/               # Course management
│── templates/             # HTML templates
│── static/                # CSS, JS, images
│── db.sqlite3             # Database file (if using SQLite)
│── manage.py              # Django management script
└── .env                   # Environment variables
```

## 🌟 Future Improvements

- Implement payment integration for premium courses.
- Add messaging system between students and artisans.
- Improve UI with modern design frameworks.

## 🤝 Contributing

1. Fork the repository.
2. Create a new branch:

   ```sh
   git checkout -b feature-branch
   ```

3. Make your changes and commit:

   ```sh
   git commit -m "Added new feature"
   ```

4. Push to your branch:

   ```sh
   git push origin feature-branch
   ```

5. Open a pull request.
