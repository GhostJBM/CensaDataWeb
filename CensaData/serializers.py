from rest_framework import serializers
from .models import *
from CensaData.services import *
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
        instance.municipioid = validated_data.get("municipioid", instance.municipioid)
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
    def update(self, instance, validated_data):
        instance.numcasa = validated_data.get("numcasa", instance.numcasa)
        instance.cantidaddehombres = validated_data.get("cantidadhombres", instance.cantidadhombres)
        instance.cantidaddemujeres = validated_data.get("cantidadmujeres", instance.cantidadmujeres)
        instance.estado = instance.estado
        instance.barrioid = validated_data.get("barrioid", instance.barrioid)
        instance.infraestructuraid = validated_data.get("infraestructuraid", instance.infraestructuraid)
        instance.ingresofamiliar = validated_data.get("ingresofamiliar", instance.ingresofamiliar)
        instance.serviciodeagua = validated_data.get("serviciodeagua", instance.serviciodeagua)
        instance.serviciodeenergia = validated_data.get("serviciodeenergia", instance.serviciodeenergia)
        instance.save()
        return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance
        
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
   
    def create(self, validated_data):
        validacionesInidividualesIncercion.ValidacionesInvestigadoresAdmin.contantoExistente(validated_data)
        contacto = Contactosinvestigadores.objects.create(
            contacto = validated_data["contacto"],
            investigadorid = validated_data["investigadorid"],
            estado = 1
        )
        return contacto
    def update(self, instance, validated_data):
        instance.contacto = validated_data.get("contacto", instance.contacto)
        instance.investigadorid = validated_data.get("investigadorid", instance.investigadorid)
        instance.estado = instance.estado
        instance.save()
        return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance
class ContactosEmpadronadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactosempadronados 
        fields = '__all__'

    def create(self, validated_data): 
        validacionesInidividualesIncercion.validacionesIndividualesEmpadronados.valiExisteContato(validated_data)
        contacto = Contactosempadronados.objects.create(
            contacto = validated_data["contacto"],
            empadronadoid = validated_data["empadronadoid"],
            estado = 1
        )
        return contacto
    def update(self, instance, validated_data):
        instance.contacto = validated_data.get("contacto", instance.contacto)
        instance.empadronadoid = validated_data.get("empadronadoid", instance.empadronadoid)
        instance.estado = instance.estado
        instance.save()
        return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance
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
            empleo = validated_data["empleo"],
            estado  = 1
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
    def update(self, instance, validated_data):
        instance.nombrecenso = validated_data.get("nombrecenso", instance.nombrecenso)
        instance.cantidadencuestados = validated_data.get("cantidadencuestados", instance.cantidadencuestados)
        instance.cantidadrespuestaspositivas = validated_data.get("cantidadrespuestaspositivas", instance.cantidadrespuestaspositivas)
        instance.cantidadrespuestasnegativas = validated_data.get("cantidadrespuestasnegativas", instance.cantidadrespuestasnegativas)
        instance.cantidadencuestas = validated_data.get("cantidadencuestas", instance.cantidadencuestas)
        instance.muestrapoblacional = validated_data.get("muestrapoblacional", instance.muestrapoblacional)
        instance.poblaciontotal = validated_data.get("poblaciontotal", instance.poblaciontotal)
        instance.cantidadcasasencuestadas = validated_data.get("cantidadcasasencuestadas", instance.cantidadcasasencuestadas)
        instance.fechainiciocenso = instance.fechainiciocenso
        instance.fechafincenso = validated_data.get("fechafincenso", instance.fechafincenso)
        instance.save()
        return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance
class EncuestasinidetrabajadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encuestasinidetrabajadores
        fields = '__all__'
    def update(self, instance, validated_data):
        instance.casaid = validated_data.get("casaid", instance.casaid)
        instance.censoid = validated_data.get("censoid", instance.censoid)
        instance.investigadorid = validated_data.get("investigadorid", instance.investigadorid)
        instance.fechainicio = instance.fechainicio
        instance.fechafin = validated_data.get("fechafin", instance.fechafin)
        instance.respuesta = instance.respuesta
        instance.totalencuestados = instance.totalencuestados
        instance.save()
        return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance
        
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
            niveleducativo = validated_data["niveleducativo"],
            grado = validated_data["grado"],
            estado = 1
        ) 
        return nivel
    def update(self, instance, validated_data):
        instance.niveleducativo = validated_data.get("niveleducativo", instance.niveleducativo)
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
    def create(self, validated_data):
        departamento = Infraestructuras.objects.create(
            materialcontruccionid = validated_data["materialcontruccionid"],
            tipodetechoid = validated_data["tipodetechoid"],
            tipodepisoid = validated_data["tipodepisoid"],
            estado = 1
        )
        return departamento
    def update(self, instance, validated_data):
        instance.nombrematerialcontruccionid = validated_data.get("materialcontruccionid", instance.materialcontruccionid)
        instance.tipodetechoid = validated_data.get("tipodetechoid", instance.tipodetechoid)
        instance.estado = instance.estado
        instance.tipodepisoid = validated_data.get("tipodepisoid", instance.tipodepisoid)
        instance.save()
        return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance

class MunicipiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipios
        fields = '__all__'  

    
    def create(self, validated_data):
        validacionesInidividualesIncercion.validacionesMunicipios.valiExiste(validated_data)
        municipio = Municipios.objects.create(
            nombre=validated_data["nombre"],
            cantidadbarrios = 0,
            departamentoid = validated_data["departamentoid"],
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
    def create(self, validated_data):
        validacionesInidividualesIncercion.validacionesInfraestructura.tipodepiso.existe(validated_data)
        tipopiso = Tiposdepisos.objects.create(
            tipopiso = validated_data["tipopiso"],
            estado = 1
        )
        return tipopiso
    def update(self, instance, validated_data):
        instance.tipopiso = validated_data.get("tipopiso", instance.tipopiso)
        instance.estado = instance.estado
        instance.save()
        return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance
        
class TiposDeTechosSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Tiposdetechos
        fields = '__all__'
    def create(self, validated_data):
        validacionesInidividualesIncercion.validacionesInfraestructura.tipodetecho.existe(validated_data)
        tipotecho = Tiposdetechos.objects.create(
            tipodetecho = validated_data["tipodetecho"],
            estado = 1
        )
        return tipotecho
    def update(self, instance, validated_data):
        instance.tipotecho = validated_data.get("tipodetecho", instance.tipotecho)
        instance.estado = instance.estado
        instance.save()
        return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance
        
class MaterialesDeConstruccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materialesconstrucciones
        fields = '__all__'
    def create(self, validated_data):
        validacionesInidividualesIncercion.validacionesInfraestructura.materialesContruccion.existe(validated_data)
        material =  Materialesconstrucciones.objects.create(
           materialcontruccion = validated_data["materialcontruccion"],
           estado = 1 
        )  
        return material
    def update(self, instance, validated_data):
        instance.materialcontruccion = validated_data["materialcontruccion", instance.materialcontruccion]
        instance.estado = instance.estado
        instance.save()
        return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance

class discapacidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discapacidades
        fields = "__all__"
    def create(self, validated_data):
        validacionesInidividualesIncercion.validacionesDiscapacidades.valiExiste(validated_data)
        discapacidad = Discapacidades.objects.create(
            discapacidad = validated_data["discapacidad"],
            estado = 1
        )
        return discapacidad
    def update(self, instance, validated_data):
        instance.discapacidad = validated_data.get("discapacidad")
        instance.estado = instance.estado
        instance.save()
        return instance
    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance

class discapacidadesPersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discapacidadespersonas
        fields="__all__"
    def create(self, validated_data):
        validacionesInidividualesIncercion.ValidacionesDiscapacidades.DiscPersonExiste(validated_data)
        DiscPerson = Discapacidadespersonas.objects.create(
            discapacidadid = validated_data["discapacidadid"],
            personaid = validated_data["personaid"],
            estado = 1
        )
        return DiscPerson
    def update(self, instance, validated_data):
        instance.discapacidadid = validated_data.get("discapacidadid", instance.discapacidadid)
        instance.personaid = validated_data.get("personaid", instance.personaid)
        validacionesInidividualesIncercion.ValidacionesDiscapacidadesPersona.DiscPersonExiste(instance)
        return instance


    def delete(self, instance):
        instance.estado = 0
        instance.save()
        return instance