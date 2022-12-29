from django.urls import path
from . import views

urlpatterns=[
    path('Add_listing/', views.Add_listing, name='Add_listing'),
    path('<int:listing_id>', views.listed, name='listed'),
]