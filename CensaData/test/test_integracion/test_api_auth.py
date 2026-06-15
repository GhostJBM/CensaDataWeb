import pytest
from rest_framework.test import APIClient
from CensaData.models import Cuentasinvestigadoresadmin

pytestmark = pytest.mark.django_db


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def admin_user(db):
    return Cuentasinvestigadoresadmin.objects.create_user(
        usuario='juan_auth',
        password='secreto',
        Correo='juan_auth@example.com',
        Role='ADMINISTRADOR',
        is_staff=1,
        is_superuser=1,
        is_active=1,
        estado=1,
    )


def test_token_endpoint_returns_access_and_refresh_tokens(api_client, admin_user):
    response = api_client.post(
        '/api/token/',
        {'Correo': 'juan_auth@example.com', 'password': 'secreto'},
        format='json',
    )

    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data


def test_me_endpoint_returns_authenticated_user_profile(api_client, admin_user):
    token_response = api_client.post(
        '/api/token/',
        {'Correo': 'juan_auth@example.com', 'password': 'secreto'},
        format='json',
    )

    access_token = token_response.data.get('access')

    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
    response = api_client.get('/me/')

    assert response.status_code == 200
    assert response.data.get('email') == 'juan_auth@example.com'
    assert response.data.get('role') == 'ADMINISTRADOR'


def test_token_endpoint_rejects_invalid_password(api_client, admin_user):
    response = api_client.post(
        '/api/token/',
        {'Correo': 'juan_auth@example.com', 'password': 'wrongpass'},
        format='json',
    )

    assert response.status_code == 401
    assert 'detail' in response.data