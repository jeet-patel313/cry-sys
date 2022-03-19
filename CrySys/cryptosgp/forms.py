from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class PositiondataForm(ModelForm):
    class Meta:
        model = Positiondata
        fields = '__all__' #tells django to make form with all fields

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']