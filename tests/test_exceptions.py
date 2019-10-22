import pytest
from getresponse_api_wrapper import exceptions


class TestExceptions:
    def test_is_subclass(self):
        assert issubclass(exceptions.ReachedQuotaException, Exception)

    def test_reached_quota_can_be_raised(self):
        with pytest.raises(exceptions.ReachedQuotaException) as exc:
            raise exceptions.ReachedQuotaException(
                message="Quota exception raised"
            )

    def test_authentication_failure_can_be_raised(self):
        with pytest.raises(exceptions.AuthenticationFailureException):
            raise exceptions.AuthenticationFailureException(
                message="Authentication Failed"
            )

    def test_bad_request_can_be_raised(self):
        with pytest.raises(exceptions.BadAPIRequest):
            raise exceptions.BadAPIRequest(
                message="Bad Request",
                request_params={"name": "test"}
            )
