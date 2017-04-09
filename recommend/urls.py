from django.conf.urls import include, url
from .views import RecommendationListView, RecommendationDetailView

urlpatterns = [
    url(r'^$', RecommendationListView.as_view(), name="all"),
    url(r'^detail/(?P<pk>\d+)/', RecommendationDetailView.as_view(), name="detail"),
]
