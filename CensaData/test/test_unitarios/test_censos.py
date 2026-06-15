from datetime import datetime
from unittest.mock import patch

from CensaData.models import Censos


def test_censos_save_called():
    censo = Censos(
        cantidadencuestados=0,
        cantidadrespuestaspositivas=0,
        cantidadrespuestasnegativas=0,
        cantidadencuestas=0,
        muestrapoblacional=0,
        poblaciontotal=0,
        cantidadcasasencuestadas=0,
        fechainiciocenso=datetime(2020, 1, 1),
        fechafincenso=datetime(2020, 1, 2),
        estado=True,
    )

    with patch.object(Censos, 'save', autospec=True) as mock_save:
        censo.save()

    assert mock_save.called
