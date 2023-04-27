from django.db import models

from Agents.models import Agent
from datetime import datetime
from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator

# Create your models here.


class Accomodation(models.Model):
    # define choices for the state dropdown

    STATE_CHOICES = [
        ('', 'what state is the hostel in?'),
        ('Abia state', 'Abia'),
        ('Adamawa state', 'Adamawa'),
        ('Akwa Ibom state', 'Akwa Ibom'),
        ('Anambra state', 'Anambra'),
        ('Bauchi state', 'Bauchi'),
        ('Bayelsa state', 'Bayelsa'),
        ('Benue state', 'Benue'),
        ('Borno state', 'Borno'),
        ('Cross River state', 'Cross River'),
        ('Delta state', 'Delta'),
        ('Eboniyi state', 'Eboniyi'),
        ('Edo state', 'Edo'),
        ('Ekiti state', 'Ekiti'),
        ('Enugu state', 'Enugu'),
        ('Gombe state', 'Gombe'),
        ('Imo state', 'Imo'),
        ('Jigawa state', 'Jigawa'),
        ('Kaduna state', 'Kaduna'),
        ('Kano state', 'Kano'),
        ('Katsina state', 'Katsina'),
        ('Kebbi state', 'Kebbi'),
        ('Kogi state', 'Kogi'),
        ('Kwara state', 'Kwara'),
        ('Lagos state', 'Lagos'),
        ('Nassarawa state', 'Nassarawa'),
        ('Niger state', 'Niger'),
        ('Ogun state', 'Ogun'),
        ('Ondo state', 'Ondo'),
        ('Osun state', 'Osun'),
        ('Oyo state', 'Oyo'),
        ('Plateau state', 'Plateau'),
        ('Rivers state', 'Rivers'),
        ('Sokoto state', 'Sokoto'),
        ('Taraba state', 'Taraba'),
        ('Yobe state', 'Yobe'),
        ('Zamfara state', 'Zamfara'),
        ('Federal Capital Territory', 'Federal Capital Territory')
    ]

    Agent = models.ForeignKey(
        Agent, on_delete=models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=30, choices=STATE_CHOICES)
    school = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Hostel_name = models.CharField(max_length=70)
    Address = models.CharField(max_length=70)
    LGA = models.CharField(max_length=70)
    image_1 = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/')
    image_3 = models.ImageField(upload_to='images/')
    image_4 = models.ImageField(upload_to='images/')
    description = models.TextField(max_length = 4000,validators=[MinLengthValidator(10)])
    date_time_uploaded = models.DateTimeField(default=datetime.now, blank=True)
    id = models.AutoField(primary_key=True)
    image_public_id = models.CharField(max_length=255)

    def __str__(self):
        if self.Agent:
            return self.Agent.name.username
        else:
            return f'Accomodation {self.pk}'
