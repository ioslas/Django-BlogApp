# Django Blog Application
![Java](https://img.shields.io/badge/Language-Python-C0D727)
![Django](https://img.shields.io/badge/Django-4.2.11-darkgreen)
![Version](https://img.shields.io/badge/Version-1.0-orange)
![Status](https://img.shields.io/badge/Status-In_Progress-yellow)

This is a web application built using the **Django framework (v4.2.11)** and **Python 3.9**.  
Its main purpose is to provide basic **blog management functionality**, including *post creation, editing, delete, etc*.

## Features
- Dynamic URL routing & views
- **CRUD** operations on blog posts
- Display posts in **list view** and **detailed view**
- HTML templating with dynamic rendering
- User-friendly URLs using *slugs*
- **Django ORM** and **SQLite database**
- **Admin interface** for management
- **User authentication** (for post creation)
- *Automatic date/time* stamps for posts
- **Search/filter** functionality

## Technologies
- *Python 3.9* -> **core programming language**   
- *Django 4.2.11* -> **web framework** for building the application
- *HTML/CSS* -> **front-end template** structure 
- *SQLite* -> **default DB** (relational database)
- *Django ORM* – **Object-Relational Mapper** for handling database operations
- *Bootstrap* -> for responsive **styling**
- *Django Templating Engine* –> for **rendering dynamic** content in *HTML*
- *Django Admin Panel* – **built-in interface** to manage posts and users 

## Installation & Setup
1. **Clone the repository** (or download the files and create a folder with the repository name)  
```bash 
git clone https://github.com/username/project_name.git
cd project_name
```
2. **Create and activate a virtual environment**
   - **Unzip** the *.rar* file (needs to be downloaded)
   ```bash
   myBlog\Scripts\activate
   ```
   - (Optional)
   ```bash
   # Windows
   py -m venv env
   env/bin/activate

   # Linux
   python -m venv env
   source env/bin/activate
   ```
3. **Install Django in the virtual environment**
   ```bash
   py -m pip install django
   ```
   **Note**: if it needs upgrade, it will you give the message and the recommended command
   
4. **Apply migrations** (Optional)
   ```bash
   cd django_blog
   # Windows
   py manage.py migrate

   # Linux
   python manage.py migrate
   ```
5. 
6.  
