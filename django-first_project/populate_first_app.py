import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import User
from faker import Faker
# script to populate data using Faker

fakegen = Faker()

def add_user(first_name, last_name, email):
    u = User.objects.get_or_create(first_name = first_name, last_name = last_name, email = email)[0]
    u.save()

def populate(N=8):
    for i in range(N):
        f_name = fakegen.first_name()
        l_name = fakegen.last_name()
        email = fakegen.email()
        add_user(f_name,l_name,email)

if __name__ == "__main__":
    print("Start populating dummy data into database")
    populate(10)
    print("Data populated into database successfully..")

