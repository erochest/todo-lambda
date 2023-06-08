
from todo_app import get_root


def test_get_root_returns_empty_list():
    """test that the get_root function returns an empty list"""
    assert get_root(None, None) == []