from unittest.mock import patch

from CensaData.models import Relacionesparentescos


def test_relacionesparentescos_save_called():
    r = Relacionesparentescos(
        relacion='Padre',
        estado=True,
    )

    with patch.object(Relacionesparentescos, 'save', autospec=True) as mock_save:
        r.save()

    assert mock_save.called
