from utils import append_slash
import pytest


@pytest.mark.parametrize("base_url, expected", [
    ("https://ahahahah.ru", "https://ahahahah.ru/"),
    ("https://mmm.ru/", "https://mmm.ru/")
])
def test_append_slash(base_url, expected):
    assert append_slash(base_url) == expected
