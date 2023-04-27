from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from accounts.models import NewUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = NewUser
        fields = ('email','username','password1', 'password2', )

    def clean_email(self):
        
        # get the email entered by the user
        email = self.cleaned_data['email']
        
        # check if a user with the same email already exists
        email_exists = NewUser.objects.filter(email='email').exists()
        
        # If a user with the same email already exists
        # Return validation error
        if email_exists:
            raise forms.ValidationError(' A User with the email "%s" aleady exists..'%email)
           
            
        
        # if the email address is valid
        # return the email
        
        else:
            return email
        
    
    def clean_username(self):
        # get the username
        username=self.cleaned_data['username']
        
        # check if username already exists
        username_exists = NewUser.objects.filter(username=username).exists()
            # if username exists
            # raise validation error
            
        if username_exists:
            return username
        
        # if the username is valid
        # return the email
        
        else:
            return username
            # Access the META attribute of the NewUser class
            print(NewUser.META)
            
                

