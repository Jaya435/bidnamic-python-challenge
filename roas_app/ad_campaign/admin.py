from django.contrib import admin

from .models import AdGroups, Campaigns, SearchTerms


@admin.register(Campaigns)
class campaignsAdmin(admin.ModelAdmin):
    list_display = ["campaign_id", "structure_value", "status"]
