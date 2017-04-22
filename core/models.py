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
    fullname = models.CharField(max_length=50, help_text="How fellow investors call you")
    email = models.EmailField(max_length=50, help_text="For other investors to contact you")
    phone = PhoneNumberField(blank = True)
    website = models.URLField(blank = True)
    city = models.ForeignKey(City, verbose_name="Residence City")
    role = models.ForeignKey(Role, verbose_name="Primary role in real estate")
    intro = models.TextField(max_length=200, blank = True, verbose_name="Self introduction")

    property_type = models.ManyToManyField(PropertyType, blank = True, verbose_name="I have invested in: (multi-select)")
    renovation_experience = models.ManyToManyField(RenovationExperience, blank = True, verbose_name="I have done these renovations: (multi-select)")
    tenant_experience = models.ManyToManyField(TenantExperience, blank = True, verbose_name="I have dealt with tenants for: (multi-select)")
    financing_experience = models.ManyToManyField(FinancingExperience, blank = True, verbose_name="I have used following fincancing strateiges: (multi-select)")
    tax_experience = models.ManyToManyField(TaxExperience, blank = True, verbose_name="I have used following tax strategies: (multi-select)")
    city_experience = models.ManyToManyField(City, blank = True, related_name="city_experience", verbose_name="I have invested in: (multi-select)")

    def __str__(self):
        return self.fullname + " (" + self.role.name + ")"
