from unittest.mock import patch

from CensaData.models import Estadosciviles


def test_estadosciviles_save_called():
    e = Estadosciviles(
        estadocivil='Soltero',
        estado=True,
    )

    with patch.object(Estadosciviles, 'save', autospec=True) as mock_save:
        e.save()

    assert mock_save.called
