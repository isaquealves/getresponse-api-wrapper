from getresponse_api_wrapper.request import Request


class BaseResource:
    def __init__(self, request: Request = None):
        if not request:
            raise ValueError("Request should be configured for resources")
        self.request = request
