
from chalice.test import Client
from app import app


def test_get_root_successfully_returns_empty_list():
    """test that the get_root function returns an empty list"""
    with Client(app) as client:
        response = client.http.get('/')
        assert response.status_code == 200
        assert response.json_body == []