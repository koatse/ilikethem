from django.conf.urls import include, url
from .views import RecommendationListView, RecommendationDetailView
from .views import CreateRecommendation

urlpatterns = [
    url(r'^$', RecommendationListView.as_view(), name="all"),
    url(r'^detail/(?P<pk>\d+)/', RecommendationDetailView.as_view(), name="detail"),
    url(r'^create/$', CreateRecommendation, name="create"),
]
