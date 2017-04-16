from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from business.models import BusinessProfile
from recommend.models import Recommendation
from django.core.mail import send_mail

class UserProfileListView(ListView):
    model = UserProfile

class UserProfileDetailView(DetailView):
    model = UserProfile
    def get_context_data(self, **kwargs):
        context = super(UserProfileDetailView, self).get_context_data(**kwargs)
        context["recommendations"] = Recommendation.objects.filter(ownby=context["object"].pk)
        context["business_profiles"] = BusinessProfile.objects.filter(ownby=context["object"].pk)
        return context

@login_required
def CreateUserProfile(request):
    form_class = UserProfileForm

    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.user = request.user
            userprofile.save()
            form.save_m2m()
            return redirect("core:detail", pk=userprofile.pk)
    else:
        form = form_class()

    return render(request, "core/create.html", {'form': form})

@login_required
def EditUserProfile(request):
    try:
        userprofile = UserProfile.objects.get(user=request.user)
    except:
        return redirect("core:create")

    form_class = UserProfileForm

    if request.method == "POST":
        form = form_class(request.POST, instance=userprofile)
        if form.is_valid():
            form.save()
            return redirect("core:detail", pk=userprofile.pk)
    else:
        form = form_class(instance=userprofile)

    return render(request, "core/edit_userprofile.html", {'form': form})

@login_required
def MyUserProfileView(request):
    try:
        userprofile = UserProfile.objects.get(user=request.user)
    except:
        return redirect("core:create")
    #send_mail('subject', 'body of the message', 'noreply@myrein.com', ['koatse@gmail.com'])
    return redirect("core:detail", pk=userprofile.pk)
