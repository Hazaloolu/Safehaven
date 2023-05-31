from django.db import models

from Agents.models import Agent
from datetime import datetime
from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator

# Create your models here.


class Amenity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Accomodation(models.Model):
    # define choices for the state dropdown

    STATE_CHOICES = [
        ('', 'what state is the hostel in?'),
        ('Abia ', 'Abia'),
        ('Adamawa ', 'Adamawa'),
        ('Akwa Ibom ', 'Akwa Ibom'),
        ('Anambra ', 'Anambra'),
        ('Bauchi ', 'Bauchi'),
        ('Bayelsa ', 'Bayelsa'),
        ('Benue ', 'Benue'),
        ('Borno ', 'Borno'),
        ('Cross River ', 'Cross River'),
        ('Delta ', 'Delta'),
        ('Eboniyi ', 'Eboniyi'),
        ('Edo ', 'Edo'),
        ('Ekiti ', 'Ekiti'),
        ('Enugu ', 'Enugu'),
        ('Gombe ', 'Gombe'),
        ('Imo ', 'Imo'),
        ('Jigawa ', 'Jigawa'),
        ('Kaduna ', 'Kaduna'),
        ('Kano ', 'Kano'),
        ('Katsina ', 'Katsina'),
        ('Kebbi ', 'Kebbi'),
        ('Kogi ', 'Kogi'),
        ('Kwara ', 'Kwara'),
        ('Lagos ', 'Lagos'),
        ('Nassarawa ', 'Nassarawa'),
        ('Niger ', 'Niger'),
        ('Ogun ', 'Ogun'),
        ('Ondo ', 'Ondo'),
        ('Osun ', 'Osun'),
        ('Oyo ', 'Oyo'),
        ('Plateau ', 'Plateau'),
        ('Rivers ', 'Rivers'),
        ('sokoto ', 'Sokoto'),
        ('Taraba ', 'Taraba'),
        ('Yobe ', 'Yobe'),
        ('Zamfara ', 'Zamfara'),
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
    amenities = models.ManyToManyField(Amenity)

    def __str__(self):
        if self.Agent:
            return self.Agent.name.username
        else:
            return f'Accomodation {self.pk}'

