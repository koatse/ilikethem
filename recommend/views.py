from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from core.mixin import RequireUserProfileMixin
from .models import Recommendation
from .forms import RecommendationForm
import logging
logger = logging.getLogger("recommend")

class RecommendationListView(ListView):
    model = Recommendation
    template_name = "recommend/list.html"

class RecommendationDetailView(DetailView):
    model = Recommendation
    template_name = "recommend/detail.html"

class MyRecommendationListView(RequireUserProfileMixin, ListView):
    model = Recommendation
    template_name = "recommend/list.html"

    def get_queryset(self):
        return Recommendation.objects.filter(user=self.request.user)

class CreateRecommendationView(RequireUserProfileMixin, CreateView):
    model = Recommendation
    form_class = RecommendationForm
    template_name = "recommend/create.html"

    def form_valid(self, form):
        recommendation = form.save(commit=False)
        recommendation.user = self.request.user
        recommendation.ownby = self.kwargs.get("userprofile")
        recommendation.save()
        form.save_m2m()
        return redirect("recommend:my")

class UpdateRecommendationView(RequireUserProfileMixin, UpdateView):
    model = Recommendation
    form_class = RecommendationForm
    template_name = "recommend/edit.html"

    def form_valid(self, form):
        form.save()
        return redirect("recommend:my")

class DeleteRecommendationView(RequireUserProfileMixin, DeleteView):
    model = Recommendation
    template_name = "recommend/delete.html"

    def delete(self, request, *args, **kwargs):
        try:
            recommendation = Recommendation.objects.get(pk=self.kwargs.get("pk"))
            recommendation.delete()
        except:
            pass
        return redirect("recommend:my")
