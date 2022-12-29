from django.contrib import admin
from .models import Accomodation
# Register your models here.



class AccomodationAdmin(admin.ModelAdmin):
    list_display = ('id','Hostel_name','Address','state','school','price','LGA')
    list_display_links = ('id', 'Hostel_name')
    list_search_field = ('Hostel_name','school','state','LGA','Address')
    list_per_page = 25

admin.site.register(Accomodation,AccomodationAdmin)