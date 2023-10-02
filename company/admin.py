# company/admin.py

from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', )
    list_filter = ('admins',)

admin.site.register(Company, CompanyAdmin)
