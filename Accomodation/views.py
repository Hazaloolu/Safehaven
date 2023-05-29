from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AccomodationForm
from accounts.models import NewUser
from Agents.models import Agent
from Accomodation.models import Accomodation
from .choices import state_choices,price_choices
from django.db.models import Q
import cloudinary
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.



def Add_listing(request):
    if request.user.is_authenticated:
        # user is authenticated already
        if request.method == 'POST':
            form = AccomodationForm(request.POST, request.FILES)
            if form.is_valid():
                # get the agent associated with the logged-in user
                selected_options = form.cleaned_data['amenities']
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
                # save the selected options to the database
                accomodation.amenities.set(selected_options)
                # add success message to the user'session
                messages.success(request, 'New listing added successfully !')
                
                # save the seleted options to the sessions
        
                return redirect('inbox')
            

        else:
            form = AccomodationForm()
        return render(request, 'listing/Add_listing.html', {'form': form})
    else:
        # user is not autehnticated
        # redirect to the login page with the next parameter
        login_url = reverse('login') + '?next=' + request.path
        return redirect(login_url)
        



def delete_listing(request,listing_id):
    listing=Accomodation.objects.get(id=listing_id)
    
    # delete the image from cloudinary
    # cloudinary.api.delete_resources([listing.image_public_id])
    
    # delete the listing
    
    listing.delete()
    return redirect('inbox')
    
  
# views to view each listings based on the listing_id


def listed(request, listing_id):
    listing = get_object_or_404(Accomodation, pk=listing_id)
    selected_options = listing.amenities.all()
    
    context = {'listing':listing,'selected_options':selected_options,}
    
    return render(request,'listing/listed.html',context)

# search result individual lsiting
@login_required(login_url='login')
def result_listed(request, listing_id):
    listing = get_object_or_404(Accomodation, pk=listing_id)
    
    
   
    context = {'listing':listing}
    return render(request,'listing/result_listed.html',context)




# search for accomodations

def search_accomodations(request):
    # extract search query from request
    search_query = request.GET.get('search')
    
    if search_query is None:
        search_query = ''

    # use filter method to return queryset of Accomodation objects with fields containing search query
    
    accomodations = Accomodation.objects.filter(
    Q(state__contains=search_query) |
    Q(school__contains=search_query) |
    Q(Hostel_name__contains=search_query) |
    Q(LGA__contains=search_query) |
    Q(description__contains=search_query)
)
    
     
    paginator = Paginator(accomodations,per_page=5)
    page_number = request.GET.get("page")
    page_obj = paginator .get_page(page_number)
    

    
    context = {'accomodations':accomodations,'search_query':search_query, 'page_obj':page_obj}

    
 

   
    # render search results template with queryset of Accomodation objects as context
    return render(request, 'listing/result.html', context)



