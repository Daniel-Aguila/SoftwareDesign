from django.db import models

# Create your models here.
class Quote(models.Model):
    gallonsReq = models.PositiveIntegerField()
    fullAddress = models.CharField(max_length=100)
    deliveryDate = models.DateField()
    pricePerGallon = models.DecimalField(decimal_places=2, max_digits=5)
    totalDue = models.DecimalField(decimal_places=2, max_digits=20)

class Profile(models.Model):
    fullName=models.CharField(max_length=50)
    address1=models.CharField(max_length=100)
    address2=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode=models.PositiveIntegerField()
