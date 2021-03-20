from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    return render(request,'index.html')

def signup(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'profile-management.html')
    context['form']=form
    return render(request,'signup.html',context)


@csrf_protect
def form(request):
    return render(request,'form.html',{'form':form})

@login_required
def profile(request):
    return render(request, 'profile-management.html')
