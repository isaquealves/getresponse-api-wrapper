from unittest import mock
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
        config = Config()
        request = Request(config)
        self.accounts = accounts.Accounts(request)
        self.mock_get = mock.MagicMock()
        self.mock_post = mock.MagicMock()
        self.monkeypatch.setattr("requests.Session.get", self.mock_get)
        self.monkeypatch.setattr("requests.Session.post", self.mock_post)

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

