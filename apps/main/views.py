from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout



def home(request):
    return render(request,'main/index.html')

def success(request):
    return render(request,'main/success.html')

