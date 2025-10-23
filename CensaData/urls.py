from django.urls import path
from rest_framework import routers
from CensaData.views import InvestigadoresViewSet, AdministradoresViewSet

router = routers.DefaultRouter()
router.register(r'investigadores', InvestigadoresViewSet)
router.register(r'administradores', AdministradoresViewSet)

urlpatterns = router.urls
