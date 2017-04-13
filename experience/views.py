from django.shortcuts import render, reverse
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic import CreateView, UpdateView
from .models import RenovationExperience, TenantExperience, FinancingExperience, TaxExperience

class ExperienceView(TemplateView):
    template_name = "experience/all.html"

    def get_context_data(self, **kwargs):
        context = super(ExperienceView, self).get_context_data(**kwargs)
        context["renovation"] = RenovationExperience.objects.all()
        context["tenant"] = TenantExperience.objects.all()
        context["financing"] = FinancingExperience.objects.all()
        context["tax"] = TaxExperience.objects.all()
        return context

class CreateRenovationExperienceView(CreateView):
    model = RenovationExperience
    fields = '__all__'
    template_name = "experience/reno.html"

    def get_success_url(self):
        return reverse("experience:all")

    def get_context_data(self, **kwargs):
        context = super(CreateRenovationExperienceView, self).get_context_data(**kwargs)
        context["renovation_experience"] = RenovationExperience.objects.all()
        context["mode"] = "Create"
        return context

class UpdateRenovationExperienceView(UpdateView):
    model = RenovationExperience
    fields = '__all__'
    template_name = "experience/reno.html"

    def get_success_url(self):
        return reverse("experience:all")

    def get_context_data(self, **kwargs):
        context = super(UpdateRenovationExperienceView, self).get_context_data(**kwargs)
        context["renovation_experience"] = RenovationExperience.objects.all()
        context["mode"] = "Edit"
        return context
