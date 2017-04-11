from django.conf.urls import include, url
from .views import RecommendationListView, MyRecommendationListView, RecommendationDetailView
from .views import CreateRecommendation

urlpatterns = [
    url(r'^all/$', RecommendationListView.as_view(), name="all"),
    url(r'^my/$', MyRecommendationListView.as_view(), name="my"),
    url(r'^detail/(?P<pk>\d+)/', RecommendationDetailView.as_view(), name="detail"),
    url(r'^create/$', CreateRecommendation, name="create"),
]
