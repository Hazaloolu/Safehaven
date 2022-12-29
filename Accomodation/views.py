from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AccomodationForm
from Accomodation.models import Accomodation

# Create your views here.


@login_required(login_url="login")
def Add_listing(request):
    if request.method == 'POST':
        form = AccomodationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inbox')
    else:
        form = AccomodationForm()
    return render(request, 'listing/add_listing.html', {'form': form})

  
# views to view each listings based on the listing_id
def listed(request, listing_id):
    listing = get_object_or_404(Accomodation, pk=listing_id)
    
    
    context = {'listing':listing}
    
    return render(request,'listing/listed.html',context)
    