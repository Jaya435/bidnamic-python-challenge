from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import AdGroup, Campaign, SearchTerm


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CampaignsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campaign
        fields = ["campaign_id", "structure_value", "status"]