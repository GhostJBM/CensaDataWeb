from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Administradores, Investigadores, Cuentasinvestigadores
from .serializers import AdministradoresSerializer, InvestigadoresSerializer, CuentasinvestigadoresSerializer,CuentaInvestigadorCreationSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class AdministradoresViewSet(viewsets.ModelViewSet):
    queryset = Administradores.objects.all()
    serializer_class = AdministradoresSerializer
    authentication_classes = [JWTAuthentication]
    

class InvestigadoresViewSet(viewsets.ModelViewSet):
    queryset = Investigadores.objects.all()
    serializer_class = InvestigadoresSerializer
    authentication_classes = [JWTAuthentication]
    
class CuentasInvestigadoresViewSet(viewsets.ModelViewSet):
    queryset = Cuentasinvestigadores.objects.all()
    
    serializer_class = CuentasinvestigadoresSerializer
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return CuentaInvestigadorCreationSerializer
        return Cuentasinvestigadores
    
    def get_permissions(self):
        if self.action == 'create': # 'create' es el método POST
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]