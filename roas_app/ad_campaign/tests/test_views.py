def test_user_viewset(db, client):
    response = client.post(
        "/api-auth/login/", {"username": "admin", "password": "pass"}
    )
    assert response.status_code == 200
