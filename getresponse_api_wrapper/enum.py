import enum
from getresponse_api_wrapper.exceptions import (
    AuthenticationFailureException,
    BadAPIRequest,
    ReachedQuotaException,
)


class ErrorCodesEnum(enum.Enum):
    API_QUOTA_REACHED = ("API Quota Reached", 429, ReachedQuotaException)
    API_AUTH_ISSUE = (
        "API Authentication Issue",
        401,
        AuthenticationFailureException,
    )
    BAD_REQUEST = ("Bad Request", 400, BadAPIRequest)

    def __init__(self, message=None, code=None, exception_cls=None):
        self.message = message
        self.code = code
        self.exception_cls = exception_cls

    @property
    def error(self):
        return f"{self.code} - {self.message}"

    @classmethod
    def message_and_exception_for_code(cls, code):
        return [
            (item.message, item.exception_cls)
            for item in cls
            if item.code == code
        ][
            0
        ]  # TODO: should improve this(?).
