from django.shortcuts import render

# Create your views here.


def BecomeAgent(request):
    return render(request,'agents/AgentPage.html')