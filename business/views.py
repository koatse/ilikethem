from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import BusinessService, BusinessProfile
from .forms import BusinessServiceForm

class BusinessServiceListView(ListView):
    model = BusinessService

class BusinessServiceDetailView(DetailView):
    model = BusinessService

class BusinessProfileListView(ListView):
    model = BusinessProfile

class BusinessProfileDetailView(DetailView):
    model = BusinessProfile

def CreateBusinessService(request):
    form_class = BusinessServiceForm

    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            business_service = form.save()
            return redirect("business:service")
    else:
        form = form_class()

    return render(request, "business/create_business_service.html", {'form': form})

