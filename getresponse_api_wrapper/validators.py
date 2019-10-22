import re


class Validator:
    """
    """

    @classmethod
    def validate_url(self, url=None):
        url_regex = re.compile(
            r"^(https?:\/\/"
            r"(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|"
            r"www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|"
            r"(http|https):\/\/localhost|"
            r"https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|"
            r"[a-zA-Z0-9]+\.[^\s]{2,})",
            re.IGNORECASE,
        )
        return re.match(url_regex, url) is not None
