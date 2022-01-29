import pytest
import os
from ad_campaign.models import Campaigns
from django.core.management import call_command


@pytest.fixture(scope='session')
def test_directory():
    return os.path.abspath('ad_campaign/tests/test_data')


@pytest.fixture(autouse=True, scope="session")
def load_campaign_data(django_db_setup, django_db_blocker, test_directory):
    file_path = os.path.join(test_directory, 'test_campaigns.csv')
    with django_db_blocker.unblock():
        call_command("load_data", file_path)


@pytest.fixture
def get_all_campaigns(db) -> Campaigns:
    return Campaigns.objects.all()
