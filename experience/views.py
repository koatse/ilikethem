from django.shortcuts import render, reverse
from django.views.generic import TemplateView
from .models import RenovationExperience, TenantExperience, FinancingExperience, TaxExperience

class ExperienceMixin(object):
    def get_context_data(self, **kwargs):
        context = super(ExperienceMixin, self).get_context_data(**kwargs)
        context["renovation"] = RenovationExperience.objects.all()
        context["tenant"] = TenantExperience.objects.all()
        context["financing"] = FinancingExperience.objects.all()
        context["tax"] = TaxExperience.objects.all()
        return context

class ExperienceView(ExperienceMixin, TemplateView):
    template_name = "experience/all.html"
