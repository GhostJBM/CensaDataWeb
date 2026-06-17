from unittest.mock import patch

from CensaData.models import Barrios, Municipios


def test_barrios_save_called():
    municipio = Municipios(id=1)
    b = Barrios(
        nombre='Barrio 1',
        cantidadcasas=10,
        municipioid=municipio,
        estado=True,
    )

    with patch.object(Barrios, 'save', autospec=True) as mock_save:
        b.save()

    assert mock_save.called
