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
