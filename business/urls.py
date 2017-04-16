from django.conf.urls import include, url
from .views import BusinessServiceListView, BusinessServiceDetailView, BusinessProfileListView, MyBusinessProfileListView, BusinessProfileDetailView
from .views import CreateBusinessProfileView, UpdateBusinessProfileView, DeleteBusinessProfileView

urlpatterns = [
    url(r'^service/$', BusinessServiceListView.as_view(), name="service"),
    url(r'^service/detail/(?P<pk>\d+)/', BusinessServiceDetailView.as_view(), name="service_detail"),

    url(r'^profile/$', BusinessProfileListView.as_view(), name="profile"),
    url(r'^profile/detail/(?P<pk>\d+)/', BusinessProfileDetailView.as_view(), name="profile_detail"),

    url(r'^myprofile/$', MyBusinessProfileListView.as_view(), name="myprofile"),
    url(r'^profile/create/$', CreateBusinessProfileView.as_view(), name="create"),
    url(r'^profile/edit/(?P<pk>\d+)/', UpdateBusinessProfileView.as_view(), name="edit"),
    url(r'^profile/delete/(?P<pk>\d+)/', DeleteBusinessProfileView.as_view(), name="delete"),
]
