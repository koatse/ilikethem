from django.conf.urls import include, url
from .views import BusinessServiceListView
from .views import BusinessProfileListView, BusinessProfileDetailView
from .views import MyBusinessProfileListView, CreateBusinessProfileView, UpdateBusinessProfileView, DeleteBusinessProfileView

urlpatterns = [
    url(r'^service/all$', BusinessServiceListView.as_view(), name="service_all"),

    url(r'^profile/all$', BusinessProfileListView.as_view(), name="profile_all"),
    url(r'^profile/detail/(?P<pk>\d+)/', BusinessProfileDetailView.as_view(), name="profile_detail"),

    url(r'^profile/my/$', MyBusinessProfileListView.as_view(), name="my"),
    url(r'^profile/create/$', CreateBusinessProfileView.as_view(), name="create"),
    url(r'^profile/edit/(?P<pk>\d+)/', UpdateBusinessProfileView.as_view(), name="edit"),
    url(r'^profile/delete/(?P<pk>\d+)/', DeleteBusinessProfileView.as_view(), name="delete"),
]
