from django.shortcuts import render, redirect

def HomeView(request):
    return render(request, "rein/home.html")

