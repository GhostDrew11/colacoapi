# colacoapi

Prototype django REST API for the colaco vending machine web application

# Libraries used
This API was bootstrapped with django, django restframework, postgreSQL, psycopg2, pillow, django-cors-headers

In the project directory, you can run:

### `mkvirtualenv nameofyourvirtualenv` inside the command prompt

To initialize a virtual environment to protect your local environment and avoid messing up your local environment

### `pip isntall django`

To install django on your virtual environment

### `pip install djangorestframework`

To install the rest framework

### `pip install psycopg2` and `pip install pillow`

To work with a postgreSQL database instead of an SQLite database

### `pip install django-cors-headers`

To allow your the communication of your locally running react frontend with your locally running REST API

### `python manage.py runserver`

To locally run your  REST API

# Routes

`http://127.0.0.1:8000/api/v1/` for the root api
`http://127.0.0.1:8000/api/v1/users/` for crud opertions on users
`http://127.0.0.1:8000/api/v1/sodas/` for crud opertions on sodas
`http://127.0.0.1:8000/api/v1/orders/` for crud opertions on orders



 
