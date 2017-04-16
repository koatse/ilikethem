from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile

class RequireUserProfileMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        try:
            userprofile = UserProfile.objects.get(user=self.request.user)
        except:
            return redirect("core:create")
        self.kwargs["userprofile"] = userprofile
        return super(RequireUserProfileMixin, self).dispatch(request, *args, **kwargs)

