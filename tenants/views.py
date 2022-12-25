from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url=reverse_lazy("login"))
#ensure that only authenticated users can access the dashboard
def dashboard(request):
    return render(request,'tenants/dashboard.html')