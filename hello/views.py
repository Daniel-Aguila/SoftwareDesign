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
from .models import Register, Quote
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

@login_required
@csrf_protect
def form(request):
    if request.method == 'POST':
        form = forms.FuelQuoteForm(request.POST)
        if form.is_valid():
            newQuote = form.save(commit=False)
            currUser = request.user.profile
            fullAddress = f'{currUser.address1}, {currUser.city}, {currUser.state} {currUser.zipcode}'
            newQuote.fullAddress = fullAddress
            newQuote.pricePerGallon = 1.50 # Hardcoded for now, implement pricing module
            newQuote.totalDue = newQuote.pricePerGallon * newQuote.gallonsReq
            newQuote.save()
            return redirect('quote')
    else:
        form = forms.FuelQuoteForm()
    return render(request,'form.html',{'form':form})

@login_required
@csrf_protect
def profile(request):
    if request.method == 'POST':
        # form = forms.profileManage(request.POST, instance=request.user.profile)
        form = forms.profileManage(request.POST)
        if form.is_valid():
            newProfile = form.save(commit=False)
            newProfile.user = request.user
            newProfile.save()
            return redirect('form')
    else:
        form = forms.profileManage()
    return render(request, 'profile-management.html',{'form':form})


def history(request):
    context = {
        'posts': Quote.objects.all()
    }
    return render(request, 'fuelQuoteHistory.html', context)

def quote(request):
    return render(request,"quote.html")
