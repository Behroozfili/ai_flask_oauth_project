import pytest
import unittest.mock
from app.main import create_app


@pytest.fixture(scope='module')
def app():
    _app = create_app()
    test_config = {
        "TESTING": True,
        "SECRET_KEY": "testing_secret_key",
        "SERVER_NAME": "localhost.test"
    }
    _app.config.update(test_config)
    yield _app


@pytest.fixture(scope='module')
def client(app):
    return app.test_client()


def test_secret_key(app):
    with app.app_context():
        assert app.config['SECRET_KEY'] == "testing_secret_key"
        assert app.secret_key is not None


def test_root(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"message" in response.data


def test_login(client):
    response = client.get('/login')
    assert response.status_code == 302
    assert "accounts.google.com" in response.location


def test_auth(app, client):
    mock_token_response = {
        'access_token': 'fake-access-token',
        'id_token': 'fake-id-token',
        'userinfo': {'sub': '123', 'name': 'Test User'}
    }
    mock_user_info = {
        'sub': '12345',
        'name': 'Test User',
        'email': 'test@example.com'
    }

    # Simulate OAuth callback
    with app.app_context():
        with unittest.mock.patch(
            'app.routes.current_app.google_oauth.authorize_access_token',
            return_value=mock_token_response
        ) as mock_authorize, unittest.mock.patch(
            'app.routes.current_app.google_oauth.parse_id_token',
            return_value=mock_user_info
        ) as mock_parse:
            response = client.get('/auth')

    assert response.status_code == 302

    # After authentication, expect redirect to /analyze
    assert response.location.endswith('/analyze')

    mock_authorize.assert_called_once()
    mock_parse.assert_called_once_with(mock_token_response)
