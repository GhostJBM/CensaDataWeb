from unittest.mock import patch

from CensaData.models import Niveleseducativos


def test_niveleseducativos_save_called():
    n = Niveleseducativos(
        nivel='Primaria',
        estado=True,
    )

    with patch.object(Niveleseducativos, 'save', autospec=True) as mock_save:
        n.save()

    assert mock_save.called
