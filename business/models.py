from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from core.models import UserProfile
from mygeo.models import City

class BusinessService(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BusinessProfile(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    ownby = models.ForeignKey(UserProfile)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = PhoneNumberField()
    website = models.URLField(blank = True)
    service  = models.ManyToManyField(BusinessService)
    city_headquarter = models.ForeignKey(City)

    def __str__(self):
        return self.name
