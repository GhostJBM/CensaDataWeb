from datetime import datetime
from unittest.mock import patch

from CensaData.models import Discapacidadespersonas, Discapacidades, Personas


def test_discapacidadespersonas_save_called():
    discapacidad = Discapacidades(id=1)
    persona = Personas(
        primernombre='Ana',
        segundonombre='',
        primerapellido='Lopez',
        segundoapellido='',
        fechadenacimiento=datetime(1995, 5, 5),
        edad=30,
        sexo='F',
        estado=True,
    )

    dp = Discapacidadespersonas(
        discapacidadid=discapacidad,
        personaid=persona,
        estado=True,
    )

    with patch.object(Discapacidadespersonas, 'save', autospec=True) as mock_save:
        dp.save()

    assert mock_save.called
