from django.contrib import admin
from .models import Agent

# Register your models here.

class AgentAdmin(admin.ModelAdmin):
    list_display = ('form_filled','name','state','phone_number','accomodation_counter')
    list_display_links = ('name','state')
    list_search_field = ('name','state','phone_number')
    list_per_page = 25

admin.site.register(Agent,AgentAdmin)
