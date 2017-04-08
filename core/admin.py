from django.contrib import admin

from .models import PropertyType, UserProfile
admin.site.register(PropertyType)
admin.site.register(UserProfile)
