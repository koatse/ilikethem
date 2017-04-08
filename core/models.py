from django.db import models
from mygeo.models import City
from phonenumber_field.modelfields import PhoneNumberField
from experience.models import RenovationExperience, TenantExperience, FinancingExperience, TaxExperience
from business.models import BusinessProfile

class PropertyType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = PhoneNumberField(blank = True)
    website = models.URLField(blank = True)
    city = models.ManyToManyField(City)

    role = models.ForeignKey(Role)

    property_type = models.ManyToManyField(PropertyType, blank = True)
    renovation_experience = models.ManyToManyField(RenovationExperience, blank = True)
    tenant_experience = models.ManyToManyField(TenantExperience, blank = True)
    financing_experience = models.ManyToManyField(FinancingExperience, blank = True)
    tax_experience = models.ManyToManyField(TaxExperience, blank = True)
    city_experience = models.ManyToManyField(City, blank = True, related_name="city_experience")

    businessprofile = models.ManyToManyField(BusinessProfile, blank = True)

    def __str__(self):
        return self.name
