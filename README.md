<html>
<h1>Convert CV to HTML using Django Template </h1>

This project is a demonstration of converting a CV (resume) into an HTML page using Django's templating system. The CV content is dynamically rendered in the template by passing context from the Django view.

<h2>Overview</h2>

The goal of this assignment was to create an HTML version of my CV using Django's templating system. The CV content was dynamically rendered in the template by passing context from the Django view.

<h2>Technologies Used</h2>

Python 3
Django Web Framework
HTML5
CSS3

<h2>Installation and Setup</h2>

Step 1: Set Up Your Django Project
1) Install Django: Make sure you have Django installed in your Python environment. You can install it using pip if you haven't already:
bash
pip install django

2) Create a Django Project: Create a new Django project by running the following command:
bash
django-admin startproject my_cv_project
Replace my_cv_project with your desired project name.

3) Create a Django App: Navigate to your project directory and create a new app named cv:
bash
cd my_cv_project
python manage.py startapp cv

4) Add the App to Installed Apps: Open my_cv_project/settings.py and add 'cv' to the INSTALLED_APPS list


Step 2: Create a Django Template for Your CV
1) Create a Template Directory: Inside your cv app, create a folder named templates and within it, create another folder named cv. The path should look like this: cv/templates/cv.
2) Create a CV Template: Inside the cv/templates/cv folder, create a file named cv.html. This file will contain the HTML structure of your CV.


Step 3: Create a View to Render Your CV
1) Create a View: Open the cv/views.py file and create a view function to render your CV.


Step 4: Configure URLs
1) Create a URL Configuration: Create a new file named urls.py in the cv app directory.
2) Include the App URLs in the Project URLs: Open my_cv_project/urls.py and include the cv app URLs


Step 5: Run Your Django Development Server
1) Run the Django development server to see your CV rendered as HTML:

bash
Copy code
python manage.py runserver
2) Then, open a web browser and go to http://127.0.0.1:8000/cv/ to see your CV in HTML format.
</html>


