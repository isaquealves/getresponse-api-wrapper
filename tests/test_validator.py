"""
"""
import inspect
import pytest
from getresponse_api_wrapper.validators import Validator


class TestValidator:
    def test_is_class(self):
        assert inspect.isclass(Validator)

    def test_has_url_validate_method(self):
        assert hasattr(Validator, "validate_url")

    def test_validate_url_is_callable(self):
        assert hasattr(Validator.validate_url, "__call__")

    @pytest.mark.parametrize(
        "url,expected_result",
        [
            ("test", False),
            ("https://localhost", True),
            ("http://localhost.local", True),
        ],
    )
    def test_validate_url(self, url, expected_result):
        assert Validator.validate_url(url) is expected_result
