from django import forms
from localflavor.us.forms import USStateSelect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class profileManage(forms.Form):
    fullName=forms.CharField(max_length=50)
    address1=forms.CharField(max_length=100)
    address2=forms.CharField(max_length=100,required=False)
    city=forms.CharField(max_length=100)
    states = forms.CharField(widget=USStateSelect)

class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","password1"]

