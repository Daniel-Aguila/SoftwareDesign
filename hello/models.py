from django.db import models
from django.db import connections
from django.contrib.auth.models import User

# Create your models here.

STATE_CHOICES = [
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware '),
    ('FL', 'Florida '),
    ('GA', 'Georgia '),
    ('HI', 'Hawaii '),
    ('ID', 'Idaho '),
    ('IL', 'Illinois '),
    ('IN', 'Indiana '),
    ('IA', 'Iowa '),
    ('KS', 'Kansas '),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine '),
    ('MD', 'Maryland '),
    ('MA', 'Massachusetts '),
    ('MI', 'Michigan '),
    ('MN', 'Minnesota '),
    ('MS', 'Mississippi '),
    ('MO', 'Missouri '),
    ('MT', 'Montana '),
    ('NE', 'Nebraska '),
    ('NV', 'Nevada '),
    ('NH', 'New Hampshire '),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio '),
    ('OK', 'Oklahoma '),
    ('OR', 'Oregon '),
    ('PA', 'Pennsylvania '),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee '),
    ('TX', 'Texas '),
    ('UT', 'Utah '),
    ('VT', 'Vermont '),
    ('VA', 'Virginia '),
    ('WA', 'Washington '),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin '),
    ('WY', 'Wyoming'),
]

class Register(models.Model):
    username = models.CharField(max_length=20, unique=True, primary_key=True)
    password = models.CharField(max_length=20)


class Profile(models.Model):
    fullName = models.CharField(max_length=50, default='John Doe')
    address1 = models.CharField(max_length=100, default='1234 Maple St')
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, default='Houston')
    state = models.CharField(max_length=2, choices=STATE_CHOICES, default='TX')
    zipcode = models.PositiveIntegerField(default=77592)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'


class Quote(models.Model):
    gallonsReq = models.PositiveIntegerField()
    fullAddress = models.CharField(max_length=100)
    deliveryDate = models.DateField()
    pricePerGallon = models.DecimalField(decimal_places=2, max_digits=5)
    totalDue = models.DecimalField(decimal_places=2, max_digits=20)

    def __str__(self):
        return self.fullAddress

class pricing():

    def __init__(self, gallonsN, location, rate_history=False):
        self.gallonsTotal = gallonsN
        self.location = location
        self.rate_history = rate_history

    def suggestedPrice(self):
        return 1.500 + self.margin()
        

    def margin(self):
        if self.location == "TX":
            location_factor = 0.020
        else:
            location_factor = 0.040
        
        if self.rate_history == True:
            rate_history_factor = 0.010
        else:
            rate_history_factor = 0.000
        if self.gallonsTotal >= 1000:
            gallons_requested_factor = 0.020
        else: 
            gallons_requested_factor = 0.030
        
        return 1.50 * (location_factor - rate_history_factor + gallons_requested_factor + 0.100)
    def totalAmountDue(self):
        return self.gallonsTotal * self.suggestedPrice()


    