from dataclasses import fields
from django.db import models
from django.forms import ImageField
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta():
        model=User
        fields = ('username','email','password1','password2')

class ProfileForm(UserCreationForm):
    class Meta():
        model=User
        fields = ('username','email','profile_pic','Bio')

