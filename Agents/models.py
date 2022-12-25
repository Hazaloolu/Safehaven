from django.db import models
from accounts.models import NewUser
# Create your models here.


class Agent(models.Model):
    Agent_name = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    Agent_phone_number = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='+')
    is_verified = models.BooleanField()
    image = models.ImageField(upload_to='images/')
    
    
  
 
    
    def __str__(self):
        return self.Agent_name.username




