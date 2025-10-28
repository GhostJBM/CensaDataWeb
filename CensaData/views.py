from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Administradores, Investigadores
from .serializers import AdministradoresSerializer, InvestigadoresSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class AdministradoresViewSet(viewsets.ModelViewSet):
    queryset = Administradores.objects.all()
    serializer_class = AdministradoresSerializer
    authentication_classes = [JWTAuthentication]
    

class InvestigadoresViewSet(viewsets.ModelViewSet):
    queryset = Investigadores.objects.all()
    serializer_class = InvestigadoresSerializer
    authentication_classes = [JWTAuthentication]