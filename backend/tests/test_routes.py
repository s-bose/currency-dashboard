import pytest
from fastapi import FastAPI
from models.response import meta
from routes.router import router
from fastapi.testclient import TestClient

app = FastAPI()
app.include_router(router)
client = TestClient(app)


def test_endpoints(necessary_endpoints):
    endpoints = [route.path for route in router.routes]
    for necessary_endpoint in necessary_endpoints:
        assert necessary_endpoint in endpoints


def test_index():
    response = client.get('/')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_meta():
    response = client.get('/meta')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert meta.Meta(**response.json())


@pytest.mark.parametrize('day,status', [
    ('', 404),
    (2, 400),
    (7, 200),
    (15, 400),
    (17, 400),
    (30, 200)
])
def test_get_forecast_for_next_n_days(day, status):
    response = client.get(f'/forecast/next/days/{day}')
    assert response.status_code == status
    assert isinstance(response.json(), dict)
