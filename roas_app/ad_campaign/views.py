from django.contrib.auth.models import Group, User
from rest_framework import filters, generics, permissions, viewsets

from .models import AdGroup, Campaign, SearchTerm
from .serializers import (
    AdGroupDetailSerializer,
    AdGroupSerializer,
    CampaignDetailSerializer,
    CampaignSerializer,
    GroupSerializer,
    SearchTermSerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CampaignViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows campaigns to be viewed or edited.
    """

    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [permissions.IsAuthenticated]


class AdGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ad groups to be viewed or edited.
    """

    queryset = AdGroup.objects.all()
    serializer_class = AdGroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class SearchTermViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows search terms to be viewed or edited.
    """

    queryset = SearchTerm.objects.all()
    serializer_class = SearchTermSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["date", "conversion_value", "cost", "roas"]
    order_by = ["roas"]
    search_fields = ["campaign_id__campaign_id", "ad_group_id__ad_group_id"]


class AdGroupDetailView(generics.ListAPIView):
    queryset = SearchTerm.objects.all()
    serializer_class = AdGroupDetailSerializer

    def get_ad_groups(self):
        return AdGroup.objects.filter(alias=self.kwargs["alias"])

    def get_queryset(self):
        ad_group = self.get_ad_groups()
        return self.queryset.order_by("-roas").filter(ad_group_id__in=ad_group)[:10]


class CampaignDetailView(generics.ListAPIView):
    queryset = SearchTerm.objects.all()
    serializer_class = CampaignDetailSerializer

    def get_campaigns(self):
        return Campaign.objects.filter(structure_value=self.kwargs["structure_value"])

    def get_queryset(self):
        campaign = self.get_campaigns()
        return self.queryset.order_by("-roas").filter(campaign_id__in=campaign)[:10]
