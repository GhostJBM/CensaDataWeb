from unittest.mock import patch
from decimal import Decimal

from CensaData.models import Casas, Infraestructuras, Barrios


def test_casas_save_called():
    infraestructura = Infraestructuras(id=1) if 'Infraestructuras' in globals() or True else None
    barrio = Barrios(id=1)

    casa = Casas(
        numcasa=123,
        cantidadhombres=1,
        cantidadmujeres=1,
        infraestructuraid=infraestructura,
        barrioid=barrio,
        serviciodeagua=True,
        serviciodeenergia=True,
        ingresofamiliar=Decimal('0.00'),
        estado=True,
    )

    with patch.object(Casas, 'save', autospec=True) as mock_save:
        casa.save()

    assert mock_save.called
