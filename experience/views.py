from django.shortcuts import render, reverse
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic import CreateView
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
    template_name = "experience/create_reno.html"

    def get_success_url(self):
        return reverse("experience:all")

    #optional extra context to pass to template
    #def get_context_data(self, **kwargs):
    #    context = super(CreateRenovationExperienceView, self).get_context_data(**kwargs)
    #    return context
