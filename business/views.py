from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic import DetailView
from core.models import UserProfile
from .models import BusinessService, BusinessProfile
from .forms import BusinessServiceForm
from .forms import BusinessProfileForm

class BusinessServiceListView(ListView):
    model = BusinessService

class BusinessServiceDetailView(DetailView):
    model = BusinessService

class BusinessProfileListView(ListView):
    model = BusinessProfile

class MyBusinessProfileListView(ListView):
    model = BusinessProfile

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return BusinessProfile.objects.filter(user=self.request.user)
        else:
            return BusinessProfile.objects.all()


class BusinessProfileDetailView(DetailView):
    model = BusinessProfile

def CreateBusinessService(request):
    form_class = BusinessServiceForm

    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            business_service = form.save()
            #Got here? created new object
            return redirect("business:service")
    else:
        #Got here? when user comes here first time
        form = form_class()

    #Got here? either first time or failed to create new object
    return render(request, "business/create_business_service.html", {'form': form})

@login_required
def CreateBusinessProfile(request):
    form_class = BusinessProfileForm
    try:
        userprofile = UserProfile.objects.get(user=request.user)
    except:
        raise Http404("Current logged in user " + str(request.user) + " has no userprofile")

    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            business_profile = form.save(commit=False)
            business_profile.user = request.user
            business_profile.ownby = userprofile
            business_profile.save()
            form.save_m2m()
            return redirect("business:profile")
    else:
        form = form_class()

    return render(request, "business/create_business_profile.html", {'form': form})

@login_required
def EditBusinessProfile(request, pk):
    try:
        businessprofile = BusinessProfile.objects.get(pk=pk)
    except:
        return redirect("business:create_profile")

    form_class = BusinessProfileForm

    if request.method == "POST":
        form = form_class(request.POST, instance=businessprofile)
        if form.is_valid():
            form.save()
            return redirect("business:profile_detail", pk=businessprofile.pk)
    else:
        form = form_class(instance=businessprofile)

    return render(request, "business/edit_business_profile.html", {'form': form})

@login_required
def DeleteBusinessProfile(request, pk):
    try:
        businessprofile = BusinessProfile.objects.get(pk=pk)
        ownby = businessprofile.ownby
        businessprofile.delete()
    except:
        return redirect("business:profile")

    return redirect("core:userprofile_detail", ownby.pk)


