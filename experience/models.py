from django.db import models
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

