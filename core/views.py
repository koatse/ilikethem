from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import UserProfile

class UserProfileListView(ListView):
    model = UserProfile

class UserProfileDetailView(DetailView):
    model = UserProfile
