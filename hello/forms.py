from django import forms
from localflavor.us.forms import USStateSelect

class profileManage(forms.Form):
    fullName=forms.CharField(max_length=50)
    address1=forms.CharField(max_length=100)
    address2=forms.CharField(max_length=100,required=False)
    city=forms.CharField(max_length=100)
    states = forms.CharField(widget=USStateSelect)

