from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Agent(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    is_verified = models.BooleanField()
    profile_image = models.ImageField(upload_to='profile_images/', default='images/defalt.png', null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return 'Agent ' + self.name

        return 'Agent ' + self.name




