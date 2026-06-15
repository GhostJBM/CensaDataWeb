import pytest
from rest_framework.test import APIClient

from CensaData.models import (
    Cuentasinvestigadoresadmin,
    Investigadores,
    Contactosinvestigadores,
    Administradores,

)

pytestmark = pytest.mark.django_db


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def admin_user(db):
    admin = Cuentasinvestigadoresadmin.objects.create_user(
        usuario='admin_contact',
        password='secreto',
        Correo='admin_contact@example.com',
        Role='ADMINISTRADOR',
        is_staff=1,
        is_superuser=1,
        is_active=1,
        estado=1,
    )

    return Administradores.objects.create(
        primernombre='Ivan',
        segundonombre='',
        primerapellido='Perez',
        segundoapellido='',
        edad=30,
        sexo='M',
        estado=1,
        cuentaid=admin,
    )   
@pytest.fixture
def investigador(db, admin_user):
    inves_user = Cuentasinvestigadoresadmin.objects.create_user(
        usuario='invest_contact',
        password='secreto',
        Correo='invest_contact@example.com',
        Role='INVESTIGADOR',
        is_staff=1,
        is_superuser=1,
        is_active=1,
        estado=1,
    )
    return Investigadores.objects.create(
        primernombre='Ivan',
        segundonombre='',
        primerapellido='Perez',
        segundoapellido='',
        edad=30,
        sexo='M',
        estado=1,
        cuentaid=inves_user,
        administradorid=admin_user,
    )


def test_create_contacto_investigador_success(api_client, investigador, admin_user):
    token_response = api_client.post(
        '/api/token/',
        {'Correo': 'admin_contact@example.com', 'password': 'secreto'},
        format='json',
    )

    access_token = token_response.data.get('access')
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    response = api_client.post(
        '/api/contactosInvestigadores/',
        {'contacto': 12345678, 'investigadorid': investigador.id},
        format='json',
    )

    assert response.status_code == 201
    assert response.data.get('message') == 'Contacto creado con exito'
    assert Contactosinvestigadores.objects.filter(contacto=12345678).exists()


def test_create_contacto_investigador_missing_body(api_client, admin_user):
    token_response = api_client.post(
        '/api/token/',
        {'Correo': 'admin_contact@example.com', 'password': 'secreto'},
        format='json',
    )

    access_token = token_response.data.get('access')
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    response = api_client.post(
        '/api/contactosInvestigadores/',
        {},
        format='json'
    )

    assert response.status_code == 204
    assert response.data.get('message') == 'No hay contenido'