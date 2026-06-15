from unittest.mock import patch

from CensaData.models import Discapacidades


def test_discapacidades_save_called():
    d = Discapacidades(
        discapacidad='Visual',
        estado=True,
    )

    with patch.object(Discapacidades, 'save', autospec=True) as mock_save:
        d.save()

    assert mock_save.called
