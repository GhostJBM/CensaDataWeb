from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *
from .serializers import *
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
    
class añosEscolaresViewSet(viewsets.ModelViewSet):
    queryset = Añosescolares.objects.all()
    serializer_class = AñosescolaresSerializer
    authentication_classes = [JWTAuthentication]
    
class añosEscolaresDocentesViewSet(viewsets.ModelViewSet):
    queryset = Añosescolaresdocentes.objects.all()
    serializer_class = AñosescolaresdocentesSerializer
    authentication_classes = [JWTAuthentication]
    
class BarriosViewSet(viewsets.ModelViewSet):
    queryset = Barrios.objects.all()
    serializer_class = BarriosSerializer
    authentication_classes = [JWTAuthentication]

class CasasViewSet(viewsets.ModelViewSet):
    queryset = Casas.objects.all()
    serializer_class = CasasSerializer
    authentication_classes = [JWTAuthentication]
    
class CentrosEducativosViewSet(viewsets.ModelViewSet):
    queryset = Centroseducativos.objects.all()
    serializer_class = CentroseducativosSerializer
    authentication_classes = [JWTAuthentication]

class CentrosEducativosDocentesViewSet(viewsets.ModelViewSet):
    queryset = Centroseducativosdocentes.objects.all()
    serializer_class = CentroseducativosdocentesSerializer
    authentication_classes = [JWTAuthentication]

class ContactosCentrosEducativosViewSet(viewsets.ModelViewSet):
    queryset = Contactoscentroseducativos.objects.all()
    serializer_class = ContactoscentroseducativosSerializer
    authentication_classes = [JWTAuthentication]
    
class ContactosDirectoresViewSet(viewsets.ModelViewSet):
    queryset = Contactosdirectores.objects.all()
    serializer_class = ContactosdirectoresSerializer
    authentication_classes = [JWTAuthentication]
    
class ContactosDocentesViewSet(viewsets.ModelViewSet):
    queryset = Contactosdocentes.objects.all()
    serializer_class = ContactosdocentesSerializer
    authentication_classes = [JWTAuthentication]    

class ContactosInvestigadoresViewSet(viewsets.ModelViewSet):
    queryset = Contactosinvestigadores.objects.all()
    serializer_class = ContactosinvestigadoresSerializer
    authentication_classes = [JWTAuthentication]
    

class DepartamentosViewSet(viewsets.ModelViewSet):
    queryset = Departamentos.objects.all()
    serializer_class = DepartamentosSerializer
    authentication_classes = [JWTAuthentication]
    
class DirectoresViewSet(viewsets.ModelViewSet):
    queryset = Directores.objects.all()
    serializer_class = DirectoresSerializer
    authentication_classes = [JWTAuthentication]
    
class DocentesViewSet(viewsets.ModelViewSet):
    queryset = Docentes.objects.all()
    serializer_class = DocentesSerializer
    authentication_classes = [JWTAuthentication]
    
class DocentesEstudiantesViewSet(viewsets.ModelViewSet):
    queryset = Docentesestudiantes.objects.all()
    serializer_class = DocentesestudiantesSerializer
    authentication_classes = [JWTAuthentication]
    
class EmpadronadosViewSet(viewsets.ModelViewSet):
    queryset = Empadronados.objects.all()
    serializer_class = EmpadronadosSerializer
    authentication_classes = [JWTAuthentication]
    
class EmpleosViewSet(viewsets.ModelViewSet):
    queryset = Empleos.objects.all()
    serializer_class = EmpleosSerializer
    authentication_classes = [JWTAuthentication]
    
class EncuestasViewSet(viewsets.ModelViewSet):
    queryset = Encuestas.objects.all()
    serializer_class = EncuestasSerializer
    authentication_classes = [JWTAuthentication]
    
class EncuestasInideTrabajadoresViewSet(viewsets.ModelViewSet):
    queryset = Encuestasinidetrabajadores.objects.all()
    serializer_class = EncuestasinidetrabajadoresSerializer
    authentication_classes = [JWTAuthentication]
    
class EncuestasMinedEscolaresViewSet(viewsets.ModelViewSet):
    queryset = Encuestasminedescolares.objects.all()
    serializer_class = EncuestasminedescolaresSerializer
    authentication_classes = [JWTAuthentication]
    
class EstadosCivilesViewSet(viewsets.ModelViewSet):
    queryset = Estadosciviles.objects.all()
    serializer_class = EstadoscivilesSerializer
    authentication_classes = [JWTAuthentication]
    
class EstudiantesViewSet(viewsets.ModelViewSet):
    queryset = Estudiantes.objects.all()
    serializer_class = EstudiantesSerializer
    authentication_classes = [JWTAuthentication]
    

class MunicipiosViewSet(viewsets.ModelViewSet):
    queryset = Municipios.objects.all()
    serializer_class = MunicipiosSerializer
    authentication_classes = [JWTAuthentication]
    

class PersonasViewSet(viewsets.ModelViewSet):
    queryset = Personas.objects.all()
    serializer_class = PersonasSerializer
    authentication_classes = [JWTAuthentication]
    
class RelacionesParentescosViewSet(viewsets.ModelViewSet):
    queryset = Relacionesparentescos.objects.all()
    serializer_class = RelacionesparentescosSerializer
    authentication_classes = [JWTAuthentication]
    
class TiposDeEducacionesViewSet(viewsets.ModelViewSet):
    queryset = Tiposdeeducaciones.objects.all()
    serializer_class = TiposdeeducacionesSerializer
    authentication_classes = [JWTAuthentication]
    
class TiposDeEducacionesDocentesViewSet(viewsets.ModelViewSet):
    queryset = Tiposdeeducacionesdocentes.objects.all()
    serializer_class = TiposdeeducacionesdocentesSerializer
    authentication_classes = [JWTAuthentication]
    
class TutoresViewSet(viewsets.ModelViewSet):
    queryset = Tutores.objects.all()
    serializer_class = TutoresSerializer
    authentication_classes = [JWTAuthentication]