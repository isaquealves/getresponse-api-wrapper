from unittest import mock
from _pytest.monkeypatch import MonkeyPatch
from getresponse_api_wrapper.settings import Config
from getresponse_api_wrapper.request import Request
from getresponse_api_wrapper.resources import BaseResource
from getresponse_api_wrapper.resources import multimedia


class TestMultimedia:

    monkeypatch = MonkeyPatch()

    def setup(self):
        config = Config()
        request = Request(config)
        self.media = multimedia.Multimedia(request)
        self.mock_get = mock.MagicMock()
        self.mock_post = mock.MagicMock()
        self.monkeypatch.setattr("requests.Session.get", self.mock_get)
        self.monkeypatch.setattr("requests.Session.post", self.mock_post)

    @classmethod
    def teardown_class(cls):
        cls.monkeypatch.undo()

    def test_class_tree(self):
        assert issubclass(multimedia.Multimedia, BaseResource)

    def test_has_get_images_member(self):
        assert hasattr(self.media, "get_images")

    def test_get_images(self):
        fields = [],
        results = 10,
        page = 1
        self.media.get_images(fields, results, page)
        self.mock_get.assert_called_once()
