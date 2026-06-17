from unittest.mock import patch

from CensaData.models import Contactosempadronados, Empadronados


def test_contactosempadronados_save_called():
    emp = Empadronados(id=1)
    ce = Contactosempadronados(
        contacto=87654321,
        empadronadoid=emp,
        estado=True,
    )

    with patch.object(Contactosempadronados, 'save', autospec=True) as mock_save:
        ce.save()

    assert mock_save.called
