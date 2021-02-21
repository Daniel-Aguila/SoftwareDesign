from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def form(request):
    return render(request,'form.html',{'form':form})