from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AccomodationForm
from accounts.models import NewUser
from Agents.models import Agent
from Accomodation.models import Accomodation

# Create your views here.


@login_required(login_url="login")
def Add_listing(request):
    if request.method == 'POST':
        form = AccomodationForm(request.POST, request.FILES)
        if form.is_valid():
            # get the agent associated with the logged-in user
            new_user = NewUser.objects.get(username=request.user)
            agent = Agent.objects.get(name=new_user)
            agent.accomodation_counter += 1
            agent.save()
            

            # create a new Accomodation instance and set the Agent field
            accomodation = form.save(commit=False)
            accomodation.Agent = agent
            accomodation.id = agent.accomodation_counter
            

            # save the Accomodation instance to the database
            accomodation.save()
            return redirect('inbox')
    else:
        form = AccomodationForm()
    return render(request, 'listing/add_listing.html', {'form': form})



def delete_listing(request,listing_id):
    listing=Accomodation.objects.get(id=listing_id)
    
    # delete the listing
    
    listing.delete()
    return redirect('inbox')
    
  
# views to view each listings based on the listing_id
def listed(request, listing_id):
    listing = get_object_or_404(Accomodation, pk=listing_id)
    
    
    context = {'listing':listing}
    
    return render(request,'listing/listed.html',context)
    