"""GetResponse client module
"""
from getresponse_api_wrapper.settings import Config
from getresponse_api_wrapper.request import Request
from getresponse_api_wrapper.resources.accounts import Accounts


class GetResponseClient:
    """GetResponseClient
    """

    def __init__(self, config: Config = Config()):
        self._config = config
        self.request = Request(self._config)

    def accounts(self):
        return Accounts(self.request)
