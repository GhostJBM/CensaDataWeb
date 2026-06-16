from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Cuentasinvestigadoresadmin

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        rol = Cuentasinvestigadoresadmin.objects.filter(id=request.user.id).first()
        
        if rol.Role == "ADMINISTRADOR":
            return True
        if rol.Role == "INVESTIGADOR":
            return request.method == "GET"
        
        return False

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        rol = Cuentasinvestigadoresadmin.objects.filter(id=request.user.id).first()
        
        if rol.Role != "ADMINISTRADOR":
            return False
        return True
        
class IsVisitante(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        rol = Cuentasinvestigadoresadmin.objects.filter(id=request.user.id).first()
        
        if rol.Role != "VISITANTE":
            return False
        return request.method == "GET"