from unittest.mock import patch

from CensaData.models import Departamentos


def test_departamentos_save_called():
    d = Departamentos(
        nombre='Depto 1',
        cantidadmunicipios=1,
        estado=True,
    )

    with patch.object(Departamentos, 'save', autospec=True) as mock_save:
        d.save()

    assert mock_save.called
