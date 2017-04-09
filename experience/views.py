from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView
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
