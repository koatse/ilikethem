from django.db import models
from core.models import PropertyType
from mygeo.models import City

class RenovationExperience(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TenantExperience(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class FinancingExperience(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TaxExperience(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class InvestmentExperience(models.Model):
    property_type = models.ManyToManyField(PropertyType, blank = True)
    renovation_experience = models.ManyToManyField(RenovationExperience, blank = True)
    tenant_experience = models.ManyToManyField(TenantExperience, blank = True)
    financing_experience = models.ManyToManyField(FinancingExperience, blank = True)
    tax_experience = models.ManyToManyField(TaxExperience, blank = True)
    city_experience = models.ManyToManyField(City, blank = True)
