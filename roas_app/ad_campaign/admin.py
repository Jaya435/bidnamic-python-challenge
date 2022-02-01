from django.contrib import admin

from .models import AdGroup, Campaign, SearchTerm


@admin.register(Campaign)
class campaignsAdmin(admin.ModelAdmin):
    list_display = ["campaign_id", "structure_value", "status"]


@admin.register(AdGroup)
class adGroupsAdmin(admin.ModelAdmin):
    list_display = ["ad_group_id", "related_campaign", "alias", "status"]

    def related_campaign(self, obj):
        return obj.campaign_id.structure_value

    related_campaign.short_description = 'Campaign'


@admin.register(SearchTerm)
class searchTermsAdmin(admin.ModelAdmin):
    list_display = ["date", "ad_group_id", "related_campaign", "clicks", "cost",
                    "conversion_value", "conversions", "search_term"]

    def related_campaign(self, obj):
        return obj.campaign_id.structure_value

    related_campaign.short_description = 'Campaign'
