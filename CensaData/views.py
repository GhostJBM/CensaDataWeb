from rest_framework import viewsets
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdminOrReadOnly
from .services import *
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from ninja import NinjaAPI

class AdministradoresViewSet(viewsets.ModelViewSet):
    queryset = Administradores.objects.all()
    serializer_class = AdministradoresSerializer
    def create(self, request):
        if not request.data:
            return Response({
                "message":"No hay contenido"
            },
            status=status.HTTP_204_NO_CONTENT
            )
            
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                "message":"Administrador creado con exito"
            }, status=status.HTTP_201_CREATED)
        except ExcepcionNegocio as e:
            return Response(
                {
                    "error":str(e),
                    
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        serializer = self.get_serializer()
        serializer.delete(instance)
        return Response({"message":"El Administrador se elimino"})
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

class InvestigadoresViewSet(viewsets.ModelViewSet):
    queryset = Investigadores.objects.all()
    serializer_class = InvestigadoresSerializer
    def create(self, request):
        if not request.data:
            return Response({
                "message":"No hay contenido"
            },
            status=status.HTTP_204_NO_CONTENT
            )
            
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                "message":"Investigador creado con exito"
            }, status=status.HTTP_201_CREATED)
        except ExcepcionNegocio as e:
            return Response(
                {
                    "error":str(e),
                    
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        serializer = self.get_serializer()
        serializer.delete(instance)
        return Response({"message":"El investigador se elimino"})
        
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    
class CuentasInvestigadoresViewSet(viewsets.ModelViewSet):
    queryset = Cuentasinvestigadoresadmin.objects.all()
    serializer_class = CuentaInvestigadorCreationSerializer
    
    
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return CuentaInvestigadorCreationSerializer
        return Cuentasinvestigadoresadmin
    
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
    permission_classes = [IsAdminOrReadOnly]
    
class añosEscolaresDocentesViewSet(viewsets.ModelViewSet):
    queryset = Añosescolaresdocentes.objects.all()
    serializer_class = AñosescolaresdocentesSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    
class BarriosViewSet(viewsets.ModelViewSet):
    queryset = Barrios.objects.all()
    serializer_class = BarriosSerializer
    def create(self, request):
        if not request.data:
            return Response({
                "message":"No hay contenido"
            },
            status=status.HTTP_204_NO_CONTENT
            )
            
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                "message":"Barrio creado con exito"
            }, status=status.HTTP_201_CREATED)
        except ExcepcionNegocio as e:
            return Response(
                {
                    "error":str(e),
                    
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        serializer = self.get_serializer()
        serializer.delete(instance)
        return Response({f"message":"Se elimino el registro"})
        
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    
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
    def create(self, request):
        if not request.data:
            return Response({
                "message":"No hay contenido"
            },
            status=status.HTTP_204_NO_CONTENT
            )
            
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                "message":"Departamento creado con exito"
            }, status=status.HTTP_201_CREATED)
        except ExcepcionNegocio as e:
            return Response(
                {
                    "error":str(e),
                    
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        serializer = self.get_serializer()
        serializer.delete(instance)
        return Response({"message":"El departamento se ha eliminado"})
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
        
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
    def create(self, request):
        if not request.data:
            return Response({
                "message":"No hay contenido"
            },
            status=status.HTTP_204_NO_CONTENT
            )
            
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                "message":"Empleo creado con exito"
            }, status=status.HTTP_201_CREATED)
        except ExcepcionNegocio as e:
            return Response(
                {
                    "error":str(e),
                    
                },
                status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        serializer = self.get_serializer()
        serializer.delete(instance)
        return Response({"message":"El empleo ha sido eliminado"})
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    
class CensosViewSet(viewsets.ModelViewSet):
    queryset = Censos.objects.all()
    serializer_class = CensosSerializer
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
    def create(self, request):
        if not request.data:
            return Response({
                "message":"No hay contenido"
            },
            status=status.HTTP_204_NO_CONTENT
            )
            
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                "message":"Estado civil creado con exito"
            }, status=status.HTTP_201_CREATED)
        except ExcepcionNegocio as e:
            return Response(
                {
                    "error":str(e),
                    
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        serializer = self.get_serializer()
        serializer.delete(instance)
        return Response({"message":"El estado civil fue eliminado"})
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    
class EstudiantesViewSet(viewsets.ModelViewSet):
    queryset = Estudiantes.objects.all()
    serializer_class = EstudiantesSerializer
    authentication_classes = [JWTAuthentication]
    
class InfraestructurasViewSet(viewsets.ModelViewSet):
    queryset = Infraestructuras.objects.all()
    serializer_class = InfraestructuraSerializer
    authentication_classes=[JWTAuthentication]
class MunicipiosViewSet(viewsets.ModelViewSet):
    queryset = Municipios.objects.all()
    serializer_class = MunicipiosSerializer
    def create(self, request):
        if not request.data:
            return Response({
                "message":"No hay contenido"
            },
            status=status.HTTP_204_NO_CONTENT
            )
            
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                "message":"Municipio creado con exito"
            }, status=status.HTTP_201_CREATED)
        except ExcepcionNegocio as e:
            return Response(
                {
                    "error":str(e),
                    
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        serializer = self.get_serializer()
        serializer.delete(instance)
        
        return Response({"message":"El Municipio fue actualizado con exito"})
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

class PersonasViewSet(viewsets.ModelViewSet):
    queryset = Personas.objects.all()
    serializer_class = PersonasSerializer
    authentication_classes = [JWTAuthentication]
    
class RelacionesParentescosViewSet(viewsets.ModelViewSet):
    queryset = Relacionesparentescos.objects.all()
    serializer_class = RelacionesparentescosSerializer
    def create(self, request):
        if not request.data:
            return Response({
                "message":"No hay contenido"
            },
            status=status.HTTP_204_NO_CONTENT
            )
            
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                "message":"Relacion de parentesco creada con exito"
            }, status=status.HTTP_201_CREATED)
        except ExcepcionNegocio as e:
            return Response(
                {
                    "error":str(e),
                    
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        serializer = self.get_serializer()
        
        serializer.delete(instance)
        return Response({"message":"La relacion fue eliminada"})
            
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
class NivelesEduactivosViewSet(viewsets.ModelViewSet):
    queryset = Niveleseducativos.objects.all()
    serializer_class = NivelesEduactivosSerializer
    def create(self, request):
        if not request.data:
            return Response({
                "message":"No hay contenido"
            },
            status=status.HTTP_204_NO_CONTENT
            )
            
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                "message":"nivel educativo creado con exito"
            }, status=status.HTTP_201_CREATED)
        except ExcepcionNegocio as e:
            return Response(
                {
                    "error":str(e),
                    
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        serializer =self.get_serializer()
        serializer.delete(instance)
        return Response({"message":"El nivel educativo fue eliminado"})
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
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
    
## views personalizadas
class CensoCompletoINIDETrabajadoresViewSet(APIView):
    authentication_classes = [JWTAuthentication]
    
    def post(self, request):

        if not request.data :
            return Response({
                "message":"datos faltantes"
            }, status=status.HTTP_204_NO_CONTENT)
            
        data = request.data
        try:
            encuesta = CensoInideService.CrearCenso(self,data)
            return Response(
                {
                    "message":"Censo creado con exito"
                    
                },
                status=status.HTTP_201_CREATED
            )
        except ExcepcionNegocio as e:
            return Response(
                {
                    "error":str(e),
                    
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    
class EncuestaINIDETrabajadosCompletaViewSet(APIView):
    def post(self, request):
        if not request.data :
            return Response({
                "message":"datos faltantes"
            }, status=status.HTTP_400_BAD_REQUEST)
            
        data = request.data
        user = request.user
        try:
            encuesta = EncuestaInideService.CrearEncuesta(self,data,user)
            return Response(
                {
                    "message":"Encuesta creado con exito"
                    
                },
                status=status.HTTP_201_CREATED
            )
        except ExcepcionNegocio as e:
            return Response(
                {
                    "error":str(e),
                    
                },
                status=status.HTTP_400_BAD_REQUEST
            )