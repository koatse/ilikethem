from django.db import models
from mygeo.models import Country

class PropertyType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BusinessService(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
