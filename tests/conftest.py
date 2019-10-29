"""Conftest plugin module for pytest
"""
import pytest


@pytest.fixture()
def fields():
    return [
        "countryCode",
        "industryTag",
        "firstName",
        "lastName",
        "companyName",
        "phone",
        "state",
        "city",
        "street",
        "zipCode",
        "numberOfEmployees",
        "timeFormat",
    ]


@pytest.fixture()
def data_fields():
    return [
        "firstName",
        "lastName",
        "companyName",
        "numberOfEmployees",
        "timeFormat",
        "Name",
    ]


@pytest.fixture()
def callback_sample(request):
    callback_data = {
        "url": "https://example.com/callback",
        "actions": {
            "open": request.param,
            "click": request.param,
            "goal": request.param,
            "subscribe": request.param,
            "unsubscribe": request.param,
            "survey": request.param
        }
    }
    return callback_data
