import pytest
import os
from ad_campaign.models import Campaigns, SearchTerms
from django.core.management import call_command


@pytest.fixture(scope='session')
def test_directory():
    return os.path.abspath('test_data')


@pytest.fixture(scope='session')
def campaign_filepath(test_directory):
    return os.path.join(test_directory, 'test_campaigns.csv')


@pytest.fixture(scope='session')
def search_terms_filepath(test_directory):
    return os.path.join(test_directory, 'test_search_terms.csv')


@pytest.fixture(autouse=True, scope="session")
def load_campaign_data(django_db_setup, django_db_blocker, campaign_filepath):
    print(campaign_filepath)
    with django_db_blocker.unblock():
        call_command("load_data", campaign_filepath)


@pytest.fixture(autouse=True, scope="session")
def load_search_terms_data(django_db_setup, django_db_blocker, campaign_filepath, search_terms_filepath):
    with django_db_blocker.unblock():
        call_command("load_data", campaign_filepath, "--search_terms", search_terms_filepath)


@pytest.fixture
def get_all_campaigns(db) -> Campaigns:
    return Campaigns.objects.all()


@pytest.fixture
def get_all_search_terms(db) -> SearchTerms:
    return SearchTerms.objects.all()
