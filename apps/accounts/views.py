from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from apps.accounts.models import NewUser
from django.contrib.auth.forms import AuthenticationForm


# Registration views

def register(request):
    context = {}
    
    # Create an empty form
    form = RegistrationForm()

    # Check if the request method is POST, which indicates that the user
    # has submitted the form
    if request.method == 'POST':
        # If the request method is POST, create a RegistrationForm object
        # using the data from the request
        form = RegistrationForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # If the form is valid, save the form data to the database
            form.save()

            # Get the email and password entered by the user
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Authenticate the user using the email and password
            user = authenticate(request, email=email, password=password)

            # Redirect the user to the login page
            return redirect('login')
        else:
            # Update the context dictionary with the form object
            context['registration_form'] = form

            # Return a response with the updated context
            return render(request, 'accounts/register.html', context)


    else:
        # Create a context dictionary that contains the form object
        context['registration_form'] = form

        # Render the registration template, passing the context dictionary
        return render(request, 'accounts/register.html', context)

    
    

def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "accounts/login.html", {"error": "Invalid email or password"})
    else:
        return render(request, "accounts/login.html")
    
    

def logout_view(request):
    logout(request)
    return redirect("home")