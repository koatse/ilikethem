from django.conf.urls import include, url
from .views import ExperienceView

urlpatterns = [
    url(r'^$', ExperienceView.as_view(), name="all"),
]
