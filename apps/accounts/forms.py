from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from apps.accounts.models import NewUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = NewUser
        fields = ('email','username' ,'phone_Number','password1', 'password2', )

    def clean_email(self):
        
        # get the email entered by the user
        email = self.cleaned_data['email']
        
        # check if a user with the same email already exists
        email_exists = NewUser.objects.filter(email='email').exists()
        
        # If a user with the same email already exists
        # Return validation error
        if email_exists:
            raise forms.ValidationError('User with the same email address "%s" already exists..'%email)
            
        
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
            raise forms.ValidationError(' A User with the username "%s" aleady exists..'%username)
        
        # if the username is valid
        # return the email
        
        else:
            return username
            # Access the META attribute of the NewUser class
            print(NewUser.META)
            
                


# # Define a LoginForm class that extends the forms.Form class
# class LoginForm(forms.Form):
#     # Define the 'email' field
#     email = forms.EmailField(
#         # Set the maximum length of the field to 255 characters
#         max_length=255,
#         # Set the field to be required
#         required=True,
#         # Use the EmailInput widget to render the field
#         widget=forms.EmailInput(attrs={'class': 'form-control'})
#     )
#     # Define the 'password' field
#     password = forms.CharField(
#         # Set the maximum length of the field to 255 characters
#         max_length=255,
#         # Set the field to be required
#         required=True,
#         # Use the PasswordInput widget to render the field
#         widget=forms.PasswordInput(attrs={'class': 'form-control'})
#     )