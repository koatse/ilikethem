from django.db import models
from django.contrib.auth.models import User
from mygeo.models import City
from phonenumber_field.modelfields import PhoneNumberField
from experience.models import RenovationExperience, TenantExperience, FinancingExperience, TaxExperience

class PropertyType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = PhoneNumberField(blank = True)
    website = models.URLField(blank = True)
    city = models.ForeignKey(City)

    role = models.ForeignKey(Role)
    intro = models.TextField(max_length=200, blank = True, default="")

    property_type = models.ManyToManyField(PropertyType, blank = True)
    renovation_experience = models.ManyToManyField(RenovationExperience, blank = True)
    tenant_experience = models.ManyToManyField(TenantExperience, blank = True)
    financing_experience = models.ManyToManyField(FinancingExperience, blank = True)
    tax_experience = models.ManyToManyField(TaxExperience, blank = True)
    city_experience = models.ManyToManyField(City, blank = True, related_name="city_experience")

    def __str__(self):
        return self.fullname + " (" + self.role.name + ")"
