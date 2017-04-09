from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Recommendation

class RecommendationListView(ListView):
    model = Recommendation

class RecommendationDetailView(DetailView):
    model = Recommendation
