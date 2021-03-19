from django import forms
from localflavor.us.forms import USStateSelect

class profileManage(forms.Form):
    fullName=forms.CharField(label='full-name',max_length=50,required=True)
    address1=forms.CharField(label='add1',max_length=100,required=True)
    address2=forms.CharField(label='add2',max_length=100,required=False)
    city=forms.CharField(label='city',max_length=100,required=True)
    states = forms.CharField(widget=USStateSelect, required=True)

