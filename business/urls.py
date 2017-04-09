from django.conf.urls import include, url
from .views import BusinessServiceListView

urlpatterns = [
    url(r'^$', BusinessServiceListView.as_view()),
]
