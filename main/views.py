from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from Accomodation.models import Accomodation
from Agents.models import Agent
from accounts.models import NewUser
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def home(request):
    accomodations = Accomodation.objects.all().order_by("-date_time_uploaded")[:6]
    
    context = {'accomodations':accomodations}

    return render(request, 'main/index.html',context)


def success(request):
    return render(request, 'main/success.html')


def inbox(request):
    # Redirect the user to the login URL if they are not authenticated
    if not request.user.is_authenticated:
        return redirect('login')

    # get the agent associated with the logged_in user
    new_user = NewUser.objects.get(username=request.user)
    agent = Agent.objects.get(name=new_user)

    # Filter the accomodation queryset by the agent
    accomodations = Accomodation.objects.filter(
        Agent=agent).order_by("-date_time_uploaded")
    total_listing = len(Accomodation.objects.filter(Agent=agent).all())
    
    paginator = Paginator(accomodations,per_page=5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
   
    
    context = {'accomodations': accomodations, 'total_listing': total_listing, 'page_obj': page_obj}

    return render(request, 'main/inbox.html', context)

    # print(len(accomodations))  # Debugging line

   
