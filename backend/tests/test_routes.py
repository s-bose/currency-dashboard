import pytest
from fastapi import FastAPI
from routes.router import router
from fastapi.testclient import TestClient

app = FastAPI()
app.include_router(router)
client = TestClient(app)

def test_endpoints(necessary_endpoints):
    endpoints = [route.path for route in router.routes]
    for necessary_endpoint in necessary_endpoints:
        assert necessary_endpoint in endpoints


def test_meta():
    response = client.get('/')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


