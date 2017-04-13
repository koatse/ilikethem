from django.conf.urls import include, url
from .views import ExperienceView
from .views import CreateRenovationExperienceView, UpdateRenovationExperienceView, DeleteRenovationExperienceView

urlpatterns = [
    url(r'^$', ExperienceView.as_view(), name="all"),
    url(r'^create_reno/$', CreateRenovationExperienceView.as_view(), name="create_reno"),
    url(r'^edit_reno/(?P<pk>\d+)/$', UpdateRenovationExperienceView.as_view(), name="edit_reno"),
    url(r'^delete_reno/(?P<pk>\d+)/$', DeleteRenovationExperienceView.as_view(), name="delete_reno"),
]
