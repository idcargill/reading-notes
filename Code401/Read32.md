# DRF Permissions

[drf - api guide](https://www.django-rest-framework.org/api-guide/permissions/)

[Classy Django REST Framework](https://www.cdrf.co/)

## Permissions Classs

```python
from rest_framework import permissions

```

set default permissions

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

```

Authenticate per view

```python
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)

```

@api_view decorator

```python
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'status': 'request was permitted'
    }
    return Response(content)

```

## Permission Classes

- AllowAny
- IsAuthenticated
- IsAdminUser
- IsAuthenticatedOrReadOnly

Django Permissions

> DjangoModelPermissions .perms_map

- POST requires add permission
- PUT/PATCH require change permissions
- DELETE requires delete permission

[DRF -views api](https://www.django-rest-framework.org/api-guide/generic-views/)
