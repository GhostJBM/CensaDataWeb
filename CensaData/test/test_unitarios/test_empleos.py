from unittest.mock import patch

from CensaData.models import Empleos


def test_empleos_save_called():
    e = Empleos(
        empleo='Ninguno',
        estado=True,
    )

    with patch.object(Empleos, 'save', autospec=True) as mock_save:
        e.save()

    assert mock_save.called
