from django.db import models
from django.db import connections

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
    fullName = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100, unique=True)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zipcode = models.PositiveIntegerField()
    #username = models.ForeignKey('Register', default=None, on_delete=models.CASCADE, to_field='username')

    def __str__(self):
        return self.fullName


class Quote(models.Model):
    gallonsReq = models.PositiveIntegerField()
    # fullAddress = models.ForeignKey('Profile', default=None, on_delete=models.CASCADE, to_field='address1')
    fullAddress = models.CharField(max_length=100)
    # Need to link address with user profile, is charfield rn for testing
    deliveryDate = models.DateField()
    pricePerGallon = models.DecimalField(decimal_places=2, max_digits=5)
    totalDue = models.DecimalField(decimal_places=2, max_digits=20)

    def __str__(self):
        return self.fullAddress
