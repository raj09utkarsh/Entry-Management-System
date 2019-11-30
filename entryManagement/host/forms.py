# this file contains all forms used for host app

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Host

# Host register form from user model
# It contains first name, last name, email and password
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


# Host register from model form
# It contains phone number field
class HostRegisterForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ['phone_Number']
