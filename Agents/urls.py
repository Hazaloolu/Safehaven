from django.urls import path
from . import views

urlpatterns = [
    
    path('Become-an-agent/',views.BecomeAgent,name='BecomeAgent'),
    path('Agent_Details/',views.collectAgentDetails,name='Agent_details'),
    
]
