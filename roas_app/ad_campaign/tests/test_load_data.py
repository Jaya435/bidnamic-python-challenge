from django.core.management import call_command


class TestLoadCampaignData:

    def test_load_campaign_data__all_data(self, get_all_campaigns):
        assert len(get_all_campaigns) == 20

    def test_load_campaign_data__CSV_already_loaded(self, db, campaign_filepath, capsys):
        msg = f"{campaign_filepath} is already saved in the ad_campaign_campaigns table.\n"
        call_command("load_data", campaign_filepath)
        out, _ = capsys.readouterr()
        assert out == msg


class TestLoadSearchTermsData:
    def test_load_search_terms__all_data(self, get_all_search_terms):
        assert len(get_all_search_terms) == 96

    def test_load_search_terms__CSV_already_loaded(self, db, campaign_filepath, search_terms_filepath, capsys):
        msg = f"Successfully inserted 96 rows into ad_campaign_searchterms table"
        call_command("load_data", campaign_filepath, "--search_terms", search_terms_filepath)
        out, _ = capsys.readouterr()
        assert msg in out
