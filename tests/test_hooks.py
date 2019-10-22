import pytest
from unittest import mock
import requests
from _pytest.monkeypatch import MonkeyPatch
from getresponse_api_wrapper import hooks
from getresponse_api_wrapper import exceptions


class TestHooks:

    monkeypatch = MonkeyPatch()

    @classmethod
    def teardown_class(cls):
        mock.patch.stopall()

    @pytest.mark.parametrize(
        "status_code,raise_for_status",
        [
            (400, exceptions.BadAPIRequest),
            (401, exceptions.AuthenticationFailureException),
            (429, exceptions.ReachedQuotaException),
            (500, requests.exceptions.HTTPError)
        ],
    )
    @mock.patch.object(requests.adapters.HTTPAdapter, "send")
    @mock.patch.object(requests.Session, "resolve_redirects")
    def test_check_response_errors(
        self, resolve_redirs, mock_send, status_code, raise_for_status
    ):
        url = "https://localhost"
        # TODO: Refactor and improve
        mock_response = mock.MagicMock()
        mock_response.json = mock.Mock(return_value={"httpStatus": status_code})
        mock_send.return_value = mock_response
        resolve_redirs.return_value = []
        mock_response.status_code = status_code
        mock_response.raise_for_status = mock.Mock(return_value=mock.MagicMock())
        mock_response.is_redirect.return_value = False
        session = requests.Session()
        session.headers.update(
            {
                "X-Auth-Token": f"api-key jysc768rglopo9revd4jtibeqd3vz0q2",
                "Content-Type": "application/json",
            }
        )
        session.hooks = {"response": hooks.check_response_errors}
        if status_code in [400, 401, 429]:
            with pytest.raises(raise_for_status):
                session.get(url)
        else:
            session.get(url)
            mock_response.raise_for_status.assert_called()
