from django import forms
from localflavor.us.forms import USStateSelect

class profileManage(forms.Form):
    fullName=forms.CharField(label='full-name',max_length=50)
    address1=forms.CharField(label='add1',max_length=100)
    address2=forms.CharField(label='add2',max_length=100,required=False)
    city=forms.CharField(label='city',max_length=100)
    states = forms.CharField(widget=USStateSelect)

