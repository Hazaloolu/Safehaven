from django import forms
from .models import Agent

class AgentsForm(forms.ModelForm):
    class  Meta:
        model = Agent
        fields = ['phone_number','state','profile_image']
        
        
        Widget = {
            'phone_number': forms.TextInput(),
            'state': forms.TextInput(),
            'profile_image': forms.FileInput(),
        }