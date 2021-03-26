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

def home(request):
    return render(request,'index.html')

def signup(response):
    if response.method == "POST":
        form = registerForm(response.POST)
        if form.is_valid():
            form.save()
        return render(response,"index.html")
    else:
        form = registerForm()
    return render(response, "signup.html", {"form":form})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f'welcome {username}')
            return redirect('profile')
        else:
            messages.info(request,f'account does not exit')
    form = AuthenticationForm()
    return render(request,'registration/login.html',{'form':form, 'title':'login'})

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


