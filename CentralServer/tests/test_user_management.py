from typing import Any

from fastapi.testclient import TestClient

from centralserver import app

client = TestClient(app)


def test_create_user_success():
    """Test creating a user successfully."""

    data: dict[str, Any] = {
        "username": "testuser",
        "roleId": 2,
        "password": "password123",
    }

    response = client.post(
        "/auth/create",
        json=data,
    )
    assert response.status_code == 201
    resp_data: dict[str, Any] = response.json()
    assert type(resp_data["id"]) is str
    assert resp_data["username"] == data["username"]
    assert resp_data["email"] is None
    assert resp_data["nameFirst"] is None
    assert resp_data["nameMiddle"] is None
    assert resp_data["nameLast"] is None
    assert resp_data["avatarUrl"] is None
    assert resp_data["schoolId"] is None
    assert resp_data["roleId"] == data["roleId"]
    assert resp_data["deactivated"] is False


def test_create_user_missing_required_field():
    """Test creating a user with a missing required field."""

    data: dict[str, Any] = {
        "username": "testuser3",
        "password": "password123",
    }
    response = client.post(
        "/auth/create",
        json=data,
    )
    assert response.status_code == 422
    resp_data = response.json()
    assert resp_data["detail"][0]["type"] == "missing"
    assert "roleId" in resp_data["detail"][0]["loc"]
    assert resp_data["detail"][0]["msg"] == "Field required"


def test_create_user_missing_username():
    """Test creating a user with a missing username."""

    response = client.post(
        "/auth/create",
        json={
            "roleId": 2,
            "password": "password123",
        },
    )
    assert response.status_code == 422
    assert "username" in response.json()["detail"][0]["loc"]


def test_create_user_short_username():
    response = client.post(
        "/auth/create",
        json={
            "username": "ab",
            "roleId": 2,
            "password": "password123",
        },
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid username"


def test_create_user_invalid_data_types():
    """Test creating a user with invalid data types."""

    response = client.post(
        "/auth/create",
        json={
            "username": 12345,
            "roleId": 2,
            "password": "password123",
        },
    )
    assert response.status_code == 422
    assert "username" in response.json()["detail"][0]["loc"]
