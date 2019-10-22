"""Exception
"""
import datetime
import json


class ReachedQuotaException(Exception):
    """Raise when reaching getresponse API requests quota per timeframe
    """

    def __init__(self, message: str = None, **kwargs):
        self.timeframe_stop = datetime.datetime.now()
        self.time_to_reset = kwargs.get("time_to_reset", 100)
        self.nextframe = self.timeframe_stop + datetime.timedelta(
            seconds=self.time_to_reset
        )
        self.message = (
            f"{message} at {self.timeframe_stop} until {self.nextframe}"
        )


class AuthenticationFailureException(Exception):
    """Raise when authentication didn't succeed
    """

    def __init__(self, message: str = None, **kwargs):
        self.auth_type = kwargs.get("auth_type", "api_key")
        self.message = f"{message} with {self.auth_type} auth type"


class BadAPIRequest(Exception):
    """Raise when submitting an invalid request parameter
    """

    def __init__(self, message: str = None, **kwargs):
        self.request_params = kwargs.get("request_params", {})
        self.message = (
            f"{message} with params {json.dumps(self.request_params)}"
        )
