from django.conf.urls import include, url
from .views import RecommendationListView, MyRecommendationListView, RecommendationDetailView
from .views import EditRecommendation, DeleteRecommendation
from .views import CreateRecommendationView

urlpatterns = [
    url(r'^all/$', RecommendationListView.as_view(), name="all"),
    url(r'^my/$', MyRecommendationListView.as_view(), name="my"),

    url(r'^detail/(?P<pk>\d+)/', RecommendationDetailView.as_view(), name="detail"),

    url(r'^create/$', CreateRecommendationView.as_view(), name="create"),
    url(r'^edit/(?P<pk>\d+)/', EditRecommendation, name="edit"),
    url(r'^delete/(?P<pk>\d+)/', DeleteRecommendation, name="delete"),

]
