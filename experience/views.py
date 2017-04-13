from django.shortcuts import render, reverse
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic import CreateView, UpdateView
from .models import RenovationExperience, TenantExperience, FinancingExperience, TaxExperience

class ExperienceMixin(object):
    def get_context_data(self, **kwargs):
        context = super(ExperienceMixin, self).get_context_data(**kwargs)
        context["renovation"] = RenovationExperience.objects.all()
        context["tenant"] = TenantExperience.objects.all()
        context["financing"] = FinancingExperience.objects.all()
        context["tax"] = TaxExperience.objects.all()
        return context

class CreateMixin(object):
    def get_context_data(self, **kwargs):
        context = super(CreateMixin, self).get_context_data(**kwargs)
        context["mode"] = "Create"
        return context

class UpdateMixin(object):
    def get_context_data(self, **kwargs):
        context = super(UpdateMixin, self).get_context_data(**kwargs)
        context["mode"] = "Update"
        return context

class ExperienceView(ExperienceMixin, TemplateView):
    template_name = "experience/all.html"

class RenovationMixin(ExperienceMixin):
    model = RenovationExperience
    fields = '__all__'
    template_name = "experience/reno.html"

    def get_success_url(self):
        return reverse("experience:all")

class CreateRenovationExperienceView(RenovationMixin, CreateMixin, CreateView):
    pass

class UpdateRenovationExperienceView(RenovationMixin, UpdateMixin, UpdateView):
    pass

