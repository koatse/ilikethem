from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from core.mixin import RequireUserProfileMixin
from .models import BusinessService, BusinessProfile
from .forms import BusinessProfileForm

class BusinessServiceListView(ListView):
    model = BusinessService

class BusinessProfileListView(ListView):
    model = BusinessProfile

class BusinessProfileDetailView(DetailView):
    model = BusinessProfile

class MyBusinessProfileListView(LoginRequiredMixin, ListView):
    model = BusinessProfile

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return BusinessProfile.objects.filter(user=self.request.user)
        else:
            return BusinessProfile.objects.all()

class CreateBusinessProfileView(LoginRequiredMixin, RequireUserProfileMixin, CreateView):
    model = BusinessProfile
    form_class = BusinessProfileForm
    template_name = "business/create_business_profile.html"

    def form_valid(self, form):
        business_profile = form.save(commit=False)
        business_profile.user = self.request.user
        business_profile.ownby = self.kwargs.get("userprofile")
        business_profile.save()
        form.save_m2m()
        return redirect("business:my")

class UpdateBusinessProfileView(LoginRequiredMixin, UpdateView):
    model = BusinessProfile
    form_class = BusinessProfileForm
    template_name = "business/edit_business_profile.html"

    def form_valid(self, form):
        form.save()
        return redirect("business:my")

class DeleteBusinessProfileView(LoginRequiredMixin, DeleteView):
    model = BusinessProfile
    template_name = "business/delete.html"

    def delete(self, request, *args, **kwargs):
        try:
            businessprofile = BusinessProfile.objects.get(pk=self.kwargs.get("pk"))
            businessprofile.delete()
        except:
            pass
        return redirect("business:my")
