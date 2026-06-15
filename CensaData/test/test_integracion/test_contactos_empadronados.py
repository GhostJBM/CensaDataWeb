import pytest
from rest_framework.test import APIClient
from CensaData.models import (
    Cuentasinvestigadoresadmin,
    Empadronados,
    Contactosempadronados,
    Casas,   
    Infraestructuras,
    Tiposdepisos,
    Tiposdetechos,
    Materialesconstrucciones,
    Departamentos,
    Municipios,
    Barrios,
    Personas,
    Niveleseducativos,
    Relacionesparentescos,
    Empleos,
    Estadosciviles
)

pytestmark = pytest.mark.django_db


@pytest.fixture
def api_client():
    return APIClient()



@pytest.fixture
def admin_user(db):
    return Cuentasinvestigadoresadmin.objects.create_user(
        usuario='admin_empad',
        password='secreto',
        Correo='admin_empad@example.com',
        Role='ADMINISTRADOR',
        is_staff=1,
        is_superuser=1,
        is_active=1,
        estado=1,
    )


@pytest.fixture
def empadronadoCasa(db, admin_user):
    material = Materialesconstrucciones.objects.create(
    materialcontruccion='Concreto',
    estado=1
)

    techo = Tiposdetechos.objects.create(
    tipodetecho='Zinc',
    estado=1
)

    piso = Tiposdepisos.objects.create(
    tipopiso='Cerámica',
    estado=1
)

    infraestructura = Infraestructuras.objects.create(
    materialcontruccionid=material,
    tipodetechoid=techo,
    tipodepisoid=piso,
    estado=1
)
    departamento = Departamentos.objects.create(
        nombre='Depto Test',
        cantidadmunicipios=1,
        estado=1
    )

    municipio = Municipios.objects.create(
    nombre='Municipio Test',
    cantidadbarrios=1,
    estado=1,
    departamentoid=departamento
    )

    barrio = Barrios.objects.create(
        nombre='Barrio Test',
        cantidadcasas=1,
        municipioid=municipio,
        estado=1
    )
    casas = Casas.objects.create(
        numcasa=1212,
        cantidadhombres=1,
        cantidadmujeres=1,
        estado=1,
        infraestructuraid=infraestructura,
        barrioid=barrio,
        serviciodeagua=1,
        serviciodeenergia = 1,
        ingresofamiliar=0
        )

    return casas
@pytest.fixture
def empadronado(db, empadronadoCasa):

    persona = Personas.objects.create(
        primernombre='Ana',
        segundonombre='',
        primerapellido='Lopez',
        segundoapellido='',
        fechadenacimiento='1990-01-01',
        edad=30,
        sexo='F',
        estado=1
    )

    relacion = Relacionesparentescos.objects.create(
        relacion='Padre',
        estado=1
    )

    estadocivil = Estadosciviles.objects.create(
        estadocivil='Soltero',
        estado=1
    )

    empleo = Empleos.objects.create(
        empleo='Ninguno',
        estado=1
    )

    nivel = Niveleseducativos.objects.create(
        niveleducativo='Primaria',
        grado=1,
        estado=1
    )

    return Empadronados.objects.create(
        personaid=persona,
        relacionid=relacion,
        numerocedula='00000000000000',
        estadocivilid=estadocivil,
        empleoid=empleo,
        niveleducativoid=nivel,
        casaid=empadronadoCasa, 
        ingresopersonal=0,
        estado=1
    )

def test_create_contacto_empadronado_success(api_client,empadronado, admin_user):
    token_response = api_client.post(
        '/api/token/',
        {'Correo': 'admin_empad@example.com', 'password': 'secreto'},
        format='json',
    )

    access_token = token_response.data.get('access')
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    response = api_client.post(
        '/api/contactosEmpadronados/',
        {'contacto': 87654321, 'empadronadoid': empadronado.id},
        format='json',
    )

    assert response.status_code == 201
    assert response.data.get('message') == 'contacto creado con exito'
    assert Contactosempadronados.objects.filter(contacto=87654321).exists()


def test_create_contacto_empadronado_missing_body(api_client, admin_user):
    token_response = api_client.post(
        '/api/token/',
        {'Correo': 'admin_empad@example.com', 'password': 'secreto'},
        format='json',
    )

    access_token = token_response.data.get('access')
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    response = api_client.post(
        '/api/contactosEmpadronados/',
        {},
        format='json'
    )

    assert response.status_code == 204
    assert response.data.get('message') == 'No hay contenido'