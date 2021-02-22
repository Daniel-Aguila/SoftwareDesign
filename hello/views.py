from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

def home(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile-management.html')
    
@csrf_protect
def form(request):
    return render(request,'form.html',{'form':form})