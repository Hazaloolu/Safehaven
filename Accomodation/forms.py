from django import forms
from .models import Accomodation

class AccomodationForm(forms.ModelForm):
    class Meta:
        model = Accomodation
        fields = ['state','school','price','Hostel_name','LGA','image_1','image_2','image_3','image_4','description']
        
        Widget={
            'state':forms.Select(attrs={'class':'form_control'}),
            'school':forms.TextInput(attrs={'class':'form_control'}),
             'price':forms.NumberInput(attrs={'class':'form_control','id':'price'}),
             'Hostel_name':forms.TextInput(attrs={'class':'form_control'}),
             'Address':forms.TextInput(attrs={'class':'form_control'}),
             'LGA':forms.TextInput(attrs={'class':'form_control'}),
             'image_1':forms.FileInput(attrs={'class':'forms_control','id':'preferred_image'}),
             'image_2':forms.FileInput(attrs={'class':'forms_control','class':'side_image'}),
             'image_3':forms.FileInput(attrs={'class':'forms_control','class':'side_image','required': False}),
             'image_4':forms.FileInput(attrs={'class':'forms_control','class':'side_image','required': False}),
              'Description':forms.TextInput(attrs={'class':'form_control'}),
        }
        
    

