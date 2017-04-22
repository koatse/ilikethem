from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from core.mixin import RequireUserProfileMixin
from .models import BusinessService, BusinessProfile
from .forms import BusinessProfileForm

class BusinessServiceListView(ListView):
    model = BusinessService
    template_name = "business/businessservice_list.html"

class BusinessProfileListView(ListView):
    model = BusinessProfile
    template_name = "business/businessprofile_list.html"

    def get_queryset(self):
        qs = super(BusinessProfileListView, self).get_queryset().order_by("user")
        return qs

class BusinessProfileDetailView(DetailView):
    model = BusinessProfile
    template_name = "business/businessprofile_detail.html"

class MyBusinessProfileListView(RequireUserProfileMixin, ListView):
    model = BusinessProfile
    template_name = "business/businessprofile_list.html"

    def get_queryset(self):
        return BusinessProfile.objects.filter(user=self.request.user)

class CreateBusinessProfileView(RequireUserProfileMixin, CreateView):
    model = BusinessProfile
    form_class = BusinessProfileForm
    template_name = "business/businessprofile_create.html"

    def form_valid(self, form):
        business_profile = form.save(commit=False)
        business_profile.user = self.request.user
        business_profile.ownby = self.kwargs.get("userprofile")
        business_profile.save()
        form.save_m2m()
        return redirect("business:my")

class UpdateBusinessProfileView(RequireUserProfileMixin, UpdateView):
    model = BusinessProfile
    form_class = BusinessProfileForm
    template_name = "business/businessprofile_edit.html"

    def form_valid(self, form):
        form.save()
        return redirect("business:my")

class DeleteBusinessProfileView(RequireUserProfileMixin, DeleteView):
    model = BusinessProfile
    template_name = "business/businessprofile_delete.html"

    def delete(self, request, *args, **kwargs):
        try:
            businessprofile = BusinessProfile.objects.get(pk=self.kwargs.get("pk"))
            businessprofile.delete()
        except:
            pass
        return redirect("business:my")
