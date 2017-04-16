from .models import UserProfile

class RequireUserProfileMixin(object):
    def dispatch(self, request, *args, **kwargs):
        try:
            userprofile = UserProfile.objects.get(user=self.request.user)
        except:
            return redirect("core:create")
        self.kwargs["userprofile"] = userprofile
        return super(RequireUserProfileMixin, self).dispatch(request, *args, **kwargs)

