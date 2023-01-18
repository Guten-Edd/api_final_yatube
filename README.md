# Yatube API
**pet project**
### Short overview:
A social networking API where users can post and view other users' posts. The mechanism of comments to records, the possibility of subscribing to publications of interest to authors, and user registration have been implemented. A JWT token is used for authentication. Tools were used in the project:
Python3, Django, DjangoORM, DjangoREST Framework, SQLite.

## How to start
### The first thing to do is to clone the repository:
```sh
git clone git@github.com:Guten-Edd/api_final_yatube.git
cd api_final_yatube
```
### Create a virtual environment to install dependencies in and activate it:
```sh
python3 -m venv venv
source venv/bin/activate
```
### Then install the dependencies:
```sh
pip install --upgrade pip
pip install -r requirements.txt
```
### Create database and apply migrations:
```sh
cd yatube_api
python manage.py migrate
```
### Now your Django project is ready to start:
```sh
cd yatube_api
python manage.py runserver
```
**Documentation available at url: http://127.0.0.1:8000/redoc/**
