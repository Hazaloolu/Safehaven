from django import forms
from .models import Agent
import re
from django.core.exceptions import ValidationError


class AgentsForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['phone_number', 'state', 'profile_image']

        widget = {
            'phone_number': forms.TextInput(),
            'state': forms.Select(attrs={'empty_value': 'Select your state'}),

            'profile_image': forms.FileInput(),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        if phone_number:
            # remove all non -numeric character

            phone_number = re.sub('\D', '', phone_number)

            # check if phone number starts with 234
            if not phone_number.startswith('234'):
                raise ValidationError('Phone number must start with 234')

            # check if phone number length = 13

            if len(phone_number) != 13:
                raise ValidationError('phone number must be 13 digits long')

            return phone_number
