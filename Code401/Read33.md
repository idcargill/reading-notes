# JWT

[JWT](https://jwt.io/introduction/)

Used for Authorization and information exchange.

header.payload.signature

- Header

```json

{
  "alg" : "HS256",
  "typ" : "JWT",
}
```

- Payload : contains claims
  - registered: recommended useful information
  - public: can be defined at will
  - private: created to share information between parties.

``` json
{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true
}

```

- Signature: verifies that the message has not been tampered with.

The server will check for a valid JWT in the Authorization Header.

### Django REST JWT

[Django Rest JWT](https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html)

```sh
install /add djangorestframework_simplejwt
```

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```

```python
# urls.py
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # Your URLs...
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
```

```python
# /app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
```

```python
# urls.py
from django.urls import path
from myapi.core import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
]
```

### Get a token

> http post http://127.0.0.1:8000/api/token/ username=vitor password=123

in the body response, store the access token and refresh token in local storage.

include the access token in the header for all other requests.

### Refresh a Token

> http post http://127.0.0.1:8000/api/token/refresh/ refresh=refreshkey

### Django Runserver not for production

[django runserver](https://vsupalov.com/django-runserver-in-production/)

- Web Server: Nginx
- Application server: Gunicorn  (WSGI specification)

[Pretty Printed](https://www.youtube.com/watch?v=Fhcn2qx-4VQ)

[Gunicorn](https://gunicorn.org/)

[django migrations](https://realpython.com/django-migrations-a-primer/)
