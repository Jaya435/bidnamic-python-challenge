from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import AdGroup, Campaign, SearchTerm


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class CampaignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campaign
        fields = ["campaign_id", "structure_value", "status"]


class AdGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdGroup
        fields = ["ad_group_id", "campaign_id", "alias", "status"]


class SearchTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchTerm
        fields = [
            "date",
            "ad_group_id",
            "campaign_id",
            "clicks",
            "cost",
            "conversion_value",
            "conversions",
            "search_term",
            "roas",
        ]


class AdGroupDetailSerializer(serializers.HyperlinkedModelSerializer):

    alias = serializers.CharField(source="ad_group_id.alias")

    class Meta:
        model = SearchTerm
        fields = [
            "date",
            "alias",
            "clicks",
            "cost",
            "conversion_value",
            "conversions",
            "search_term",
            "roas",
        ]


class CampaignDetailSerializer(serializers.ModelSerializer):

    structure_value = serializers.CharField(source="campaign_id.structure_value")

    class Meta:
        model = SearchTerm
        fields = [
            "date",
            "structure_value",
            "clicks",
            "cost",
            "conversion_value",
            "conversions",
            "search_term",
            "roas",
        ]
