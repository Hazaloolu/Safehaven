from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import NewUser

class AccountAdmin(UserAdmin):
    list_display = ('email','username','is_Agent','date_joined','is_staff','is_admin')
    search_fields = ('email','username')
    filter_list  = ()
    readonly_fields = ('id', 'date_joined')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Register your models here.
admin.site.register(NewUser, AccountAdmin)