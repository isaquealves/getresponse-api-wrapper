"""Collection of request hooks useful for supplement responses behavior
"""
from getresponse_api_wrapper.enum import ErrorCodesEnum


def check_response_errors(response, *args, **kwargs):
    """Hook to raise the expected exception in failure cases
    """
    resp = response.json()
    if resp.get("httpStatus") in [400, 401, 429]:
        msg, exception = ErrorCodesEnum.message_and_exception_for_code(
            code=resp.get("httpStatus")
        )
        raise exception(message=msg)
    response.status_code = resp.get("httpStatus")
    return response.raise_for_status()
