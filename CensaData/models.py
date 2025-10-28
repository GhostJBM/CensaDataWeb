# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _


## Modelos de autentificacion
class InvestigadorManager(BaseUserManager):
    def create_user(self, usuario, password=None, **extra_fields):
        """Create and save a regular user with the given usuario and password."""
        if not usuario:
            raise ValueError('User is required')
        user = self.model(usuario=usuario, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class  AdministradorManager(BaseUserManager):
    def create_user(self, user, password, **extra_fields):
        if not user:
            raise ValueError('User is required')
        Administrador = self.model(usuario=self(user), **extra_fields)
        Administrador.set_password(password)
        Administrador.save(using=self._db)
        return 

## Modelos de la base de datos
class Administradores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    primernombre = models.CharField(db_column='PrimerNombre', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    segundonombre = models.CharField(db_column='SegundoNombre', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='PrimerApellido', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='SegundoApellido', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    edad = models.IntegerField(db_column='Edad', blank=True, null=True)  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    cuentaid = models.IntegerField(db_column='CuentaId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Administradores'


class Añosescolares(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    añoescolar = models.CharField(db_column='A�oEscolar', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipoeducacionid = models.IntegerField(db_column='TipoEducacionId', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AñosEscolares'


class Añosescolaresdocentes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    docenteid = models.IntegerField(db_column='DocenteId', blank=True, null=True)  # Field name made lowercase.
    añoescolarid = models.IntegerField(db_column='A�oEscolarId', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AñosEscolaresDocentes'


class Barrios(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cantidadcasas = models.IntegerField(db_column='CantidadCasas', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    municipioid = models.IntegerField(db_column='MunicipioId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Barrios'


class Casas(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numcasa = models.IntegerField(db_column='NumCasa', blank=True, null=True)  # Field name made lowercase.
    cantidadhombres = models.IntegerField(db_column='CantidadHombres', blank=True, null=True)  # Field name made lowercase.
    cantidadmujeres = models.IntegerField(db_column='CantidadMujeres', blank=True, null=True)  # Field name made lowercase.
    totalpersonas = models.IntegerField(db_column='TotalPersonas', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    barrioid = models.IntegerField(db_column='BarrioId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Casas'


class Centroseducativos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    barrioid = models.CharField(db_column='BarrioId', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    directorid = models.IntegerField(db_column='DirectorId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CentrosEducativos'


class Centroseducativosdocentes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    docenteid = models.IntegerField(db_column='DocenteId', blank=True, null=True)  # Field name made lowercase.
    centroeducativoid = models.IntegerField(db_column='CentroEducativoId', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CentrosEducativosDocentes'


class Contactoscentroseducativos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    contacto = models.IntegerField(db_column='Contacto', blank=True, null=True)  # Field name made lowercase.
    centroeducativoid = models.IntegerField(db_column='CentroEducativoId', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactosCentrosEducativos'


class Contactosdirectores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    contacto = models.IntegerField(db_column='Contacto', blank=True, null=True)  # Field name made lowercase.
    directorid = models.IntegerField(db_column='DirectorID', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactosDirectores'


class Contactosdocentes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    contacto = models.IntegerField(db_column='Contacto', blank=True, null=True)  # Field name made lowercase.
    docenteid = models.IntegerField(db_column='DocenteId', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactosDocentes'


class Contactosinvestigadores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    contacto = models.IntegerField(db_column='Contacto', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    investigadorid = models.IntegerField(db_column='InvestigadorId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactosInvestigadores'


class Contactostutores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    contacto = models.IntegerField(db_column='Contacto', blank=True, null=True)  # Field name made lowercase.
    tutorid = models.IntegerField(db_column='TutorId', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactosTutores'


class Cuentasadministradores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS',  blank=False, null=False)  # Field name made lowercase.
    contraseña = models.CharField(db_column='Contraseña', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CuentasAdministradores'


class Cuentasinvestigadores(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', unique=True, blank=False, null=False)  # Field name made lowercase.
    contraseña = models.CharField(db_column='Contraseña', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CuentasInvestigadores'
    
    prg_validacion = models.CharField(max_length=128, null=False)
    rp_validacion = models.CharField(max_length=128, null=False)
    # Si hay un campo numérico de estado distinto al booleano original, mantener nombre diferente
    estado_code = models.SmallIntegerField(null=False, default=1) # Asumimos un default

    # Campos requeridos por AbstractBaseUser / PermissionsMixin
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # Definición de campos para autenticación
    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = []

    objects = InvestigadorManager()

    def __str__(self):
        return str(self.usuario)

    @property
    def is_anonymous(self):
        """Required by some parts of Django auth: anonymous users have True, normal users False."""
        return False



class Departamentos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cantidadmunicipios = models.IntegerField(db_column='CantidadMunicipios', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Departamentos'


class Directores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    cedula = models.CharField(db_column='Cedula', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    personaid = models.IntegerField(db_column='PersonaId', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Directores'


class Docentes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    personaid = models.IntegerField(db_column='PersonaId', blank=True, null=True)  # Field name made lowercase.
    cedula = models.CharField(db_column='Cedula', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    especialidad = models.CharField(db_column='Especialidad', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Docentes'


class Docentesestudiantes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    docenteid = models.IntegerField(db_column='DocenteId', blank=True, null=True)  # Field name made lowercase.
    estudianteid = models.IntegerField(db_column='EstudianteId', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DocentesEstudiantes'


class Empadronados(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    personaid = models.IntegerField(db_column='PersonaId', blank=True, null=True)  # Field name made lowercase.
    relacionid = models.IntegerField(db_column='RelacionId', blank=True, null=True)  # Field name made lowercase.
    estadocivilid = models.IntegerField(db_column='EstadoCivilId', blank=True, null=True)  # Field name made lowercase.
    empleoid = models.IntegerField(db_column='EmpleoId', blank=True, null=True)  # Field name made lowercase.
    encuestainideid = models.IntegerField(db_column='EncuestaINIDEId', blank=True, null=True)  # Field name made lowercase.
    casaid = models.IntegerField(db_column='CasaId', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Empadronados'


class Empleos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    empleo = models.CharField(db_column='Empleo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Empleos'


class Encuestas(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    investigadorid = models.IntegerField(db_column='InvestigadorId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Encuestas'


class Encuestasinidetrabajadores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    casaid = models.IntegerField(db_column='CasaId', blank=True, null=True)  # Field name made lowercase.
    encuestaid = models.IntegerField(db_column='EncuestaId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EncuestasINIDETrabajadores'


class Encuestasminedescolares(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    centroeducativoid = models.IntegerField(db_column='CentroEducativoId', blank=True, null=True)  # Field name made lowercase.
    encuestaid = models.IntegerField(db_column='EncuestaId', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EncuestasMINEDEscolares'


class Estadosciviles(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    estadocivil = models.CharField(db_column='EstadoCivil', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EstadosCiviles'


class Estudiantes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    personaid = models.IntegerField(db_column='PersonaId', blank=True, null=True)  # Field name made lowercase.
    tipoeducacionid = models.IntegerField(db_column='TipoEducacionId', blank=True, null=True)  # Field name made lowercase.
    añoescolarid = models.IntegerField(db_column='A�oEscolarId', blank=True, null=True)  # Field name made lowercase.
    tutorid = models.IntegerField(db_column='TutorId', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    codigoestudiante = models.CharField(db_column='CodigoEstudiante', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Estudiantes'


class Investigadores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    primernombre = models.CharField(db_column='PrimerNombre', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    segundonombre = models.CharField(db_column='SegundoNombre', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='PrimerApellido', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='SegundoApellido', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    edad = models.IntegerField(db_column='Edad', blank=True, null=True)  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    cuentaid = models.IntegerField(db_column='CuentaId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Investigadores'
   

class Municipios(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cantidadbarrios = models.IntegerField(db_column='CantidadBarrios', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    departamentoid = models.IntegerField(db_column='DepartamentoId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Municipios'


class Personas(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    primernombre = models.CharField(db_column='PrimerNombre', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    segundonombre = models.CharField(db_column='SegundoNombre', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='PrimerApellido', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='SegundoApellido', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fechadenacimiento = models.DateField(db_column='FechaDeNacimiento', blank=True, null=True)  # Field name made lowercase.
    edad = models.IntegerField(db_column='Edad', blank=True, null=True)  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Personas'


class Relacionesparentescos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    relacion = models.CharField(db_column='Relacion', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelacionesParentescos'


class Tiposdeeducaciones(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    centroeducativoid = models.IntegerField(db_column='CentroEducativoId', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TiposDeEducaciones'


class Tiposdeeducacionesdocentes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    docenteid = models.IntegerField(db_column='DocenteId', blank=True, null=True)  # Field name made lowercase.
    tipoeducacionid = models.IntegerField(db_column='TipoEducacionId', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TiposDeEducacionesDocentes'


class Tutores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    personaid = models.IntegerField(db_column='PersonaId', blank=True, null=True)  # Field name made lowercase.
    cedula = models.CharField(db_column='Cedula', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tutores'
