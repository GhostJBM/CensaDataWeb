import pytest
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
from CensaData.services import EncuestaInideService, ExcepcionNegocio

pytestmark = pytest.mark.django_db


@pytest.fixture
def encuesta_setup(db):
    admin_user = Cuentasinvestigadoresadmin.objects.create_user(
        usuario='admin_inide',
        password='secreto',
        Correo='admin_inide@example.com',
        Role='ADMINISTRADOR',
        is_staff=1,
        is_superuser=1,
        is_active=1,
        estado=1,
    )

    user_inves= Cuentasinvestigadoresadmin.objects.create_user(
        usuario='admitn_contact',
        password='secreto',
        Correo='adm7_contact@example.com',
        Role='INVESTIGADOR',
        is_staff=1,
        is_superuser=1,
        is_active=1,
        estado=1,
    )


    admin=    Administradores.objects.create(
        primernombre='Ivan',
        segundonombre='',
        primerapellido='Perez',
        segundoapellido='',
        edad=30,
        sexo='M',
        estado=1,
        cuentaid=admin_user,
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


def test_crear_encuesta_inide_trabajador_complete_flow(encuesta_setup):
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

    assert Encuestasinidetrabajadores.objects.filter(
        censoid=encuesta_setup['censo'],
        investigadorid=encuesta_setup['investigador']
    ).exists()


def test_crear_encuesta_inide_invalid_date_raises(encuesta_setup):
    service = EncuestaInideService()

    payload = {
        'Casa': {
            'numcasa': 12,
            'barrioid': encuesta_setup['barrio'].id,
            'infraestructuraid': encuesta_setup['infraestructura'].id,
            'serviciodeagua': 1,
            'serviciodeenergia': 0,
        },
        'encuestainide': {
            'censoid': encuesta_setup['censo'].id,
            'fechainicio': '2000-01-01',
            'fechafin': '2000-01-02',
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

    with pytest.raises(ExcepcionNegocio):
        service.CrearEncuesta(payload, encuesta_setup['user'])