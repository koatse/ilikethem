from django.forms import ModelForm
from . models import Recommendation

class RecommendationForm(ModelForm):
    class Meta:
        model = Recommendation
        exclude = ['user', 'ownby']
