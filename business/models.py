from django.db import models

class BusinessService(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BusinessProfile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    website = models.URLField(blank = True)
    service  = models.ManyToManyField(BusinessService, blank = True)

    def __str__(self):
        return self.name
