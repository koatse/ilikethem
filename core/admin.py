from django.contrib import admin

from .models import PropertyType
admin.site.register(PropertyType)

from .models_experience import RenovationExperience, TenantExperience, FinancingExperience, TaxExperience, InvestmentExperience
admin.site.register(RenovationExperience)
admin.site.register(TenantExperience)
admin.site.register(FinancingExperience)
admin.site.register(TaxExperience)
admin.site.register(InvestmentExperience)

from .models_geo import Country, Region, City
#admin.site.register(Country)
#admin.site.register(Region)
#admin.site.register(City)
