from django.shortcuts import render
from django.views.generic.list import ListView
from .models import BusinessService

class BusinessServiceListView(ListView):
    model = BusinessService
