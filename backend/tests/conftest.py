# Pytest fixtures

import pytest


@pytest.fixture
def necessary_endpoints():
    return [
        "/",
        "/meta",
        "/currencies",
        "/convert/",
        "/convert",
        "/forecast/today",
        "/forecast/tomorrow",
        "/forecast/next/days/{days}",
        "/forecast",
        "/exchange_rate/currency",
        "/exchange_rate/currency"
    ]
