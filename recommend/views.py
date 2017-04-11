from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic import DetailView
from core.models import UserProfile
from .models import Recommendation
from .forms import RecommendationForm

class RecommendationListView(ListView):
    model = Recommendation

class MyRecommendationListView(ListView):
    model = Recommendation

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Recommendation.objects.filter(user=self.request.user)
        else:
            return Recommendation.objects.all()

class RecommendationDetailView(DetailView):
    model = Recommendation
    
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

