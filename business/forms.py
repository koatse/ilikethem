from django.forms import ModelForm
from . models import BusinessService

class BusinessServiceForm(ModelForm):
    class Meta:
        model = BusinessService
        fields = '__all__'
