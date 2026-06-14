from unittest.mock import patch

from CensaData.models import Municipios, Departamentos


def test_municipios_save_called():
    depto = Departamentos(id=1)
    m = Municipios(
        nombre='Municipio 1',
        departamentoid=depto,
        estado=True,
    )

    with patch.object(Municipios, 'save', autospec=True) as mock_save:
        m.save()

    assert mock_save.called
