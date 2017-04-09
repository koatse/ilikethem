from django.conf.urls import include, url
from .views import UserProfileListView, UserProfileDetailView
from .views import CreateUserProfile, EditUserProfile

urlpatterns = [
    url(r'^$', UserProfileListView.as_view(), name="userprofile_all"),
    url(r'^detail/(?P<pk>\d+)/', UserProfileDetailView.as_view(), name="userprofile_detail"),
    url(r'^create/$', CreateUserProfile, name="create_userprofile"),
    url(r'^edit/$', EditUserProfile, name="edit_userprofile"),
]
