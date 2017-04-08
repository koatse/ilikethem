from django.contrib import admin

#from .models import RecommendedContact, Recommendation
#admin.site.register(RecommendedContact)

from .models import Recommendation
admin.site.register(Recommendation)
