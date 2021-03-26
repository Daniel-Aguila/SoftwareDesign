from django import forms
from localflavor.us.forms import USStateSelect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","password1"]


