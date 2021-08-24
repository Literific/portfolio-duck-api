# notes for useful commands and tips

## HTTP Status Response Codes

- 2xx Success
- 3xx Redirections
- 4xx Client Error
    - 404 Not Found
- 5xx Server Error
    - 500 Internal Server Error

## Restful APIs

    - a base URI https://ex.com/api
    - HTTP methods (GET, POST, PUT, PATCH and DELETE)
    - is stateless, like HTTP
        - stateless: every cycle (HTTP request, Retrieve Data) is completely independent of what happened in the cycle before (no memory). e.g. authentication, every time we need to authenticate ourselves (send authentication signature with request).
    - includes media type to define state transition data elements (JSON)
    - RESTful APIs have endpoints
        -  webpages normally contains links to resources (http://site.com/blog)
        - http://site.com/api/user/1 -> get user with id=1
        - http://site.com/api/books
        - Rembmer: Data is returned as JSON etc
    - Service respond based upon request type:
        - https://site.com/api/user/1 
        - GET -> retrieve user 1 data
        - DELETE -> delete user 1
    - xx

## Project Details

- Build Login facility in React JS, we are going to store the session (or state) in the react application.
- if not, everytime we make a request, we have to login again and again.

## Useful commands

```
# create virtual environment 
python -m venv venv 

# activate venv
source venv/bin/activate

# install django 
pip install django

# create project 
django-admin startproject core .

python manage.py startapp stock
python manage.py startapp stock_api # just manage the api for the stock

# add urlpatterns in core > urls.py, stock > urls.py, stock_api > urls.py
# add apps in the INSTALLED_APPS in settings.py
# create templates > stock > index.html
# add template directory in settings.py


# instructor useful commands
python manage.py makemigrations --dry-run --verbosity 3
python manage.py runserver
python manage.py createsuperuser
pip install coverage
coverage run --omit='*/venv/*' manage.py test 
coverage html
pip install djangorestframework
```
