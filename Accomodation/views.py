from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import AccomodationForm

# Create your views here.


@login_required(login_url="login" , redirect_field_name='next')
def Add_listing(request):
    if request.method == 'POST':
        form = AccomodationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inbox')
    else:
        form = AccomodationForm()
    return render(request, 'listing/add_listing.html', {'form': form})

  