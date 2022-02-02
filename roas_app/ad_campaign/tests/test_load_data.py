from django.core.management import call_command


class TestLoadCampaignData:
    def test_load_campaign_data__all_data(self, get_all_campaigns):
        assert len(get_all_campaigns) == 32

    def test_load_campaign_data__CSV_already_loaded(
        self, db, campaign_filepath, capsys
    ):
        msg = (
            f"{campaign_filepath} is already saved in the ad_campaign_campaign table.\n"
        )
        call_command("load_data", campaign_filepath)
        out, _ = capsys.readouterr()
        assert out == msg


class TestLoadSearchTermsData:
    def test_load_search_terms__all_data(self, get_all_search_terms):
        assert len(get_all_search_terms) == 96


class TestLoadAdGroupsData:
    def test_load_ad_groups__all_data(self, get_all_ad_groups):
        assert len(get_all_ad_groups) == 56
