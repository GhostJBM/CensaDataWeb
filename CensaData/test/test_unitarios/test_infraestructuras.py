from unittest.mock import patch

from CensaData.models import Infraestructuras
from CensaData.models import Materialesconstrucciones, Tiposdepisos, Tiposdetechos

def test_infraestructuras_save_called():
    material = Materialesconstrucciones(id=1)
    techo = Tiposdetechos(id=1)
    piso = Tiposdepisos(id=1)
    i = Infraestructuras(
        materialcontruccionid=material,
        tipodetechoid = techo,
        tipodepisoid = piso,
        estado=True,
    )

    with patch.object(Infraestructuras, 'save', autospec=True) as mock_save:
        i.save()

    assert mock_save.called
