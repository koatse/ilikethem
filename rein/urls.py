"""rein URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (password_reset, password_reset_done, password_reset_confirm, password_reset_complete)
from .backends import MyRegistrationView
from .views import HomeView
from .views import AboutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^business/', include('business.urls', namespace="business")),
    url(r'^experience/', include('experience.urls', namespace="experience")),
    url(r'^recommend/', include('recommend.urls', namespace="recommend")),
    url(r'^core/', include('core.urls', namespace="core")),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name="register"),
    url(r'^accounts/', include('registration.backends.simple.urls')),

    #password reset
    url(r'^accounts/password/reset/$', 
        password_reset,
        {'template_name':
        'registration/password_reset_form.html'},
        name="password_reset"),
    url(r'^accounts/password/reset/done/$',
        password_reset_done,
        {'template_name':
        'registration/password_reset_done.html'},
        name="password_reset_done"),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        password_reset_confirm,
        {'template_name':
        'registration/password_reset_confirm.html'},
        name="password_reset_confirm"),
    url(r'^accounts/password/done/$', 
        password_reset_complete,
        {'template_name':
        'registration/password_reset_complete.html'},
        name="password_reset_complete"),

    #Login/Logout
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^$', HomeView, name="home"),
    url(r'^about/$', AboutView, name="about"),
    #url(r'^$', include('core.urls', namespace="core")),

]
