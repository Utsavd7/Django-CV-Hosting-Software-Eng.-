<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Convert CV to HTML using Django Template - README</title>
</head>
<body>
    <h1>Convert CV to HTML using Django Template</h1>
    
    <h2>Overview</h2>
    <p>The goal of this assignment was to create an HTML version of my CV using Django's templating system. The CV content was dynamically rendered in the template by passing context from the Django view.</p>
    
    <h2>Technologies Used</h2>
    <ul>
        <li>Python 3</li>
        <li>Django Web Framework</li>
        <li>HTML5</li>
        <li>CSS3</li>
    </ul>
    
    <h2>Installation and Setup</h2>
    
    <h3>Step 1: Set Up Your Django Project</h3>
    <ol>
        <li>
            <p><strong>Install Django:</strong> Make sure you have Django installed in your Python environment. You can install it using pip if you haven't already:</p>
            <pre><code>pip install django</code></pre>
        </li>
        <li>
            <p><strong>Create a Django Project:</strong> Create a new Django project by running the following command:</p>
            <pre><code>django-admin startproject my_cv_project</code></pre>
            <p>Replace <code>my_cv_project</code> with your desired project name.</p>
        </li>
        <li>
            <p><strong>Create a Django App:</strong> Navigate to your project directory and create a new app named <code>cv</code>:</p>
            <pre><code>
cd my_cv_project
python manage.py startapp cv
            </code></pre>
        </li>
        <li>
            <p><strong>Add the App to Installed Apps:</strong> Open <code>my_cv_project/settings.py</code> and add <code>'cv'</code> to the <code>INSTALLED_APPS</code> list.</p>
        </li>
    </ol>
    
    <h3>Step 2: Create a Django Template for Your CV</h3>
    <ol>
        <li><p><strong>Create a Template Directory:</strong> Inside your <code>cv</code> app, create a folder named <code>templates</code> and within it, create another folder named <code>cv</code>. The path should look like this: <code>cv/templates/cv</code>.</p></li>
        <li><p><strong>Create a CV Template:</strong> Inside the <code>cv/templates/cv</code> folder, create a file named <code>cv.html</code>. This file will contain the HTML structure of your CV.</p></li>
    </ol>
    
    <h3>Step 3: Create a View to Render Your CV</h3>
    <ol>
        <li><p><strong>Create a View:</strong> Open the <code>cv/views.py</code> file and create a view function to render your CV.</p></li>
    </ol>
    
    <h3>Step 4: Configure URLs</h3>
    <ol>
        <li><p><strong>Create a URL Configuration:</strong> Create a new file named <code>urls.py</code> in the <code>cv</code> app directory.</p></li>
        <li><p><strong>Include the App URLs in the Project URLs:</strong> Open <code>my_cv_project/urls.py</code> and include the <code>cv</code> app URLs.</p></li>
    </ol>
    
    <h3>Step 5: Run Your Django Development Server</h3>
    <ol>
        <li><p><strong>Run the Django development server to see your CV rendered as HTML:</strong></p>
            <pre><code>python manage.py runserver</code></pre>
        </li>
        <li><p>Then, open a web browser and go to <a href="http://127.0.0.1:8000/cv/">http://127.0.0.1:8000/cv/</a> to see your CV in HTML format.</p></li>
    </ol>
</body>
</html>
