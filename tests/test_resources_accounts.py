import json
from unittest import mock
import inspect
import pytest
import requests
from _pytest.monkeypatch import MonkeyPatch
from getresponse_api_wrapper.settings import Config
from getresponse_api_wrapper.request import Request
from getresponse_api_wrapper.resources import BaseResource
from getresponse_api_wrapper.resources import accounts


class TestAccounts:

    monkeypatch = MonkeyPatch()

    def setup(self):
        self.config = Config()
        self.request = Request(self.config)
        self.accounts = accounts.Accounts(self.request)
        self.mock_get = mock.MagicMock()
        self.mock_post = mock.MagicMock()
        self.mock_delete = mock.MagicMock()
        self.monkeypatch.setattr("requests.Session.get", self.mock_get)
        self.monkeypatch.setattr("requests.Session.post", self.mock_post)
        self.monkeypatch.setattr("requests.Session.delete", self.mock_delete)

    @classmethod
    def teardown_class(cls):
        cls.monkeypatch.undo()

    def test_class_tree(self):
        assert issubclass(accounts.Accounts, BaseResource)

    def test_has_get_blacklists(self):
        assert hasattr(self.accounts, "get_blacklists")

    def test_get_blacklist(self):

        self.accounts.get_blacklists()
        self.mock_get.assert_called()

    def test_has_update_blacklists(self):
        assert hasattr(self.accounts, "update_blacklists")

    def test_update_blacklist(self):
        data = {
            "masks": [
                "test@example.com",
                "quest@example.com",
                "user@localhost"
            ]
        }
        self.accounts.update_blacklists(data=data)
        self.mock_post.assert_called()

    def test_update_blacklist_raise_without_data(self):
        with pytest.raises(ValueError):
            self.accounts.update_blacklists()

    def test_has_get_account_info(self):
        assert hasattr(self.accounts, "get_account_info")

    def test_get_account_info(self):
        self.accounts.get_account_info()
        self.mock_get.assert_called()

    def test_has_update_account_info(self):
        assert hasattr(self.accounts, "update_account_info")

    def test_update_account_info(self):
        update_data = {
            "firstName": "Test"
        }
        self.accounts.update_account_info(data=update_data)
        self.mock_post.assert_called()

    @pytest.mark.parametrize("data,exc", [
        ({}, ValueError),
        ({'name': 'Name'}, KeyError)
    ])
    def test_update_account_info_raise_with_invalid_data(self, data, exc):
        with pytest.raises(exc):
            self.accounts.update_account_info(data=data)

    def test_get_full_billing_information_called_with(self):
        self.accounts.get_billing_info()
        self.mock_get.assert_called_with(
            url=f"{self.config.base_url}/accounts/billing",
            params={'fields': None}
        )

    def test_get_billing_info_accept_params(self):
        get_billing = inspect.getfullargspec(self.accounts.get_billing_info)
        assert 'fields' in get_billing.args

    def test_get_callbacks(self):
        self.accounts.get_callbacks()
        self.mock_get.assert_called_once_with(
            url=f"{self.config.base_url}/accounts/callbacks"
        )

    @pytest.mark.parametrize("callback_sample", [
        True,
        False
    ], indirect=["callback_sample"])
    @pytest.mark.usefixtures("callback_sample")
    def test_set_callbacks(self, callback_sample):
        self.accounts.set_callbacks(data=callback_sample)
        self.mock_post.assert_called_with("/accounts/callbacks", data=json.dumps(callback_sample))

    def test_delete_callbacks(self):
        self.accounts.delete_callbacks()
        self.mock_delete.assert_called_once()