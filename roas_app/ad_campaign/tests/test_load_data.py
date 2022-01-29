class TestLoadCampaignData:

    def test_load_campaign_data__all_data(self, get_all_campaigns):
        assert 20 == len(get_all_campaigns)
