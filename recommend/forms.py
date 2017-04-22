from django.forms import ModelForm
from . models import Recommendation

class RecommendationForm(ModelForm):
    class Meta:
        model = Recommendation
        exclude = ['user', 'ownby']

    def __init__(self, *args, **kwargs):
        super(RecommendationForm, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'placeholder': 'optional'})  
        self.fields['website'].widget.attrs.update({'placeholder': 'optional'})  
