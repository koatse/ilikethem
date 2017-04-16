from django.conf.urls import include, url
from .views import UserProfileListView, UserProfileDetailView
from .views import CreateUserProfile, EditUserProfile, MyUserProfileView

urlpatterns = [
    url(r'^all/$', UserProfileListView.as_view(), name="all"),
    url(r'^detail/(?P<pk>\d+)/', UserProfileDetailView.as_view(), name="detail"),

    url(r'^my/$', MyUserProfileView, name="my"),
    url(r'^create/$', CreateUserProfile, name="create"),
    url(r'^edit/$', EditUserProfile, name="edit"),
    #cannot delete 
]
