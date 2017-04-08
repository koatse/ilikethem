from django.contrib import admin

from .models import PropertyType, Role, UserProfile
admin.site.register(PropertyType)
admin.site.register(Role)
admin.site.register(UserProfile)
