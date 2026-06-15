from unittest.mock import patch

from CensaData.models import Contactosinvestigadores, Investigadores


def test_contactosinvestigadores_save_called():
    investigador = Investigadores(id=1)
    ci = Contactosinvestigadores(
        contacto=12345678,
        investigadorid=investigador,
        estado=True,
    )

    with patch.object(Contactosinvestigadores, 'save', autospec=True) as mock_save:
        ci.save()

    assert mock_save.called
