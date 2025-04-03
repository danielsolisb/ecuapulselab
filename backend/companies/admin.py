from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'twilio_phone_number', 'webhook_token', 'created_at']
    search_fields = ['name', 'twilio_phone_number']
    readonly_fields = ['webhook_token', 'created_at']
