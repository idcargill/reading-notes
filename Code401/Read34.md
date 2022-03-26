# Django API Deployment

[Best practices by some random dude](https://djangostars.com/blog/configuring-django-settings-best-practices/)

- settings_local.py

- keep settings in individual files

## django-environ

```python
# settings.py
import environ

# .env
DEBUG=TRUE
SECRET_GARBAGE=stuffandthings

```

> os.environ


### 12 Factors recommendations for deployment

- Codebase
- Dependencies
- Config
- Backing services
- Build, release, run
- Processes
- Port Binding
- Concurrency
- Disposability
- Dev/prod parity
- Logs
- Admin Processes

- Keep settings in .env
- write default values for prod

### SSH

[SSH encryption](https://www.hostinger.com/tutorials/ssh-tutorial-how-does-ssh-work)

Secure Shell Protocol

```sh
ssh {user}@{host}
```

Host: remote server you are accessing.


### WhiteNoise

[WhiteNoise](http://whitenoise.evans.io/en/stable/)

```sh
install whitenoise
```

```python
# settings.py

MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# WSGI Apps

from whitenoise import WhiteNoise

from my_project import MyWSGIApp

application = MyWSGIApp()
application = WhiteNoise(application, root="/path/to/static/files")
application.add_files("/path/to/more/static/files", prefix="more-files/")


```

[wiki - infrastructure as service](https://en.wikipedia.org/wiki/Infrastructure_as_a_service)
there is no cloud

[wiki - platform as a service](https://en.wikipedia.org/wiki/Platform_as_a_service)

[wiki - CORS](https://en.m.wikipedia.org/wiki/Cross-origin_resource_sharing)

HTTP Header

```sh
Response header allowing requests from the originally GET are allowed
Access-Control-Allow-Origin: http://www.example.com 





Preflight Example
OPTIONS /
Host: service.example.com
Origin: http://www.example.com
Access-Control-Request-Method: PUT
```

### Request Headers

- Origin
- Access-Control-Request-Method
- Access-Control-Request-Headers

### Response Headers

- Access-Control-Allow-Origin
- Access-Control-Allow-Credentials
- Access-Control-Expose-Headers
- Access-Control-Max-Age
- Access-Control-Allow-Methods
- Access-Control-Allow-Headers
