import json

import pytest

pytestmark = pytest.mark.django_db


class TestUserViews:
    def test_user_viewset__success(self, client, create_admin_user):
        response = client.post(
            "/api-auth/login/", {"username": "admin", "password": "pass"}
        )
        assert response.status_code == 200
        assert create_admin_user.is_authenticated

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


class TestCampaignViews:

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
