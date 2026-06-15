import pytest
from rest_framework.test import APIClient
from datetime import datetime, timedelta

from CensaData.models import (
    Cuentasinvestigadoresadmin,
    Investigadores,
    Barrios,
    Departamentos,
    Infraestructuras,
    Censos,
    Relacionesparentescos,
    Empleos,
    Estadosciviles,
    Niveleseducativos,
    Encuestasinidetrabajadores,
    Administradores,
    Municipios,
    Tiposdepisos,
    Tiposdetechos,
    Materialesconstrucciones
)
from CensaData.services import EncuestaInideService

pytestmark = pytest.mark.django_db


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def admin_user(db):
    return Cuentasinvestigadoresadmin.objects.create_user(
        usuario='admin_inide_api',
        password='secreto',
        Correo='admin_inide_api@example.com',
        Role='ADMINISTRADOR',
        is_staff=1,
        is_superuser=1,
        is_active=1,
        estado=1,
    )


@pytest.fixture
def encuesta_setup(db):
    admin_user_obj = Cuentasinvestigadoresadmin.objects.create_user(
        usuario='admin_inide',
        password='secreto',
        Correo='admin_inide@example.com',
        Role='ADMINISTRADOR',
        is_staff=1,
        is_superuser=1,
        is_active=1,
        estado=1,
    )

    user_inves = Cuentasinvestigadoresadmin.objects.create_user(
        usuario='admitn_contact',
        password='secreto',
        Correo='adm7_contact@example.com',
        Role='INVESTIGADOR',
        is_staff=1,
        is_superuser=0,
        is_active=1,
        estado=1,
    )

    admin = Administradores.objects.create(
        primernombre='Ivan',
        segundonombre='',
        primerapellido='Perez',
        segundoapellido='',
        edad=30,
        sexo='M',
        estado=1,
        cuentaid=admin_user_obj,
    )
    investigador = Investigadores.objects.create(
        primernombre='Ivan',
        segundonombre='',
        primerapellido='Perez',
        segundoapellido='',
        edad=30,
        sexo='M',
        estado=1,
        cuentaid=user_inves,
        administradorid=admin,
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

    censo = Censos.objects.create(
        nombrecenso='Censo Test',
        cantidadencuestados=0,
        cantidadrespuestaspositivas=0,
        cantidadrespuestasnegativas=0,
        cantidadencuestas=0,
        muestrapoblacional=100,
        poblaciontotal=1000,
        cantidadcasasencuestadas=0,
        fechainiciocenso=datetime.now(),
        fechafincenso=datetime.now() + timedelta(days=30),
        estado=1,
    )

    relacion = Relacionesparentescos.objects.create(relacion='Padre', estado=1)
    empleo = Empleos.objects.create(empleo='Ninguno', estado=1)
    estadocivil = Estadosciviles.objects.create(estadocivil='Soltero', estado=1)
    nivel = Niveleseducativos.objects.create(niveleducativo='Primaria', grado=1, estado=1)

    return {
        'user': user_inves,
        'investigador': investigador,
        'barrio': barrio,
        'infraestructura': infraestructura,
        'censo': censo,
        'relacion': relacion,
        'empleo': empleo,
        'estadocivil': estadocivil,
        'nivel': nivel,
    }


def test_encuestas_list_and_create_inaccessible(api_client, encuesta_setup, admin_user):
    # create an encuesta via service so list has data
    service = EncuestaInideService()
    future_date = (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
    final_date = (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')

    payload = {
        'Casa': {
            'numcasa': 112522,
            'barrioid': encuesta_setup['barrio'].id,
            'infraestructuraid': encuesta_setup['infraestructura'].id,
            'serviciodeagua': 1,
            'serviciodeenergia': 0,
            'cantidadhombres':0,
            'cantidadmujeres':0
        },
        'encuestainide': {
            'censoid': encuesta_setup['censo'].id,
            'fechainicio': future_date,
            'fechafin': final_date,
            'respuesta': 'POSITIVA',
        },
        'personas': {
            'p1': {
                'primernombre': 'Ana',
                'segundonombre': '',
                'primerapellido': 'Lopez',
                'segundoapellido': '',
                'fechanacimiento': '1990-01-01',
                'sexo': 'F',
            }
        },
        'empadronados': {
            'e1': {
                'relacionid': encuesta_setup['relacion'].id,
                'empleoid': encuesta_setup['empleo'].id,
                'estadocivilid': encuesta_setup['estadocivil'].id,
                'niveleducativoid': encuesta_setup['nivel'].id,
                'numerocedula': '00000000000000',
                'ingresopersonal': 0,
            }
        }
    }

    service.CrearEncuesta(payload, encuesta_setup['user'])

    # list endpoint
    token_response = api_client.post(
        '/api/token/',
        {'Correo': 'admin_inide_api@example.com', 'password': 'secreto'},
        format='json',
    )
    # if token endpoint fails, proceed without auth for list
    access_token = token_response.data.get('access') if token_response.status_code == 200 else None
    if access_token:
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    response = api_client.get('/api/encuestasIniDeTrabajadores/')
    assert response.status_code == 200
    assert 'data' in response.data

    # create should be inaccessible from this endpoint
    post_response = api_client.post('/api/encuestasIniDeTrabajadores/', payload, format='json')
    assert post_response.status_code == 400
    assert 'El metodo es inaccesible' in str(post_response.data)


def test_censo_completo_and_encuesta_completa_empty_body(api_client, admin_user):
    token_response = api_client.post(
        '/api/token/',
        {'Correo': 'admin_inide_api@example.com', 'password': 'secreto'},
        format='json',
    )
    access_token = token_response.data.get('access') if token_response.status_code == 200 else None
    if access_token:
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    resp_censo = api_client.post('/api/censoCompleto/', {}, format='json')
    assert resp_censo.status_code == 204
    assert resp_censo.data.get('message') == 'datos faltantes'

    resp_encuesta = api_client.post('/api/EncuestaCompleta/', {}, format='json')
    assert resp_encuesta.status_code == 400
    assert resp_encuesta.data.get('message') == 'datos faltantes' or 'error' in resp_encuesta.data
