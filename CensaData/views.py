from rest_framework import viewsets
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdminOrReadOnly
from .services import *
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

class AdministradoresViewSet(viewsets.ModelViewSet):
    queryset = Administradores.objects.all()
    serializer_class = AdministradoresSerializer
    
    def get(self, request):
        user = Cuentasinvestigadoresadmin.objects.filter(estado = 1).all()
        
        authentication_classes = [AllowAny]
        permission_classes = [IsAuthenticated]
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
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        
        partial = kwargs.pop('partial', False)
        
        serializer = self.get_serializer(
                    instance, 
                    data=request.data, 
                    partial=partial
                )

        try:
            serializer.is_valid(raise_exception=True)
            serializer.update(instance,serializer.validated_data)

            return Response({
                "data": serializer.data
            }, status=status.HTTP_200_OK)
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

class meViewSet(APIView):
    def get(self, request):
        try:
            
            user = request.user
            data = Cuentasinvestigadoresadmin.objects.get(id=user.id)
            return Response({
                "id":data.id,
                "Usuario":data.usuario,
                "email":data.Correo,
                "role":data.Role
            })
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    
    authentication_classes = [JWTAuthentication]
    
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
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        
        partial = kwargs.pop('partial', False)
        
        serializer = self.get_serializer(
                    instance, 
                    data=request.data, 
                    partial=partial
                )

        try:
            serializer.is_valid(raise_exception=True)
            serializer.update(instance,serializer.validated_data)

            return Response({
                "data": serializer.data
            }, status=status.HTTP_200_OK)
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
    
    def list(self, request, *args, **kwargs):

            user = Cuentasinvestigadoresadmin.objects.filter(estado = 1).all()
            return Response({"data": user.all().values("id","usuario","Correo","Role")})
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
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    
class CustomeTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomeTokenObtainSerializer
    
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
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        
        partial = kwargs.pop('partial', False)
        
        serializer = self.get_serializer(
                    instance, 
                    data=request.data, 
                    partial=partial
                )

        try:
            serializer.is_valid(raise_exception=True)
            serializer.update(instance,serializer.validated_data)

            return Response({
                "data": serializer.data
            }, status=status.HTTP_200_OK)
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
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        
        partial = kwargs.pop('partial', False)
        
        serializer = self.get_serializer(
                    instance, 
                    data=request.data, 
                    partial=partial
                )

        try:
            serializer.is_valid(raise_exception=True)
            serializer.update(instance,serializer.validated_data)

            return Response({
                "data": serializer.data
            }, status=status.HTTP_200_OK)
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
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        
        partial = kwargs.pop('partial', False)
        
        serializer = self.get_serializer(
                    instance, 
                    data=request.data, 
                    partial=partial
                )

        try:
            serializer.is_valid(raise_exception=True)
            serializer.update(instance,serializer.validated_data)

            return Response({
                "data": serializer.data
            }, status=status.HTTP_200_OK)
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
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        
        partial = kwargs.pop('partial', False)
        
        serializer = self.get_serializer(
                    instance, 
                    data=request.data, 
                    partial=partial
                )

        try:
            serializer.is_valid(raise_exception=True)
            serializer.update(instance,serializer.validated_data)

            return Response({
                "data": serializer.data
            }, status=status.HTTP_200_OK)
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
        
        
        partial = kwargs.pop('partial', False)
        
        serializer = self.get_serializer(
                    instance, 
                    data=request.data, 
                    partial=partial
                )

        try:
            serializer.is_valid(raise_exception=True)
            serializer.update(instance,serializer.validated_data)

            return Response({
                "data": serializer.data
            }, status=status.HTTP_200_OK)
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
        
        return Response({"message":"El Municipio fue Eliminado con exito"})
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
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        
        partial = kwargs.pop('partial', False)
        
        serializer = self.get_serializer(
                    instance, 
                    data=request.data, 
                    partial=partial
                )

        try:
            serializer.is_valid(raise_exception=True)
            serializer.update(instance,serializer.validated_data)

            return Response({
                "data": serializer.data
            }, status=status.HTTP_200_OK)
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
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        
        partial = kwargs.pop('partial', False)
        
        serializer = self.get_serializer(
                    instance, 
                    data=request.data, 
                    partial=partial
                )

        try:
            serializer.is_valid(raise_exception=True)
            serializer.update(instance,serializer.validated_data)

            return Response({
                "data": serializer.data
            }, status=status.HTTP_200_OK)
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
    authentication_classes = [JWTAuthentication]
    
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
    authentication_classes = [JWTAuthentication]
    
class RecoveryPasswordView(APIView):
    def post(self, request):
        email = request.data.get("Correo")
        
        user = Cuentasinvestigadoresadmin.objects.filter(
            Correo = email
        ).first()
        
        if not user:
            return Response({
                "message":"Si existe la cuenta se enviará un correo"
            })
            
        code = RecoveryPasswordService.create_recoveryCode(
            user
        )
        
        return Response({
            "message":"Codigo enviado"
        })
    permission_classes=[AllowAny]
    
class VerificarPasswordView(APIView):
    def post(self, request):
        cuentaid = request.data.get("Id")
        cuenta = Cuentasinvestigadoresadmin.objects.filter(Correo=cuentaid).first()
        code = request.data.get("code")
        token = None
        try:
            token = RecoveryPasswordService.verifyCode(cuenta, code)
        except ExcepcionNegocio as e:
            return Response({
                "error":str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if not token:
            return Response({
                "message":"Código invalido"
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "token":token
        })
    permission_classes=[AllowAny]
class changePasswordView(APIView):
    def post(self, request):
        token = request.data.get("token")
        password = request.data.get("password")
        
        success=RecoveryPasswordService.changePassword(
            token,
            password
        )
        
        if not success:
            return Response({
                "message":"Token invalido"
            }, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({
            "message":"Contraseña cambiada"
        }, status=status.HTTP_200_OK)
    permission_classes=[AllowAny]
## Views de reportes
class EstadisticasINIDEView(APIView):
    pass