from fastapi.testclient import TestClient

from centralserver import app

client = TestClient(app)


def test_healthcheck() -> None:
    """Check if healthcheck endpoint is reachable."""

    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"message": "Healthy"}
