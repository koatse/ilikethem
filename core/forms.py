from django.forms import ModelForm
from . models import UserProfile

class UserProfileForm(ModelForm):
    #the user field should be auto assigned
    class Meta:
        model = UserProfile
        #fields = '__all__'
        exclude = ['user']
