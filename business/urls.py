from django.conf.urls import include, url
from .views import BusinessServiceListView, BusinessServiceDetailView, BusinessProfileListView, BusinessProfileDetailView

urlpatterns = [
    url(r'^service/$', BusinessServiceListView.as_view(), name="service"),
    url(r'^service/detail/(?P<pk>\d+)/', BusinessServiceDetailView.as_view(), name="service_detail"),
    url(r'^profile/$', BusinessProfileListView.as_view(), name="profile"),
    url(r'^profile/detail/(?P<pk>\d+)/', BusinessProfileDetailView.as_view(), name="profile_detail"),
]
