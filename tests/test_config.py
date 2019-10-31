"""
"""
import os
import logging
from pathlib import Path
import inspect
import pytest
import decouple
from getresponse_api_wrapper.settings import Config


class TestConfig:
    def setup(self):
        supported = {"env.circleci": decouple.RepositoryEnv}
        self.configobj = Config(supported=supported)

    def test_is_class(self):
        assert inspect.isclass(Config), "Config is anything but a class"

    def test_is_instantiable(self):
        assert self.configobj is not None, "Config cannot be instantiated"

    def test_raise_invalid_base_url(self):
        os.environ["BASE_URL"] = "something"
        config = Config()
        with pytest.raises(ValueError):
            config.base_url
        del os.environ["BASE_URL"]

    def test_raise_no_base_url(self):
        BASE_URL = os.environ.pop(
            "BASE_URL",
            "https://localhost"
        )
        path = Path(__file__).parent
        config = Config(path)
        with pytest.raises(decouple.UndefinedValueError):
            config.base_url
        os.environ["BASE_URL"] = BASE_URL

    def test_raise_no_api_key(self):
        APIKEY = os.environ.pop(
            "API_KEY",
            "oSQMBAmyfHrQrHBBfZEnDOlvsCJpaaVF"
        )
        path = Path(__file__).parent
        config = Config(path)
        with pytest.raises(decouple.UndefinedValueError):
            config.api_key
        os.environ["API_KEY"] = APIKEY

    def test_is_not_enterprise(self):
        assert self.configobj.is_enterprise is False

    def test_is_enterprise(self):
        os.environ["ENTERPRISE"] = "true"
        config = Config()
        assert config.is_enterprise is True

    def test_debug(self):
        assert self.configobj.debug is False

    def test_setup_logging(self):
        os.environ["DEBUG_REQUESTS"] = "true"
        config = Config()
        config.setup_logging()
        assert (
            logging.getLevelName(
                logging.getLogger("getresponse_api_wrapper").level
            )
            == "DEBUG"
        )
