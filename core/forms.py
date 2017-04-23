from django import forms
from django.forms import ModelForm
from . models import UserProfile
from . models import PropertyType, RenovationExperience, TenantExperience, FinancingExperience, TaxExperience, City

class UserProfileForm(ModelForm):
    property_type = forms.ModelMultipleChoiceField(queryset=PropertyType.objects.all(), widget=forms.CheckboxSelectMultiple(),required=True, label="I have these investment experiences:")
    renovation_experience = forms.ModelMultipleChoiceField(queryset=RenovationExperience.objects.all(), widget=forms.CheckboxSelectMultiple(),required=True, label="I have these renovation experiences:")
    tenant_experience = forms.ModelMultipleChoiceField(queryset=TenantExperience.objects.all(), widget=forms.CheckboxSelectMultiple(),required=True, label="I have these tenant experiences:")
    financing_experience = forms.ModelMultipleChoiceField(queryset=FinancingExperience.objects.all(), widget=forms.CheckboxSelectMultiple(),required=True, label="I have these financing experiences:")
    tax_experience = forms.ModelMultipleChoiceField(queryset=TaxExperience.objects.all(), widget=forms.CheckboxSelectMultiple(),required=True, label="I have these tax experiences:")
    city_experience = forms.ModelMultipleChoiceField(queryset=City.objects.all(), widget=forms.CheckboxSelectMultiple(),required=True, label="I have invested in these cities:")

    class Meta:
        model = UserProfile
        exclude = ['user']
