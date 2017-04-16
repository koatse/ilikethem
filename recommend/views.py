from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from core.models import UserProfile
from .models import Recommendation
from .forms import RecommendationForm
import logging
logger = logging.getLogger("recommend")

class RecommendationListView(ListView):
    model = Recommendation

class RecommendationDetailView(DetailView):
    model = Recommendation

class MyRecommendationListView(LoginRequiredMixin, ListView):
    model = Recommendation

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Recommendation.objects.filter(user=self.request.user)
        else:
            return Recommendation.objects.all()

@login_required
def CreateRecommendation(request):
    try:
        userprofile = UserProfile.objects.get(user=request.user)
    except:
        return redirect("core:create_userprofile")

    form_class = RecommendationForm

    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            recommendation = form.save(commit=False)
            recommendation.user = request.user
            recommendation.ownby = userprofile
            recommendation.save()
            form.save_m2m()
            return redirect("recommend:my")
    else:
        form = form_class()

    return render(request, "recommend/create_recommendation.html", {'form': form})

@login_required
def EditRecommendation(request, pk):
    try:
        recommendation = Recommendation.objects.get(pk=pk)
    except:
        return redirect("recommend:create")

    form_class = RecommendationForm

    if request.method == "POST":
        form = form_class(request.POST, instance=recommendation)
        if form.is_valid():
            form.save()
            return redirect("recommend:detail", pk=recommendation.pk)
    else:
        form = form_class(instance=recommendation)

    return render(request, "recommend/edit_recommendation.html", {'form': form})

@login_required
def DeleteRecommendation(request, pk):
    try:
        recommendation = Recommendation.objects.get(pk=pk)
        ownby = recommendation.ownby
        recommendation.delete()
    except:
        return redirect("recommend:my")

    return redirect("core:userprofile_detail", ownby.pk)

#TODO: how to log to the terminal ?
class RequireUserProfileMixin(object):
    def dispatch(self, request, *args, **kwargs):
        logger.info("dispatch")
        try:
            userprofile = UserProfile.objects.get(user=self.request.user)
        except:
            return redirect("core:create_userprofile")
        self.kwargs["userprofile"] = userprofile
        return super(RequireUserProfileMixin, self).dispatch(request, *args, **kwargs)

class CreateRecommendationView(LoginRequiredMixin, RequireUserProfileMixin, CreateView):
    model = Recommendation
    form_class = RecommendationForm
    template_name = "recommend/create_recommendation.html"

    def get_success_url(self):
        return reverse("recommend:my")

    def form_valid(self, form):
        recommendation = form.save(commit=False)
        recommendation.user = self.request.user
        recommendation.ownby = self.kwargs.get("userprofile")
        recommendation.save()
        form.save_m2m()
        return redirect("recommend:my")
