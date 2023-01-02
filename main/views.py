from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from Accomodation.models import Accomodation
from Agents.models import Agent
from accounts.models import NewUser
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'main/index.html')


def success(request):
    return render(request, 'main/success.html')


from django.shortcuts import redirect

def inbox(request):
    # Redirect the user to the login URL if they are not authenticated
    if not request.user.is_authenticated:
        return redirect('login')

    # get the agent associated with the logged_in user
    new_user = NewUser.objects.get(username=request.user)
    agent = Agent.objects.get(name=new_user)
    

    # Filter the accomodation queryset by the agent
    accomodations = Accomodation.objects.filter(
        Agent=agent).all().order_by("-date_time_uploaded")
    total_listing = len(Accomodation.objects.filter(Agent = agent).all())
    context = {'accomodations': accomodations,'total_listing':total_listing}
    
    
   
    return render(request, 'main/inbox.html', context)

    
    
    
    print(len(accomodations))  # Debugging line
   
    return render(request, 'main/inbox.html', context)
