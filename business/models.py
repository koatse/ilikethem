from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from core.models import UserProfile
from mygeo.models import City

class BusinessService(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class BusinessProfile(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    ownby = models.ForeignKey(UserProfile)
    name = models.CharField(max_length=50, verbose_name="Your name or your company name")
    email = models.EmailField(max_length=50, verbose_name="Business email")
    phone = PhoneNumberField(verbose_name="Business phone")
    website = models.URLField(blank = True)
    service  = models.ManyToManyField(BusinessService, verbose_name="Business services provided: (multi-select)")
    city_headquarter = models.ForeignKey(City, verbose_name="City of main office")

    def __str__(self):
        return self.name
