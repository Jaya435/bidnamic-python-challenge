from django.core.management import call_command
import os


class TestLoadCampaignData:

    def test_load_campaign_data__all_data(self, get_all_campaigns):
        assert len(get_all_campaigns) == 20

    def test_load_campaign_data__CSV_already_loaded(self, db, test_directory, capsys):
        file_path = os.path.join(test_directory, 'test_campaigns.csv')
        msg = f"{file_path} is already saved in the ad_campaign_campaigns table.\n"
        call_command("load_data", file_path)
        out, _ = capsys.readouterr()
        assert out == msg
