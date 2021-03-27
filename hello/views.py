from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import registerForm
from .import forms
from django.template.loader import get_template
from django.template import Context
from .models import Register
import logging

def home(request):
    return render(request,'index.html')

def signup(response):
    form = registerForm(response.POST)
    if response.method == "POST" and form.is_valid():
            user=form.cleaned_data['username']
            passd=form.cleaned_data['password1']
            newPerson = Register(username=user,password=passd)
            newPerson.save(force_insert=True)
            form.save()

            return render(response,"index.html")

    return render(response, "signup.html", {"form":form})

def loginpage(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)

        logging.debug("hello")

        if user is not None:

            login(request, user)
            return redirect('profile')


    return render(request,'login.html',{'form':form, 'title':'login'})

@csrf_protect
def form(request):
    if request.method == 'POST':
        form = forms.FuelQuoteForm(request.POST)
        if form.is_valid():
            # SAVE TO DB
            return redirect('history')
    else:
        form = forms.FuelQuoteForm()
    return render(request,'form.html',{'form':form})

@login_required
def profile(request):
    return render(request, 'profile-management.html')
def history(request):
    return render(request, 'fuelQuoteHistory.html')


