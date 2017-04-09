from django.conf.urls import include, url
from .views import BusinessServiceListView, BusinessServiceDetailView, BusinessProfileListView, BusinessProfileDetailView
from .views import CreateBusinessService, CreateBusinessProfile, EditBusinessProfile, DeleteBusinessProfile

urlpatterns = [
    url(r'^service/$', BusinessServiceListView.as_view(), name="service"),
    url(r'^service/detail/(?P<pk>\d+)/', BusinessServiceDetailView.as_view(), name="service_detail"),
    url(r'^profile/$', BusinessProfileListView.as_view(), name="profile"),
    url(r'^profile/detail/(?P<pk>\d+)/', BusinessProfileDetailView.as_view(), name="profile_detail"),
    url(r'^service/create/$', CreateBusinessService, name="create_service"),
    url(r'^profile/create/$', CreateBusinessProfile, name="create_profile"),
    url(r'^profile/edit/(?P<pk>\d+)/', EditBusinessProfile, name="edit_profile"),
    url(r'^profile/delete/(?P<pk>\d+)/', DeleteBusinessProfile, name="delete_profile"),
]
