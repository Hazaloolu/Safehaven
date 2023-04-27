from django.shortcuts import render,redirect
from .models import Agent
from .forms import AgentsForm
from accounts.models import NewUser
from django.contrib.auth.decorators import login_required

# Create your views here.
# Collect the details of new agent and Regsister them
@login_required(login_url='login')
def collectAgentDetails(request):
    # try to get the Agent instance associated with the current user
    try:
        new_user = NewUser.objects.get(username=request.user)
        agent = Agent.objects.get(name=new_user)

        
        # if agent does no exist, create a new one
    except Agent.DoesNotExist:
        new_user = NewUser.objects.get(username=request.user)
        agent = Agent(name=new_user, name_id=request.user.id)
        
        # set the form_filled field to false for the newly created agent
        agent.form_filled = False
        
        # save to database
        agent.save()
        return redirect('Agent_details')
        
        
    # if agent.form_filled = True
    if agent.form_filled:
        # redirect the user to create a listing(redirect to the Add_lising url)
        return redirect('Add_listing')
    
    # create a new form instance
    form = AgentsForm()
    context = {'form': form}
    
    # check the request method
    if request.method == 'POST':
        form = AgentsForm(request.POST,request.FILES)
        # check if the form is valid
        if form.is_valid():
            # if form is valid, update the field of the Agent instance with the cleaned data
            
            agent.phone_number = form.cleaned_data['phone_number']
            agent.state = form.cleaned_data['state']
            agent.profile_image = form.cleaned_data['profile_image']
            # Set the form_filled field to True
            agent.form_filled = True
            
            # save the agent instance to the database
            agent.save()
            
            # redirect the user to create a listing(redirect to the Add_lising url)
            return redirect('Add_listing')
        
        # if the form is not valid,
        else:
            # update the context variable with the form instance
            context = {'form': form}
    
    # render the template with the context
    return render(request, 'agents/agents.html', context)


        

           
            

            
        
        




def BecomeAgent(request):
   
    return render(request, 'agents/AgentPage.html')


