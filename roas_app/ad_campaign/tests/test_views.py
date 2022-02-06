import json

import pytest
from model_bakery import baker

pytestmark = pytest.mark.django_db


class TestUserViews:
    def test_user_viewset__success(self, client, admin_user):
        response = client.post(
            "/api-auth/login/", {"username": "admin", "password": "pass"}
        )
        assert response.status_code == 200
        assert admin_user.is_authenticated

    def test_user_viewset__unregistered_user(self, client):
        response = client.post(
            "/api-auth/login/", {"username": "unregistered_user", "password": "pass"}
        )
        err_msg = (
            "Please enter a correct username and password. "
            "Note that both fields may be case-sensitive."
        )
        assert response.status_code == 200
        assert err_msg in str(response.content)


class TestCampaignEndpoints:

    endpoint = "/api/campaigns/"

    def test_list(self, api_client):

        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert json.loads(response.content)["count"] == 32

    def test_create(self, api_client):
        data = {
            "campaign_id": 2578451596,
            "structure_value": "bbc 1",
            "status": "ENABLED",
        }
        response = api_client.post(self.endpoint, data=data, format="json")
        assert response.status_code == 201
        assert json.loads(response.content) == data

    def test_retrieve(self, api_client):
        campaign_id = 1578451596
        expected_json = {
            "campaign_id": campaign_id,
            "structure_value": "fox 40",
            "status": "ENABLED",
        }
        url = f"{self.endpoint}{campaign_id}/"

        response = api_client.get(url)

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json

    def test_update(self, api_client):
        data = {
            "campaign_id": 3578451596,
            "structure_value": "bbc 2",
            "status": "ENABLED",
        }
        url = f"{self.endpoint}{1578451596}/"

        response = api_client.put(path=url, data=data, format="json")

        assert response.status_code == 200
        assert json.loads(response.content) == data

    @pytest.mark.parametrize(
        "field",
        [
            ("campaign_id"),
            ("structure_value"),
            ("status"),
        ],
    )
    def test_partial_update(self, api_client, field):
        campaign_dict = {
            "campaign_id": 1578451596,
            "structure_value": "fox 40",
            "status": "ENABLED",
        }
        valid_field = campaign_dict[field]
        url = f"{self.endpoint}{campaign_dict['campaign_id']}/"

        response = api_client.patch(url, {field: valid_field}, format="json")

        assert response.status_code == 200
        assert json.loads(response.content)[field] == valid_field

    def test_delete(self, api_client, get_all_campaigns):
        url = f"{self.endpoint}{1578451596}/"

        response = api_client.delete(url)

        assert response.status_code == 204
        assert get_all_campaigns.count() == 31


class TestAdGroupEndpoints:

    endpoint = "/api/adgroups/"

    def test_list(self, api_client):

        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert json.loads(response.content)["count"] == 57

    def test_create(self, api_client):
        data = {
            "ad_group_id": 94481260174,
            "campaign_id": 1578451596,
            "alias": (
                "Shift - Shopping - GB - fox 40 - HIGH - "
                "vermont-oregon-oscar-uncle - 611936a2347d4da3b2fb4aabe8f8ff0a"
            ),
            "status": "ENABLED",
        }
        response = api_client.post(self.endpoint, data=data, format="json")
        assert response.status_code == 201
        assert json.loads(response.content) == data

    def test_retrieve(self, api_client):
        ad_group_id = 84481260174
        expected_json = {
            "ad_group_id": ad_group_id,
            "campaign_id": 1578451584,
            "alias": (
                "Shift - Shopping - GB - ellesse - HIGH - "
                "oscar-gee-princess-mexico - d77d4e4c99a4462991dd51ae0051e039"
            ),
            "status": "ENABLED",
        }
        url = f"{self.endpoint}{ad_group_id}/"

        response = api_client.get(url)

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json

    def test_update(self, api_client):
        data = {
            "ad_group_id": 84481260174,
            "campaign_id": 1578451596,
            "alias": (
                "Shift - Shopping - GB - fox 40 - HIGH - "
                "oscar-gee-princess-mexico - d77d4e4c99a4462991dd51ae0051e039"
            ),
            "status": "ENABLED",
        }
        url = f"{self.endpoint}{84481260174}/"

        response = api_client.put(path=url, data=data, format="json")

        assert response.status_code == 200
        assert json.loads(response.content) == data

    @pytest.mark.parametrize(
        "field",
        [
            ("ad_group_id"),
            ("campaign_id"),
            ("alias"),
            ("status"),
        ],
    )
    def test_partial_update(self, api_client, field):
        ad_group_dict = {
            "ad_group_id": 84481260174,
            "campaign_id": 1578451584,
            "alias": (
                "Shift - Shopping - GB - ellesse - HIGH - "
                "oscar-gee-princess-mexico - d77d4e4c99a4462991dd51ae0051e039"
            ),
            "status": "ENABLED",
        }
        valid_field = ad_group_dict[field]
        url = f"{self.endpoint}{ad_group_dict['ad_group_id']}/"

        response = api_client.patch(url, {field: valid_field}, format="json")

        assert response.status_code == 200
        assert json.loads(response.content)[field] == valid_field

    def test_delete(self, api_client, get_all_ad_groups):
        url = f"{self.endpoint}{84481260174}/"

        response = api_client.delete(url)

        assert response.status_code == 204
        assert get_all_ad_groups.count() == 56


class TestSearchTermEndpoints:

    endpoint = "/api/searchterms/"

    def test_list(self, api_client):

        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert json.loads(response.content)["count"] == 97

    def test_create(self, api_client):
        data = {
            "date": "2020-04-17",
            "ad_group_id": 84481260174,
            "campaign_id": 1578451584,
            "clicks": 1,
            "cost": 0.05,
            "conversion_value": 0.0,
            "conversions": 0,
            "search_term": "test_term",
            "roas": 0.0,
        }
        response = api_client.post(self.endpoint, data=data, format="json")
        assert response.status_code == 201
        assert json.loads(response.content) == data

    def test_retrieve(self, api_client):
        id = 1
        expected_json = {
            "date": "2020-04-16",
            "ad_group_id": 84481260174,
            "campaign_id": 1578451584,
            "clicks": 1,
            "cost": 0.05,
            "conversion_value": 0.0,
            "conversions": 0,
            "search_term": "camillaw",
            "roas": 0.0,
        }
        url = f"{self.endpoint}{id}/"

        response = api_client.get(url)

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json

    def test_update(self, api_client):
        data = {
            "date": "2020-04-16",
            "ad_group_id": 84481260174,
            "campaign_id": 1578451584,
            "clicks": 1,
            "cost": 0.05,
            "conversion_value": 0.0,
            "conversions": 0,
            "search_term": "test_search_term",
            "roas": 0.0,
        }
        url = f"{self.endpoint}{1}/"

        response = api_client.put(path=url, data=data, format="json")

        assert response.status_code == 200
        assert json.loads(response.content) == data

    @pytest.mark.parametrize(
        "field",
        [
            ("date"),
            ("ad_group_id"),
            ("campaign_id"),
            ("clicks"),
            ("cost"),
            ("conversion_value"),
            ("conversions"),
            ("search_term"),
            ("roas"),
        ],
    )
    def test_partial_update(self, api_client, field):
        search_term_dict = {
            "date": "2020-04-16",
            "ad_group_id": 84481260174,
            "campaign_id": 1578451584,
            "clicks": 1,
            "cost": 0.05,
            "conversion_value": 0.0,
            "conversions": 0,
            "search_term": "camillaw",
            "roas": 0.0,
        }
        valid_field = search_term_dict[field]
        url = f"{self.endpoint}{1}/"

        response = api_client.patch(url, {field: valid_field}, format="json")

        assert response.status_code == 200
        assert json.loads(response.content)[field] == valid_field

    def test_delete(self, api_client, get_all_search_terms):
        url = f"{self.endpoint}{1}/"

        response = api_client.delete(url)

        assert response.status_code == 204
        assert get_all_search_terms.count() == 96


class TestStructureValueEndPoints:
    endpoint = "/api/structure-value/ellesse/"

    def test_retrieve(self, api_client):
        campaign = baker.make(
            "Campaign", campaign_id=2578451584, structure_value="ellesse"
        )
        baker.make("SearchTerm", _quantity=8, campaign_id=campaign)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert json.loads(response.content)["count"] == 10

    def test_delete(self, api_client):
        url = f"{self.endpoint}"

        response = api_client.delete(url)

        assert response.status_code == 405


class TestAliasEndPoints:
    alias = (
        r"Shift - Shopping - GB - Converse - HIGH - "
        r"failed-five-cola-mockingbird - 7f9a1fbba2e14a4e95bb7375181f0c9b"
    )
    endpoint = f"/api/alias/{alias}/"

    def test_retrieve(self, api_client):
        campaign = baker.make(
            "Campaign", campaign_id=1578451386, structure_value="converse"
        )
        adgroup = baker.make(
            "AdGroup", ad_group_id=59624654596, campaign_id=campaign, alias=self.alias
        )
        baker.make("SearchTerm", _quantity=9, campaign_id=campaign, ad_group_id=adgroup)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert json.loads(response.content)["count"] == 10

    def test_delete(self, api_client):
        url = f"{self.endpoint}"

        response = api_client.delete(url)

        assert response.status_code == 405
