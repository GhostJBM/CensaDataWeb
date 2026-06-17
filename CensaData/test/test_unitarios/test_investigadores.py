from unittest.mock import patch

from CensaData.models import Investigadores, Cuentasinvestigadoresadmin


def test_investigadores_save_called():
    cuenta = Cuentasinvestigadoresadmin(id=1)
    inv = Investigadores(
        cuentaid=cuenta,
        estado=True,
    )

    with patch.object(Investigadores, 'save', autospec=True) as mock_save:
        inv.save()

    assert mock_save.called
