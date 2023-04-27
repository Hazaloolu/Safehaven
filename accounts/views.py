from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from accounts.models import NewUser
from django.contrib import messages
# from django.utils.encoding import force_str
# from django.utils.http import urlsafe_base64_decode
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.core.mail import send_mail
# from .forms import RegistrationForm
# from .token_generator import account_activation_token









# def activate(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         messages.success(request, 'Your account has been activated successfully.')
#         return redirect('home')
#     else:
#         messages.error(request, 'The activation link is invalid or has expired.')
#         return redirect('login')

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
            
           
            # # send activation email to user
            # current_site = get_current_site(request)
            # subject = 'Activate your account'
            # message = render_to_string('accounts/activation_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            #     'token': account_activation_token.make_token(user),
            # })
            # send_mail(subject, message, 'noreply@yourdomain.com', [email], fail_silently=False)

            # messages.success(request, 'We have sent you an email, please confirm your email address to complete registration.')

            return redirect("login")
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

        if not NewUser.is_email_verified:
            messages.add_message(
                request, message.Error, 'Email is not verified, please check your email inbox')
            return render(request, "accounts/login.html", {"error": "Email has not been verified"})

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


# forgot password view


# activate _email

def activate_user(request, uidb64, token):
    try:

        uid = force_str(urlsafe_base64_decode(uidb64))

        user = NewUser.objects.get(pk=uid)
    except Exception as e:

        user = None
    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()
        messages.add_messages(request, messages.SUCCESS,
                              'Email verified, Your account has been created successfully')
        return redirect(reverse('login'))

    return render(request, 'accounts/activate_failed.html', {'user': user})
