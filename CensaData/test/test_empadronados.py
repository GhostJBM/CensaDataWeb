from unittest.mock import patch
from decimal import Decimal

from CensaData.models import Empadronados, Personas, Relacionesparentescos, Estadosciviles, Empleos, Niveleseducativos, Casas


def test_empadronados_save_called():
    persona = Personas(id=1)
    relacion = Relacionesparentescos(id=1)
    estadocivil = Estadosciviles(id=1)
    empleo = Empleos(id=1)
    nivel = Niveleseducativos(id=1)
    casa = Casas(id=1)

    emp = Empadronados(
        personaid=persona,
        relacionid=relacion,
        numerocedula='00000000',
        estadocivilid=estadocivil,
        empleoid=empleo,
        niveleducativoid=nivel,
        casaid=casa,
        ingresopersonal=Decimal('0.00'),
        estado=True,
    )

    with patch.object(Empadronados, 'save', autospec=True) as mock_save:
        emp.save()

    assert mock_save.called
