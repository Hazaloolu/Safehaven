from django.db import models
from datetime import datetime
# Create your models here.

class Accomodation(models.Model):
    # define choices for the state dropdown
    
    STATE_CHOICES = [
    ('Abia_state','Abia'),
    ('Adamawa_state','Adamawa'),
    ('Akwa_Ibom_state','Akwa Ibom'),
    ('Anambra_state','Anambra'),
    ('Bauchi_state','Bauchi'),
    ('Bayelsa_state','Bayelsa'),
    ('Benue_state','Benue'),
    ('Borno_state','Borno'),
    ('Cross_River_state','Cross River'),
    ('Delta_state','Delta'),
    ('Eboniyi_state','Eboniyi'),
    ('Edo_state','Edo'),
    ('Ekiti_state','Ekiti'),
    ('Enugu_state','Enugu'),
    ('Gombe_state','Gombe'),
    ('Imo_state','Imo'),
    ('Jigawa_state','Jigawa'),
    ('Kaduna_state','Kaduna'),
    ('Kano_state','Kano'),
    ('Katsina_state','Katsina'),
    ('Kebbi_state','Kebbi'),
    ('Kogi_state','Kogi'),
    ('Kwara_state','Kwara'),
    ('Lagos_state','Lagos'),
    ('Nassarawa_state','Nassarawa'),
    ('Niger_state','Niger'),
    ('Ogun_state','Ogun'),
    ('Ondo_state','Ondo'),
    ('Osun_state','Osun'),
    ('Oyo_state','Oyo'),
    ('Plateau_state','Plateau'),
    ('Rivers_state','Rivers'),
    ('Sokoto_state','Sokoto'),
    ('Taraba_state','Taraba'),
    ('Yobe_state','Yobe'),
    ('Zamfara_state','Zamfara'),
    ('Federal_Capital_Territory','Federal Capital Territory')
]

 
    state=models.CharField(max_length=30, choices=STATE_CHOICES)
    school = models.CharField(max_length=70)
    price=models.DecimalField( max_digits=8, decimal_places=2)
    Hostel_name=models.CharField(max_length=70)
    Address=models.CharField(max_length=70)
    LGA = models.CharField(max_length=70)
    image_1 = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/')
    image_3 = models.ImageField(upload_to='images/')
    image_4 = models.ImageField(upload_to='images/')
    description = models.TextField()
    date_time_uploaded = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.Hostel_name + ' / ' + self.school 
    