from django.urls import path
from . import views

urlpatterns = [
    path('Become-an-agent/',views.BecomeAgent,name='BecomeAgent'),
    path('inbox/',views.Agents_dashboard,name='inbox'),
]
