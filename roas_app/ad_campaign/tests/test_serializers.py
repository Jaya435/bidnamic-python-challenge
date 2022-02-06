import pytest
from ad_campaign.serializers import AdGroupSerializer

pytestmark = pytest.mark.django_db


class TestAdGroupSerializer:
    def test_serialize_model(self, get_all_ad_groups):
        ad_group = get_all_ad_groups[0]
        serializer = AdGroupSerializer(ad_group)

        assert serializer.data

    def test_serialized_data(self):
        data = {
            "ad_group_id": 94481260174,
            "campaign_id": 1578451596,
            "alias": (
                "Shift - Shopping - GB - fox 40 - HIGH - "
                "vermont-oregon-oscar-uncle - 611936a2347d4da3b2fb4aabe8f8ff0a"
            ),
            "status": "ENABLED",
        }
        serializer = AdGroupSerializer(data=data)
        assert serializer.is_valid()
        assert serializer.errors == {}
