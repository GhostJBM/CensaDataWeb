import pytest
from unittest.mock import patch
from datetime import datetime

from CensaData.models import (
    Encuestasinidetrabajadores,
    Casas,
    Censos,
    Investigadores,
)


def test_encuestasinidetrabajadores_save_called():
    casa = Casas(id=1)
    censo = Censos(id=1)
    investigador = Investigadores(id=1)

    encuesta = Encuestasinidetrabajadores(
        casaid=casa,
        censoid=censo,
        investigadorid=investigador,
        fechainicio=datetime(2020, 1, 1),
        fechafin=datetime(2020, 1, 2),
        respuesta='POSITIVA',
        totalencuestados=0,
        estado=True,
    )

    with patch.object(Encuestasinidetrabajadores, 'save', autospec=True) as mock_save:
        encuesta.save()

    assert mock_save.called
