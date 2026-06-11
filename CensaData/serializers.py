from rest_framework import serializers
from .models import Añosescolares, Añosescolaresdocentes, Administradores, Barrios,Casas,Centroseducativos,Centroseducativosdocentes,Contactoscentroseducativos,Contactosdirectores,Contactosdocentes,Contactosinvestigadores,Contactostutores,Cuentasinvestigadoresadmin,CustomInvestigadorAdminManager, Departamentos,Directores,Docentes,Docentesestudiantes,Empadronados,Empleos,Censos,Encuestasinidetrabajadores,Encuestasminedescolares,Estadosciviles,Estudiantes,Investigadores,Municipios,Personas,Relacionesparentescos,Tiposdeeducaciones,Tiposdeeducacionesdocentes,Tutores
from .services import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from django.db.models import Q

## serializer para las tablas

class AñosescolaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Añosescolares
        fields = '__all__'
    


class AñosescolaresdocentesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Añosescolaresdocentes
        fields = '__all__'

class AdministradoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administradores
        fields = '__all__'
    def create(self, validated_data):
        validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin.valiExistAdmin(validated_data) 
        segundoNombre = validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin.segundoNombre(validated_data)
        segundoApellido = validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin.segundoApellido(validated_data)
        investigador = Investigadores.objects.create(
            primernombre = validated_data["primernombre"],
            segundonombre = segundoNombre,
            primerapellido = validated_data["primerapellido"],
            segundoapellido = segundoApellido,
            sexo = validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin.sexo(validated_data["sexo"]),
            edad = validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin.edad(validated_data["edad"]),
            estado = 1,
            cuentaid = validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin.cuenta(validated_data["cuentaid"]),
            administradorid = validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin.admin(validated_data["administradorid"])
        )
        return investigador
    def update(self, instance, validated_data):
            
            segundoNombre = validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin.segundoNombre(validated_data.get("segundonombre",instance.segundonombre))
            segundoApellido = validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin.segundoApellido(validated_data.get("segundoapellido", instance.segundoapellido))
            instance.primernombre = validated_data.get("primernombre", instance.primernomre)
            instance.segundonombre = segundoNombre
            instance.primerapellido = validated_data.get("primerapellido", instance.primerapellido)
            instance.segundoapellido = segundoApellido
            instance.sexo = validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin.sexo(validated_data.get("sexo", instance.sexo))
            instance.edad = validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin.edad(validated_data.get("edad", instance.edad))
            instance.estado = instance.estado
            instance.cuentaid = validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin.cuenta(validated_data.get("cuentaid", instance.cuentaid))
            instance.save()
            return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance
        
class BarriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrios
        fields = '__all__'

    def create(self, validated_data):
        validacionesInidividualesIncercion.validacionesBarrios.valiExiste(validated_data)
        barrio = Barrios.objects.create(
                nombre = validated_data["nombre"],
                cantidadcasas = 0,
                estado = 1,
                municipioid = validated_data["municipioid"]
            )
        return barrio
    def update(self, instance, validated_data):
        Barrio = Barrios.objects.get(id=instance.id)
        instance.nombre = validated_data.get("nombre", instance.nombre)
        instance.cantidadcasas = Barrio.cantidadcasas
        instance.estado = instance.estado
        
        instance.save()
        return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance
class CasasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casas
        fields = '__all__'
        
class CentroseducativosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Centroseducativos
        fields = '__all__'

class CentroseducativosdocentesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Centroseducativosdocentes
        fields = '__all__'  
        
class ContactoscentroseducativosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactoscentroseducativos
        fields = '__all__'  
        
class ContactosdirectoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactosdirectores
        fields = '__all__'  
        
class ContactosdocentesSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Contactosdocentes
        fields = '__all__'  
        
class ContactosinvestigadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactosinvestigadores
        fields = '__all__'
        
class ContactostutoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactostutores
        fields = '__all__'
        
# Serializador para crear un nuevo Cliente (con contraseña)
class CuentaInvestigadorCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuentasinvestigadoresadmin
        # Campos que el usuario enviará
        fields = ('usuario', 'password', "Role","Correo")
        # La contraseña solo se puede escribir
        extra_kwargs = {'password': {'write_only': True}}

    # Método para guardar el usuario con contraseña encriptada
    def create(self, validated_data):
        # Usamos el método create_user que definimos en el Manager
        VRole = str(validated_data["Role"]).upper()
        
        user = Cuentasinvestigadoresadmin.objects.create_user(
            usuario=validated_data['usuario'],
            password=validated_data['password'],
            Role=VRole,
            Correo=validated_data["Correo"],
            is_staff = 0,
            is_superuser = 0,
            is_active = 1,
            estado = 1)  
        return user

class  CuentasInvestigadoresAdmin(serializers.ModelSerializer):
    class Meta:
        model = Cuentasinvestigadoresadmin
        fields = 'usuario, password, Role, Correo'
    def create(self, validated_data):
        return True
    def update(self, instance, validated_data):
        return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance
        
                
class CustomeTokenObtainSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        login = attrs.get("Correo")
        password = attrs.get("password")
        
        user = Cuentasinvestigadoresadmin.objects.filter(Q( Correo = login) |Q(usuario=login) ).first()
        
        if not user:
            raise AuthenticationFailed("Credenciales invalidas")
        if not user.check_password(password):
            raise AuthenticationFailed("Credenciales invalidas")
        refresh = self.get_token(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

class DepartamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamentos
        fields = '__all__'
    
    def create(self, validated_data):
        validacionesInidividualesIncercion.validacionesDepartamentos.valiExiste(validated_data)
        departamento = Departamentos.objects.create(
            nombre = validated_data["nombre"],
            cantidadmunicipios = 0,
            estado = 1
        )
        return departamento
    def update(self, instance, validated_data):
        instance.nombre = validated_data.get("nombre", instance.nombre)
        instance.cantidadmunicipios = instance.cantidadmunicipios
        instance.estado = instance.estado
        instance.save()
        return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance
        
class DirectoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directores
        fields = '__all__'
        
class DocentesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docentes
        fields = '__all__'
        
class DocentesestudiantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docentesestudiantes
        fields = '__all__'      
        
class EmpadronadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empadronados
        fields = '__all__'
        
        
    def create(self, validated_data):
        validacionesInidividualesIncercion.validacionesDepartamentos.valiExiste(validated_data)
        departamento = Departamentos.objects.create(
            nombre = validated_data["nombre"],
            cantidadmunicipios = 0,
            estado = 1
        )
        return departamento
    def update(self, instance, validated_data):
        instance.nombre = validated_data.get("nombre", instance.nombre)
        instance.cantidadmunicipios = instance.cantidadmunicipios
        instance.estado = instance.estado
        instance.save()
        return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance
        
class EmpleosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleos
        fields = '__all__' 
    def create(self, validated_data):
        validacionesInidividualesIncercion.validacionesEmpleos.valiExiste(validated_data)
        Empleo = Empleos.objects.create(
            empleo = validated_data["empleo"]
        )
        return Empleo
    def update(self, instance, validated_data):
        instance.empleo = validated_data.get("empleo", instance.empleo)
        instance.estado = instance.estado
        instance.save() 
        return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance
        
class CensosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Censos
        fields = '__all__'  
        
class EncuestasinidetrabajadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encuestasinidetrabajadores
        fields = '__all__'
        
class EncuestasminedescolaresSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Encuestasminedescolares
        fields = '__all__'
        
class EstadoscivilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadosciviles
        fields = '__all__'
        

    def create(self, validated_data):
        validacionesInidividualesIncercion.validacionesEstadoCiviles.valiExiste(validated_data)
        estado = Estadosciviles.objects.create(
            estadocivil=validated_data["estadocivil"],
            estado = 1
        )
        return estado
    def update(self, instance, validated_data):
        instance.estadocivil = validated_data.get("estadocivil", instance.estadocivil)
        instance.estado = instance.estado
        instance.save()
        return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance
        
class EstudiantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiantes
        fields = '__all__'
class NivelesEduactivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveleseducativos
        fields = '__all__'
    def create(self, validated_data):
        validacionesInidividualesIncercion.validacionesNivelesEducativos.valiExiste(validated_data)
        nivel = Niveleseducativos.objects.create(
            niveleducativo = validated_data["nivelEducativo"],
            grado = validated_data["grado"],
            estado = 1
        )
        return nivel
    def update(self, instance, validated_data):
        instance.niveleducativo = validated_data.get("nivelEducativo", instance.niveleducativo)
        instance.grado = validated_data.get("grado", instance.grado)
        instance.estado = instance.estado
        instance.save()
        return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance
                
class InvestigadoresSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Investigadores
        fields = '__all__'
    
    def create(self, validated_data):
        validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin.valiExisteInves(validated_data) 
        segundoNombre = validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin.segundoNombre(validated_data)
        segundoApellido = validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin.segundoApellido(validated_data)
        investigador = Investigadores.objects.create(
            primernombre = validated_data["primernombre"],
            segundonombre = segundoNombre,
            primerapellido = validated_data["primerapellido"],
            segundoapellido = segundoApellido,
            sexo = validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin.sexo(validated_data["sexo"]),
            edad = validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin.edad(validated_data["edad"]),
            estado = 1,
            cuentaid = validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin.cuenta(validated_data["cuentaid"]),
            administradorid = validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin.admin(validated_data["administradorid"])
        )
        return investigador
    
    def update(self, instance, validated_data):
        Val = validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin

        instance.primernombre = validated_data.get("primernombre", instance.primernombre)

        instance.segundonombre = Val.segundoNombre(
            validated_data.get("segundonombre", instance.segundonombre)
        )

        instance.primerapellido = validated_data.get("primerapellido", instance.primerapellido)

        instance.segundoapellido = Val.segundoApellido(
        validated_data.get("segundoapellido", instance.segundoapellido)
        )

        instance.edad = Val.edad(
            validated_data.get("edad", instance.edad)
        )

        instance.sexo = Val.sexo(
            validated_data.get("sexo", instance.sexo)
        )
        instance.estado = instance.estado

        instance.cuentaid = Val.cuenta(
            validated_data.get("cuentaid", instance.cuentaid)
        )

        instance.administradorid = Val.admin(
            validated_data.get("administradorid", instance.administradorid)
        )

        instance.save()
        return instance

    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance
class InfraestructuraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infraestructuras
        fields = '__all__'

class MunicipiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipios
        fields = '__all__'  

    
    def create(self, validated_data):
        validacionesInidividualesIncercion.validacionesMunicipios.valiExiste(validated_data)
        municipio = Municipios.objects.create(
            nombre=validated_data["nombre"],
            cantidadbarrios = 0,
            estado = 1
        )
        return municipio
    def update(self, instance, validated_data):
        instance.nombre = validated_data.get("nombre", instance.nombre)
        instance.cantidadbarrios = instance.cantidadbarrios
        instance.estado = instance.estado
        instance.departamentoid = validated_data.get("departamentoid", instance.departamentoid)
        instance.save()
        return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance
class PersonasSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Personas
        fields = '__all__'  
        
        
    def create(self, validated_data):
        validacionesInidividualesIncercion.validacionesPersonas.valiExiste(validated_data)
        return ExcepcionNegocio("La accion no puede ser completada desde este punto")
    def update(self, instance, validated_data):
        instance.primernombre = validated_data.get("primernombre", instance.primernombre)
        instance.segundonombre = validated_data.get("segundonombre", instance.segundonombre)
        instance.primerapellido = validated_data.get("primerapellido", instance.primerapellido)
        instance.segundoapellido = validated_data.get("segundoapellido", instance.segundoapellido)
        instance.fechanacimiento = validacionesInidividualesIncercion.validacionesPersonas.valiFecha(validated_data.get("fechanacimiento", instance.fechanacimiento))
        instance.edad = validacionesInidividualesIncercion.validacionesPersonas.edad(validated_data.get("fechanacimiento"), instance.fechanacimiento)
        instance.sexo = validacionesInidividualesIncercion.validacionesPersonas.valiSexo(validated_data.get("sexo"), instance.sexo)
        instance.estado = instance.estado
        instance.save()
        return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance
        
class RelacionesparentescosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relacionesparentescos
        fields = '__all__'
    def create(self, validated_data):
        validacionesInidividualesIncercion.validacionesRelacionParentesco.valiExiste(validated_data)
        relacion = Relacionesparentescos.objects.create(
            relacion = validated_data["relacion"],
            estado = 1
        )
        return relacion
    def update(self, instance, validated_data):
        instance.relacion = validated_data.get("relacion", instance.relacion)
        instance.estado = instance.estado
        return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance
            
class TiposdeeducacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiposdeeducaciones
        fields = '__all__'

class TiposdeeducacionesdocentesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiposdeeducacionesdocentes
        fields = '__all__'
        
class TutoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutores
        fields = '__all__'

class TiposDePisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiposdepisos
        fields = '__all__'
        
class TiposDeTechosSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Tiposdetechos
        fields = '__all__'
        
class MaterialesDeConstruccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materialesconstrucciones
        fields = '__all__'