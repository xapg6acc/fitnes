# Fitness App

Django project for fitness tracking


## Installation

Python3 must be installed

```shell
git clone https://github.com/LaskoA/FitnessApp
cd FitnessApp

Virtual environment install for Windows:
  - python3 -m venv venv
  - source venv/bin/activate
  - pip install -r requirements.txt
  
Virtual environment install for Mac:
  - sudo pip install virtualenv
  - virtualenv env
  - source env/bin/activate

pip install -r requirements.txt  
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Current endpoints

- http://127.0.0.1:8000/admin/
- http://127.0.0.1:8000/app/shapes/
- http://127.0.0.1:8000/app/days/
- http://127.0.0.1:8000/app/exercises/
- http://127.0.0.1:8000/app/muscles/
- http://127.0.0.1:8000/app/trainings/

Adding of "id" to each endpoint (for example, http://127.0.0.1:8000/app/trainings/1/) will redirect you to detail page

## Access

user for test: admin
password: admin12345
