# Django Custom User

[Django Best Practices: Models](https://learndjango.com/tutorials/django-custom-user-model)

Create a custom user for new projects.

- update project/settings.py
- create a new CustomUser model 
- create new user form CustomUser model
- update admin

'''python

# project/settings.py

AUTH_USER_MODEL = 'accounts.CustomUser' # new

# app/models.py

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username

# app/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)

'''
update models

'''sh
$ python manage.py makemigrations accounts
$ python manage.py migrate
'''

### Base User

> django.coontrib.auth.models import AbstractBaseUser, BaseUserManager

class keyword
> USERNAME_FIELD
> REQUIRED_FIELDS = []

'''python

class MyManager(BaseUserManager):
  def create_user(self, email, password=None):
    if not email:
      raise ValueError

    user = self.model(
      ...
    )

    user.set_password(password)
    user.save(user=self._db)
    return user

  def create_superuser(self, email....):
    user = self.create_user(...)
    user.is_admin = True
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)
    return user
  
'''

project/settings.py
> AUTH_USER_MODEL = 'app.AppModel'


[djangoX](https://github.com/wsvincent/djangox)

[Creating Custom Users](https://www.youtube.com/watch?v=eCeRC7E8Z7Y&t=59s)

[Abstract Users](https://www.youtube.com/watch?v=EudKs1HPUfE)

[Substitute Custom User](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#auth-custom-user)

