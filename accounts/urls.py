from django.urls import path
from . import views





urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.logout_view,name='logout_view'),
path('csrf-failure/', views.csrf_failure_view, name='csrf_failure')
 
  
   
    
]


