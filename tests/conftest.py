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
        "timeFormat"
    ]

@pytest.fixture()
def data_fields():
    return [
        "firstName",
        "lastName",
        "companyName",
        "numberOfEmployees",
        "timeFormat",
        "Name"
    ]