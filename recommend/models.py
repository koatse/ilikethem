from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from mygeo.models import City
from core.models import UserProfile
from business.models import BusinessService

SATISFACTION_CHOICES = (
         (0, "GOOD"),
         (1, "GREAT"),
         (2, "AWESOME"),
         (3, "PERFECT"),
)
SPENDING_CHOICES = (
        (-1, "Not Applicable"),
        (0, "$1 - $99"),
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
     user = models.ForeignKey(User, blank=True, null=True)
     ownby = models.ForeignKey(UserProfile)
     name = models.CharField(max_length=50, verbose_name="Business Owner/Company name")
     email = models.EmailField(max_length=50)
     phone = PhoneNumberField(blank = True)
     website = models.URLField(blank = True)
     #should i make this many to many/checkbox ?
     service  = models.ForeignKey(BusinessService)
     #should i make this checkbox ?
     city_serviced = models.ManyToManyField(City, verbose_name="Cities where they provided service to me")

     satisfaction = models.IntegerField(choices=SATISFACTION_CHOICES, default=0, verbose_name="They make me feel")
     total_money_spent = models.IntegerField(choices=SPENDING_CHOICES, default=0, verbose_name="Total purchase so far", help_text="Select N/A if you don't directly pay (e.g. buyer realtor)")
     pricing = models.IntegerField(choices=PRICING_CHOICES, default=1, verbose_name="Price point")
     on_active_contract = models.BooleanField(default = False, verbose_name="I have a ongoing contract with this business")
     is_repeated_customer = models.BooleanField(default = False, verbose_name="I am a repeated customer of this business")
     main_reason_to_reuse = models.IntegerField(choices=REUSE_REASON_CHOICES, default = 5, verbose_name="Why I like them:")
     story = models.TextField(max_length=1000, blank = True, verbose_name="My happy story working with them:", default="")

     def __str__(self):
         return self.name + " (" + self.service.name + ")" + " - " + self.get_main_reason_to_reuse_display()
