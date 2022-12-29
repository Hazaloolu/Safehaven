from django.shortcuts import render
from .models import Agent
from accounts.models import NewUser

# Create your views here.


# def BecomeAgent(request):
#     agents = Agent.objects.all() 
#     context={'agents':agents}  
#     return render(request,'agents/agents.html',context)


def BecomeAgent(request):
    return render(request, 'agents/AgentPage.html')


