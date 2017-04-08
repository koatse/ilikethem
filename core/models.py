from django.db import models
from .models_geo import Country

class PropertyType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
