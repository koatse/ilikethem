from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from mygeo.models import City
from business.models import BusinessService

SATISFACTION_CHOICES = (
         (0, "GOOD"),
         (1, "GREAT"),
         (2, "AWESOME"),
         (3, "PERFECT"),
)
SPENDING_CHOICES = (
        (0, "$0 - $99"),
        (1, "$100 - $199"),
        (2, "$200 - $499"),
        (3, "$500 - $999"),
        (4, "$1,000 - $1,999"),
        (5, "$2,000 - $4,999"),
        (6, "$5,000 - $9,999"),
        (7, "$10,000 - $19,999"),
        (8, "$20,000 - $49,999"),
        (9, "$50,000 - $99,999"),
        (10, "$100,000 - $199,999"),
        (11, "$200,000 - $499,999"),
        (12, "$500,000 - $999,999"),
)
PRICING_CHOICES = (
        (0, "Budget"),
        (1, "AveragePrice"),
        (2, "Premium"),
)
REUSE_REASON_CHOICES = (
        (0, "LowPrice"),
        (1, "Expertise"),
        (2, "CustomerService"),
        (3, "Availability"),
        (4, "Workmanship"),
        (5, "Satisfied"),
)

class Recommendation(models.Model):
     name = models.CharField(max_length=50)
     email = models.EmailField(max_length=50)
     phone = PhoneNumberField(blank = True)
     website = models.URLField(blank = True)
     service  = models.ForeignKey(BusinessService)
     city_serviced = models.ManyToManyField(City)

     satisfaction = models.IntegerField(choices=SATISFACTION_CHOICES, default=0)
     total_money_spent = models.IntegerField(choices=SPENDING_CHOICES, default=0)
     pricing = models.IntegerField(choices=PRICING_CHOICES, default=1)
     on_active_contract = models.BooleanField(default = False)
     is_repeated_customer = models.BooleanField(default = False)
     main_reason_to_reuse = models.IntegerField(choices=REUSE_REASON_CHOICES, default = 5)

     def __str__(self):
         return self.name + " (" + self.service.name + ")" + " - " + REUSE_REASON_CHOICES[self.main_reason_to_reuse][1]


