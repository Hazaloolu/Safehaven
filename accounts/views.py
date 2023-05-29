from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from accounts.models import NewUser
from django.views.decorators.csrf import requires_csrf_token
from django.contrib import messages
# from django.utils.encoding import force_str
# from django.utils.http import urlsafe_base64_decode
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.core.mail import send_mail
# from .forms import RegistrationForm
# from .token_generator import account_activation_token







# View to register users

def register(request):
    context = {}

    # Create an empty form
    form = RegistrationForm()

    # Check if the request method is POST
    if request.method == 'POST':
        # If the request method is POST, create a RegistrationForm object
        # using the data from the request
        form = RegistrationForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # If the form is valid, save the form data to the database
            new_user = form.save()
   
            # Get the email and password entered by the user
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Authenticate the user using the email and password
            user = authenticate(request, email=email, password=password)
            
           
            

            # messages.success(request, 'We have sent you an email, please confirm your email address to complete registration.')

            login(request, user)
            return redirect("/")
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






@requires_csrf_token
def csrf_failure_view(request, reason=''):
    return render(request, 'accounts/activation_email.html', {'reason': reason})



def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)

        if not NewUser.is_email_verified:
            messages.add_message(
                request, message.Error, 'Email is not verified, please check your email inbox')
            return render(request, "accounts/login.html", {"error": "Email has not been verified"})

        if user is not None:
            # Get the "next" parameter from the query string
            next = request.GET.get('next')
            login(request, user)
            return redirect(next or "/")
        else:
            return render(request, "accounts/login.html", {"error": "Invalid email or password"})
    else:
        return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("home")


