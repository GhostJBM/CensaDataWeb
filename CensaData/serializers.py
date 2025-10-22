from rest_framework import serializers
from .models import Añosescolares, Añosescolaresdocentes, Administradores, Barrios,Casas,Centroseducativos,Centroseducativosdocentes,Contactoscentroseducativos,Contactosdirectores,Contactosdocentes,Contactosinvestigadores,Contactostutores,Cuentasadministradores,Cuentasinvestigadores, Departamentos,Directores,Docentes,Docentesestudiantes,Empadronados,Empleos,Encuestas,Encuestasinidetrabajadores,Encuestasminedescolares,Estadosciviles,Estudiantes,Investigadores,Municipios,Personas,Relacionesparentescos,Tiposdeeducaciones,Tiposdeeducacionesdocentes,Tutores


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
        fields = ('id', 'primernombre','segundonombre','primerapellido', 'segundoapellido','edad','sexo','estado','cuentaid')
        read_only_fields = ('id', 'cuentaid')
        
class BarriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrios
        fields = '__all__'

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
        
class CuentasadministradoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuentasadministradores
        fields = ('id','usuario','estado')
        read_only_fields = ('id')
        
class CuentasinvestigadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuentasinvestigadores
        fields = ('id','usuario','estado')
        read_only_fields = ('id')

class DepartamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamentos
        fields = '__all__'
        
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
        
class EmpleosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleos
        fields = '__all__'  
        
class EncuestasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encuestas
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
        
class EstudiantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiantes
        fields = '__all__'
        
class InvestigadoresSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Investigadores
        fields = ('id','primernombre','segundonombre', 'primerapellido','segundoapellido','edad','sexo','estado','cuentaid')
        read_only_fields = ('id','cuentaid')

class MunicipiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipios
        fields = '__all__'  
        
class PersonasSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Personas
        fields = '__all__'  
        
class RelacionesparentescosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relacionesparentescos
        fields = '__all__'
        
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
