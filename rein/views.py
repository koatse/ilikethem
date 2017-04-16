from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404

def HomeView(request):
    return render(request, "rein/home.html")
