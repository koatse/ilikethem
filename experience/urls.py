from django.conf.urls import include, url
from .views import ExperienceView
from .views import CreateRenovationExperienceView

urlpatterns = [
    url(r'^$', ExperienceView.as_view(), name="all"),
    url(r'^create_reno/$', CreateRenovationExperienceView.as_view(), name="create_reno"),
]
