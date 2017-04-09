from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Recommendation
from .forms import RecommendationForm

class RecommendationListView(ListView):
    model = Recommendation

class RecommendationDetailView(DetailView):
    model = Recommendation
    
@login_required
def CreateRecommendation(request):
    form_class = RecommendationForm

    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            recommendation = form.save(commit=False)
            recommendation.user = request.user
            recommendation.ownby = userprofile
            recommendation.save()
            form.save_m2m()
            return redirect("recommend:all")
    else:
        form = form_class()

    return render(request, "recommend/create_recommendation.html", {'form': form})

