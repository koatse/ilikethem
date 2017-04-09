from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import BusinessService, BusinessProfile

class BusinessServiceListView(ListView):
    model = BusinessService

class BusinessServiceDetailView(DetailView):
    model = BusinessService

class BusinessProfileListView(ListView):
    model = BusinessProfile

class BusinessProfileDetailView(DetailView):
    model = BusinessProfile
