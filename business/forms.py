from django import forms
from django.forms import ModelForm
from . models import BusinessService, BusinessProfile

class BusinessServiceForm(ModelForm):
    class Meta:
        model = BusinessService
        fields = '__all__'

class BusinessProfileForm(ModelForm):
    service = forms.ModelMultipleChoiceField(queryset=BusinessService.objects.all(), widget=forms.CheckboxSelectMultiple(),required=True, label="Business services provided:")
    class Meta:
        model = BusinessProfile
        exclude = ['user', 'ownby']
