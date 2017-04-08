from django.contrib import admin

from .models import PropertyType
from .models_experience import RenovationExperience, TenantExperience, FinancingExperience, TaxExperience, InvestmentExperience

admin.site.register(PropertyType)

admin.site.register(RenovationExperience)
admin.site.register(TenantExperience)
admin.site.register(FinancingExperience)
admin.site.register(TaxExperience)
admin.site.register(InvestmentExperience)
