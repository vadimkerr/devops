from fastapi.testclient import TestClient
from freezegun import freeze_time
from server.main import app

client = TestClient(app)


@freeze_time("2021-08-27T14:26:35.798658")
def test_get_current_time():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == "2021-08-27 17:26:35.798658+03:00"
