"""
"""
from typing import Any, AnyStr, Dict, Union
from pathlib import Path
import logging
import decouple
import http.client as http_client
from getresponse_api_wrapper.validators import Validator


class Config:
    def __init__(
        self,
        config_path: Union[Any, Path] = None,
        supported: Dict[AnyStr, Any] = None,
    ):
        self._config = decouple.AutoConfig(search_path=config_path)
        self._config.SUPPORTED = supported or {".env": decouple.RepositoryEnv}

    @property
    def base_url(self):
        base_url = self._config("BASE_URL")
        if Validator.validate_url(base_url):
            return base_url
        raise ValueError("Invalid address provided.")

    @property
    def api_key(self):
        api_key = self._config("API_KEY")
        return api_key

    @property
    def is_enterprise(self):
        return self._config("ENTERPRISE", default=False, cast=bool)

    @property
    def debug(self):
        return self._config("DEBUG_REQUESTS", default=False, cast=bool)

    def setup_logging(self):
        if self.debug:
            http_client.HTTPConnection.debuglevel = 1
        logging.basicConfig()
        logging.getLogger("getresponse_api_wrapper").setLevel(logging.DEBUG)
