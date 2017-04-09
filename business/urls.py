from django.conf.urls import include, url
from .views import BusinessServiceListView, BusinessServiceDetailView, BusinessProfileListView, BusinessProfileDetailView

urlpatterns = [
    url(r'^service/$', BusinessServiceListView.as_view()),
    url(r'^service/detail/(?P<pk>\d+)/', BusinessServiceDetailView.as_view()),
    url(r'^profile/$', BusinessProfileListView.as_view()),
    url(r'^profile/detail/(?P<pk>\d+)/', BusinessProfileDetailView.as_view()),
]
