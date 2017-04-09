from django.conf.urls import include, url
from .views import UserProfileListView, UserProfileDetailView

urlpatterns = [
    url(r'^$', UserProfileListView.as_view(), name="users_all"),
    url(r'^detail/(?P<pk>\d+)/', UserProfileDetailView.as_view(), name="users_detail"),
]
