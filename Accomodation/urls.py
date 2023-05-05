from django.urls import path
from . import views

urlpatterns=[
    path('Add_listing/', views.Add_listing, name='Add_listing'),
    path('Listing<int:listing_id>', views.listed, name='listed'),
    path('Listing-Result<int:listing_id>', views.result_listed, name='result_listed'),
    path('accomodation/Listing//<int:listing_id>/delete/', views.delete_listing, name='delete_listing'),
    path('search/', views.search_accomodations, name='search'),
    
]