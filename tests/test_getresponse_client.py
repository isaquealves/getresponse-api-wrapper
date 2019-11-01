import inspect
import pytest
from tests.helper import not_raises
from getresponse_api_wrapper.client import GetResponseClient


class TestGetResponseClient:
    def setup(self):
        self.client = GetResponseClient()

    def test_is_class(self):
        assert inspect.isclass(GetResponseClient)

    def test_can_instantiate(self):
        client = GetResponseClient()
        assert client is not None

    def test_need_config(self):
        client_init = inspect.getfullargspec(GetResponseClient.__init__)
        assert "config" in client_init.args

    def test_has_accounts(self):
        assert hasattr(GetResponseClient, "accounts")
