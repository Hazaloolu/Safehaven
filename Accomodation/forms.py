from django import forms
from .models import Accomodation
from django.core.validators import FileExtensionValidator

class AccomodationForm(forms.ModelForm):
    class Meta:
        model = Accomodation
        fields = ['state','school','Address','price','Hostel_name','LGA','image_1','image_2','image_3','image_4','description']
        
        field_kwargs = {
            'image_1': {'validators': [FileExtensionValidator(allowed_extensions=['png','jpeg','jpg'])]},
            'image_2': {'validators': [FileExtensionValidator(allowed_extensions=['png','jpeg','jpg'])]},
            'image_3': {'validators': [FileExtensionValidator(allowed_extensions=['png','jpeg','jpg'])]},
            'image_4': {'validators': [FileExtensionValidator(allowed_extensions=['png','jpeg','jpg'])]},
        }
        
        widgets = {
            'state': forms.Select(attrs={'class':'form_control','placeholder':'What state is the hostel located?'}),
            'school': forms.TextInput(attrs={'class':'form_control','placeholder':'What university is closest to the hostel?:'}),
            'price': forms.NumberInput(attrs={'class':'form_control','id':'price'} ),
            'Hostel_name': forms.TextInput(attrs={'class':'form_control','placeholder':'What id the name of the hostel?'}),
            'Address': forms.TextInput(attrs={'class':'form_control','placeholder':'What is the address of the hostel?'}),
            'LGA': forms.TextInput(attrs={'class':'form_control', 'placeholder':'Enter LGA:'}),
            'image_1': forms.FileInput(attrs={'class':'forms_control','id':'preferred_image'}),
            'image_2': forms.FileInput(attrs={'class':'forms_control','class':'side_image'}),
            'image_3': forms.FileInput(attrs={'class':'forms_control','class':'side_image','required': False}),
            'image_4': forms.FileInput(attrs={'class':'forms_control','class':'side_image','required': False}),
            'Description': forms.TextInput(attrs={'class':'form_control'}),
        }


def check_price(self):
    price = self.cleaned_data['price']
    if price > 1000000:
        raise form.ValidatorError('Hostel price cannot be greater than One Million')
    else:
        return price
    
    