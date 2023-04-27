from django.db import models
from accounts.models import NewUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Agent(models.Model):

    # define choices for the state dropdown

    STATE_CHOICES = [
        ('', 'Select Your State'),
        ('Abia_state', 'Abia'),
        ('Adamawa_state', 'Adamawa'),
        ('Akwa_Ibom_state', 'Akwa Ibom'),
        ('Anambra_state', 'Anambra'),
        ('Bauchi_state', 'Bauchi'),
        ('Bayelsa_state', 'Bayelsa'),
        ('Benue_state', 'Benue'),
        ('Borno_state', 'Borno'),
        ('Cross_River_state', 'Cross River'),
        ('Delta_state', 'Delta'),
        ('Eboniyi_state', 'Eboniyi'),
        ('Edo_state', 'Edo'),
        ('Ekiti_state', 'Ekiti'),
        ('Enugu_state', 'Enugu'),
        ('Gombe_state', 'Gombe'),
        ('Imo_state', 'Imo'),
        ('Jigawa_state', 'Jigawa'),
        ('Kaduna_state', 'Kaduna'),
        ('Kano_state', 'Kano'),
        ('Katsina_state', 'Katsina'),
        ('Kebbi_state', 'Kebbi'),
        ('Kogi_state', 'Kogi'),
        ('Kwara_state', 'Kwara'),
        ('Lagos_state', 'Lagos'),
        ('Nassarawa_state', 'Nassarawa'),
        ('Niger_state', 'Niger'),
        ('Ogun_state', 'Ogun'),
        ('Ondo_state', 'Ondo'),
        ('Osun_state', 'Osun'),
        ('Oyo_state', 'Oyo'),
        ('Plateau_state', 'Plateau'),
        ('Rivers_state', 'Rivers'),
        ('Sokoto_state', 'Sokoto'),
        ('Taraba_state', 'Taraba'),
        ('Yobe_state', 'Yobe'),
        ('Zamfara_state', 'Zamfara'),
        ('Federal_Capital_Territory', 'Federal Capital Territory')
    ]

    name = models.OneToOneField(
        NewUser, on_delete=models.SET_NULL, related_name='agent', null=True)
    phone_number = models.CharField(max_length=13)
    profile_image = models.ImageField(
        upload_to='profile_images/', default='images/defalt.png', null=True, blank=True)
    state = models.CharField(max_length=30, choices=STATE_CHOICES)
    description = models.TextField()
    form_filled = models.BooleanField(default=False)
    accomodation_counter = models.PositiveIntegerField(default=0)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'{self.name.username} ({self.pk})'
