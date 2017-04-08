from django.contrib import admin

from .models import RecommendedContact, Recommendation
admin.site.register(RecommendedContact)
admin.site.register(Recommendation)
