from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from mygeo.models import City

class BusinessService(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BusinessProfile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = PhoneNumberField()
    website = models.URLField(blank = True)
    service  = models.ManyToManyField(BusinessService)
    city_headquarter = models.ForeignKey(City)

    def __str__(self):
        return self.name
