import pytest
from getresponse_api_wrapper.settings import Config
from getresponse_api_wrapper.request import Request
from getresponse_api_wrapper import resources


class TestBaseResource:
    def setup(self):
        config = Config()
        request = Request(config)
        self.baseres = resources.BaseResource(request)

    def test_exists(self):
        assert hasattr(resources, "BaseResource")

    def test_can_instantiate(self):
        assert self.baseres is not None

    def test_has_request(self):
        assert hasattr(self.baseres, "request")

    def test_raise_without_request(self):
        with pytest.raises(ValueError):
            resources.BaseResource()
