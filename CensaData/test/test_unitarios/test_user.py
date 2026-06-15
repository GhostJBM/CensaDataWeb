import pytest
from unittest.mock import patch

from CensaData.models import Cuentasinvestigadoresadmin


def test_str_returns_usuario():
    user = Cuentasinvestigadoresadmin(
        usuario='juan',
        Correo='juan@example.com',
        Role='ADMINISTRADOR'
    )

    assert str(user) == 'juan'


def test_create_user_hashes_password_and_saves():
    manager = Cuentasinvestigadoresadmin.objects

    with patch.object(Cuentasinvestigadoresadmin, 'save', autospec=True) as mock_save:
        user = manager.create_user(
            'juan',
            'secreto',
            Correo='juan@example.com',
            Role='INVESTIGADOR'
        )

    assert user.usuario == 'juan'
    assert user.Correo == 'juan@example.com'
    assert user.Role == 'INVESTIGADOR'
    assert user.check_password('secreto')
    assert user.password != 'secreto'
    mock_save.assert_called_once_with(user, using=manager._db)


def test_create_superuser_sets_staff_and_superuser():
    manager = Cuentasinvestigadoresadmin.objects

    with patch.object(Cuentasinvestigadoresadmin, 'save', autospec=True) as mock_save:
        user = manager.create_superuser(
            'admin',
            'secreto',
            Correo='admin@example.com',
            Role='ADMINISTRADOR'
        )

    assert user.is_staff is True
    assert user.is_superuser is True
    assert user.check_password('secreto')
    mock_save.assert_called_once_with(user, using=manager._db)


def test_create_user_without_usuario_raises_value_error():
    manager = Cuentasinvestigadoresadmin.objects

    with pytest.raises(ValueError):
        manager.create_user(
            '',
            'secreto',
            Correo='juan@example.com',
            Role='INVESTIGADOR'
        )
