from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import UserProfile
from business.models import BusinessProfile
from recommend.models import Recommendation

class UserProfileListView(ListView):
    model = UserProfile

class UserProfileDetailView(DetailView):
    model = UserProfile
    def get_context_data(self, **kwargs):
        context = super(UserProfileDetailView, self).get_context_data(**kwargs)
        context["recommendations"] = Recommendation.objects.filter(ownby=context["object"].pk)
        context["business_profiles"] = BusinessProfile.objects.filter(ownby=context["object"].pk)
        return context
