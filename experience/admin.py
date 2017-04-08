from django.contrib import admin

from experience.models import RenovationExperience, TenantExperience, FinancingExperience, TaxExperience
admin.site.register(RenovationExperience)
admin.site.register(TenantExperience)
admin.site.register(FinancingExperience)
admin.site.register(TaxExperience)
