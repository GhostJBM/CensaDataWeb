from unittest.mock import patch

from CensaData.models import Infraestructuras


def test_infraestructuras_save_called():
    i = Infraestructuras(
        infraestructura='Casa',
        estado=True,
    )

    with patch.object(Infraestructuras, 'save', autospec=True) as mock_save:
        i.save()

    assert mock_save.called
