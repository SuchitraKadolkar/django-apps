# django-apps
Created basic Django-apps which cover all basic concepts using conda in Linux environment.

Here below are basic useful commands that I have used:
  1. bash Anaconda3-2024.02-1-Linux-x86_64.sh 
  2. conda
  3. source activate <env_name>
  4. django-admin startproject <project_name>
  5. django-admin startapp <app_name>
  6. Then go to project directory you have created and run the application using
     - python manage.py runserver

Commands for migration:
  1. python manage.py migrate
  2. python manage.py makemigrations <app_name>
  3. python manage.py migrate
  4. python manage.py runserver

   
django-first-project => In this project, I have created basic first Django project.

django_url_template => In this project, I have created separate url.py for each application and this urls.py fils path included in main urls.py

db_admin_project => In this project, I have created simple database(sqlite) 

django_graphql => In this project, I have implemented Django with GraphQL.
