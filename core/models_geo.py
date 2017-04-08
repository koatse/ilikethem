from django.db import models

import cities_light
from cities_light.settings import ICity
from cities_light.abstract_models import AbstractCountry, AbstractRegion, AbstractCity
from cities_light.receivers import connect_default_signals
#from cities_light.models import City, Country

def filter_region_import(sender, items, **kwargs):
    #items[2] is State/Province name
    #print("items[2]", items[2])
    if items[2] not in (['Ontario']):
        raise cities_light.InvalidItems()
cities_light.signals.region_items_pre_import.connect(filter_region_import)

def filter_city_import(sender, items, **kwargs):
    #items[1] is City name
    #if(items[1] == 'Markham'):
    #    print("items[1]", items[1])
    #    print("items[8]", items[8])
    #    print("items[10]", items[10])
    #items[8] is country code, items[10] is province/state code
    if items[8] not in (['CA']) or items[10] not in (['08']):
        raise cities_light.InvalidItems()
cities_light.signals.city_items_pre_import.connect(filter_city_import)

#def set_city_fields(sender, instance, items, **kwargs):
#    instance.timezone = items[ICity.timezone]
#cities_light.signals.city_items_post_import.connect(set_city_fields)

class Country(AbstractCountry):
    pass
connect_default_signals(Country)

class Region(AbstractRegion):
    pass
connect_default_signals(Region)

class City(AbstractCity):
    #timezone = models.CharField(max_length=40, null=True)
    pass
connect_default_signals(City)

class Province(models.Model):
    name = models.CharField(max_length=100, default="province", null = True)
    region = models.ForeignKey(Region, null = True)

    def __str__(self):
        return self.region
