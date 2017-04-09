from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Recommendation
from .forms import RecommendationForm

class RecommendationListView(ListView):
    model = Recommendation

class RecommendationDetailView(DetailView):
    model = Recommendation

def CreateRecommendation(request):
    form_class = RecommendationForm

    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            recommendation = form.save()
            return redirect("recommend:all")
    else:
        form = form_class()

    return render(request, "recommend/create_recommendation.html", {'form': form})

