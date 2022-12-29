from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from Accomodation.models import Accomodation


def home(request):
    return render(request,'main/index.html')

def success(request):
    return render(request,'main/success.html')

def inbox(request):
    
    accomodations = Accomodation.objects.all().order_by("-date_time_uploaded")
    context = {'accomodations':accomodations}
    return render(request, 'main/inbox.html',context)