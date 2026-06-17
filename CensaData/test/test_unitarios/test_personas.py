from datetime import datetime
from unittest.mock import patch

from CensaData.models import Personas


def test_personas_save_called():
    persona = Personas(
        primernombre='Juan',
        segundonombre='',
        primerapellido='Perez',
        segundoapellido='',
        fechadenacimiento=datetime(1990, 1, 1),
        edad=30,
        sexo='M',
        estado=True,
    )

    with patch.object(Personas, 'save', autospec=True) as mock_save:
        persona.save()

    assert mock_save.called
