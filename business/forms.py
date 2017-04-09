from django.forms import ModelForm
from . models import BusinessService, BusinessProfile

class BusinessServiceForm(ModelForm):
    class Meta:
        model = BusinessService
        fields = '__all__'

class BusinessProfileForm(ModelForm):
    class Meta:
        model = BusinessProfile
        fields = '__all__'
