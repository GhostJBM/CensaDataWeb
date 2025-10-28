from django.urls import path
from rest_framework import routers
from CensaData.views import InvestigadoresViewSet, AdministradoresViewSet, CuentasInvestigadoresViewSet

router = routers.DefaultRouter()
router.register(r'investigadores', InvestigadoresViewSet)
router.register(r'administradores', AdministradoresViewSet)
router.register(r'cuentasInvestigadores', CuentasInvestigadoresViewSet)

urlpatterns = router.urls
