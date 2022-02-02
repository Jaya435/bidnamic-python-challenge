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
