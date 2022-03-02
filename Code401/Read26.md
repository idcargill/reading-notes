# Django

[Intro](https://www.djangoproject.com/start/)

- Define data models
- URLs and Views  
- Django uses a template language for HTML
- Builtin Forms library
- Built in security authentication
- Automatic admin interface
- Builtin language translation
- Builtin security

## Django Server Setup

[installation](https://docs.djangoproject.com/en/4.0/topics/install/#installing-official-release)

```sh
## Setup Virtual ENV with Django
poetry new <project>
cd <project>
poetry shell
poetry add Django

## Start a new project with Django-admin
django-admin startproject <webProject>
cd my <webProject>

## dev server
python manage.py runserver

## Create an APP in the project from same level as manage.py
python manage.py startapp <appName>
```


> myapp/views.py

```python
## base response
from django.http import HttpResponse

def index(request):
  return HttpResponse('Hello')

```

> myapp/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index')
]
```

> webProject/urls.py

```python
# add new app root
path('<myapp>/', include('<myapp>.urls')),

## add path to <webProject/settings.py>
INSTALLED_APPS = [
  '...',
  '<myapp>.apps.<Config>',
]
```

```sh
## Setup db models
python manage.py makemigrations polls

## Create SQLight tables
python manage.py sqlmigrate polls 0001
```

- migrate command synchronizes the models with DB


### How it works

[how django works](https://wsvincent.com/how-django-works-behind-the-scenes/)

- An open source python web framework.

#### Django Software Foundation

Code is managed by a non-profit who manages security and maintenance issues.\
 Volunteers are able to contribute to the open code.

### API

```sh
## activate a python environment with Django settings
python manage.py shell
```

#### Admin

```sh
python manage.py createsuperuser

## access admin server at /admin
```

Register admin  app/admin.py

```python
from django.contrib import admin
from .models import Question

admin.site.register(Question)
```

### Views

- Views are functions that take in the request and return an HttpResponse or an error.
