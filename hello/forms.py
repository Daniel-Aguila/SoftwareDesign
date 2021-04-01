from django import forms
from localflavor.us.forms import USStateSelect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .import models


class DateInput(forms.DateInput):
    input_type = 'date'

# MODEL FORMS:

class profileManage(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['fullName','address1','address2','city','state','zipcode']

class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","password1"]

class FuelQuoteForm(forms.ModelForm):
    class Meta:
        model = models.Quote
        widgets = {'deliveryDate': DateInput()}
        fields = ['gallonsReq', 'deliveryDate'] 
