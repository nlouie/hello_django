# Creating your first hello world in Django

## Requirements
- python3
- pip

## Dependencies
- django
- jinja

## Setting up the package
### Install dependencies
    `$ pip install requirements.txt`
### Setting up a virtural environment
Create a virtual environment for our django project

 1. Install virtualenv if you have not already
        `$ pip install virtualenv`
 2. Create the new virtual environment `/django-env`
        `$ virtualenv django-env -p usr/bin/python3`
 3. Activate python source
        `$ django-env/bin/.activate`
#### Installing django
    `pip install django`
    For this project I will use jinja as my templating engine.
    `pip install django-jinja`

### Starting a New Project

#### Creating a project
    `$ django-admin.py startproject <project-name>`
    `$ cd <project-name>`
#### Running a Django Server
    `$ python manage.py runserver`

#### Adding a new app
    `$ python manage.py startapp <app-name>`
