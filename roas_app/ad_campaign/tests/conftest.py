import pytest
import os
from ad_campaign.models import AdGroups, Campaigns, SearchTerms
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


@pytest.fixture(scope='session')
def ad_groups_filepath(test_directory):
    return os.path.join(test_directory, 'test_adgroups.csv')


@pytest.fixture(autouse=True, scope="session")
def load_data(django_db_setup, django_db_blocker, campaign_filepath, search_terms_filepath, ad_groups_filepath):
    with django_db_blocker.unblock():
        call_command("load_data", campaign_filepath,
                     "--search_terms", search_terms_filepath,
                     "--ad_groups", ad_groups_filepath)


@pytest.fixture
def get_all_campaigns(db) -> Campaigns:
    return Campaigns.objects.all()


@pytest.fixture
def get_all_search_terms(db) -> SearchTerms:
    return SearchTerms.objects.all()


@pytest.fixture
def get_all_ad_groups(db) -> AdGroups:
    return AdGroups.objects.all()
