# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class Administradores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    primernombre = models.CharField(db_column='PrimerNombre', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    segundonombre = models.CharField(db_column='SegundoNombre', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    primerapellido = models.CharField(db_column='PrimerApellido', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='SegundoApellido', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    edad = models.IntegerField(db_column='Edad')  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    cuentaid = models.ForeignKey('Cuentasinvestigadoresadmin', models.DO_NOTHING, db_column='CuentaId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Administradores'


class Añosescolares(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    añoescolar = models.CharField(db_column='AñoEscolar', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tipoeducacionid = models.ForeignKey('Tiposdeeducaciones', models.DO_NOTHING, db_column='TipoEducacionId')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AñosEscolares'


class Añosescolaresdocentes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    docenteid = models.ForeignKey('Docentes', models.DO_NOTHING, db_column='DocenteId')  # Field name made lowercase.
    añoescolarid = models.ForeignKey(Añosescolares, models.DO_NOTHING, db_column='AñoEscolarId')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AñosEscolaresDocentes'


class Barrios(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cantidadcasas = models.IntegerField(db_column='CantidadCasas')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    municipioid = models.ForeignKey('Municipios', models.DO_NOTHING, db_column='MunicipioId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Barrios'


class Casas(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    numcasa = models.IntegerField(db_column='NumCasa', unique=True)  # Field name made lowercase.
    cantidadhombres = models.IntegerField(db_column='CantidadHombres')  # Field name made lowercase.
    cantidadmujeres = models.IntegerField(db_column='CantidadMujeres')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    infraestructuraid = models.ForeignKey('Infraestructuras', models.DO_NOTHING, db_column='InfraestructuraId')  # Field name made lowercase.
    barrioid = models.ForeignKey(Barrios, models.DO_NOTHING, db_column='BarrioId')  # Field name made lowercase.
    serviciodeagua = models.BooleanField(db_column='ServicioDeAgua', blank=True, null=True)  # Field name made lowercase.
    serviciodeenergia = models.BooleanField(db_column='ServicioDeEnergia', blank=True, null=True)  # Field name made lowercase.
    ingresofamiliar = models.DecimalField(db_column='IngresoFamiliar', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Casas'


class Censos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    nombrecenso = models.CharField(db_column='NombreCenso', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cantidadencuestados = models.IntegerField(db_column='CantidadEncuestados')  # Field name made lowercase.
    cantidadrespuestaspositivas = models.IntegerField(db_column='CantidadRespuestasPositivas')  # Field name made lowercase.
    cantidadrespuestasnegativas = models.IntegerField(db_column='CantidadRespuestasNegativas')  # Field name made lowercase.
    cantidadencuestas = models.IntegerField(db_column='CantidadEncuestas')  # Field name made lowercase.
    muestrapoblacional = models.IntegerField(db_column='MuestraPoblacional')  # Field name made lowercase.
    poblaciontotal = models.IntegerField(db_column='PoblacionTotal')  # Field name made lowercase.
    cantidadcasasencuestadas = models.IntegerField(db_column='CantidadCasasEncuestadas')  # Field name made lowercase.
    fechainiciocenso = models.DateTimeField(db_column='FechaInicioCenso')  # Field name made lowercase.
    fechafincenso = models.DateTimeField(db_column='FechaFinCenso')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Censos'


class Centroseducativos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    barrioid = models.ForeignKey(Barrios, models.DO_NOTHING, db_column='BarrioId')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    directorid = models.ForeignKey('Directores', models.DO_NOTHING, db_column='DirectorId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CentrosEducativos'


class Centroseducativosdocentes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    docenteid = models.ForeignKey('Docentes', models.DO_NOTHING, db_column='DocenteId')  # Field name made lowercase.
    centroeducativoid = models.ForeignKey(Centroseducativos, models.DO_NOTHING, db_column='CentroEducativoId')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CentrosEducativosDocentes'


class Contactoscentroseducativos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    contacto = models.IntegerField(db_column='Contacto')  # Field name made lowercase.
    centroeducativoid = models.ForeignKey(Centroseducativos, models.DO_NOTHING, db_column='CentroEducativoId')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactosCentrosEducativos'


class Contactosdirectores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    contacto = models.IntegerField(db_column='Contacto')  # Field name made lowercase.
    directorid = models.ForeignKey('Directores', models.DO_NOTHING, db_column='DirectorID')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactosDirectores'


class Contactosdocentes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    contacto = models.IntegerField(db_column='Contacto')  # Field name made lowercase.
    docenteid = models.ForeignKey('Docentes', models.DO_NOTHING, db_column='DocenteId')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactosDocentes'


class Contactosempadronados(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    contacto = models.IntegerField(db_column='Contacto')  # Field name made lowercase.
    empadronadoid = models.ForeignKey('Empadronados', models.DO_NOTHING, db_column='EmpadronadoId')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactosEmpadronados'


class Contactosinvestigadores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    contacto = models.IntegerField(db_column='Contacto')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    investigadorid = models.ForeignKey('Investigadores', models.DO_NOTHING, db_column='InvestigadorId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactosInvestigadores'


class Contactostutores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    contacto = models.IntegerField(db_column='Contacto')  # Field name made lowercase.
    tutorid = models.ForeignKey('Tutores', models.DO_NOTHING, db_column='TutorId')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContactosTutores'

class CustomInvestigadorAdminManager(BaseUserManager):
    def create_user(self, usuario, password=None, **extra_fields):
        if not usuario:
            raise ValueError('El nombre de usuario es obligatorio')
        user = self.model(usuario=usuario, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, usuario, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(usuario, password, **extra_fields)       

class Cuentasinvestigadoresadmin(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS',)
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_active = models.BooleanField(blank=True, null=True)
    is_staff = models.BooleanField(blank=True, null=True)
    is_superuser = models.BooleanField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    Role = models.CharField(db_column='Role', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    Correo = models.CharField(db_column='Correo', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS',unique=True, blank=False, null=False)  # Field name made lowercase.


    objects = CustomInvestigadorAdminManager()
    USERNAME_FIELD = 'Correo'
    REQUIRED_FIELDS = ['Role', 'usuario', 'password']
    class Meta:
        managed = False
        db_table = 'CuentasInvestigadoresAdmin'
    def __str__(self):
        return self.usuario

class Departamentos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cantidadmunicipios = models.IntegerField(db_column='CantidadMunicipios')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Departamentos'


class Directores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    cedula = models.CharField(db_column='Cedula', max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    personaid = models.ForeignKey('Personas', models.DO_NOTHING, db_column='PersonaId')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Directores'


class Discapacidades(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    discapacidad = models.CharField(db_column='Discapacidad', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Discapacidades'


class Discapacidadespersonas(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    discapacidadid = models.ForeignKey(Discapacidades, models.DO_NOTHING, db_column='DiscapacidadId')  # Field name made lowercase.
    personaid = models.ForeignKey('Personas', models.DO_NOTHING, db_column='PersonaId')  # Field name made lowercase.
    estado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DiscapacidadesPersonas'


class Docentes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    personaid = models.ForeignKey('Personas', models.DO_NOTHING, db_column='PersonaId')  # Field name made lowercase.
    cedula = models.CharField(db_column='Cedula', max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    especialidad = models.CharField(db_column='Especialidad', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Docentes'


class Docentesestudiantes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    docenteid = models.ForeignKey(Docentes, models.DO_NOTHING, db_column='DocenteId')  # Field name made lowercase.
    estudianteid = models.ForeignKey('Estudiantes', models.DO_NOTHING, db_column='EstudianteId')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DocentesEstudiantes'


class Empadronados(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    personaid = models.ForeignKey('Personas', models.DO_NOTHING, db_column='PersonaId')  # Field name made lowercase.
    relacionid = models.ForeignKey('Relacionesparentescos', models.DO_NOTHING, db_column='RelacionId')  # Field name made lowercase.
    numerocedula = models.CharField(db_column='NumeroCedula', max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    estadocivilid = models.ForeignKey('Estadosciviles', models.DO_NOTHING, db_column='EstadoCivilId')  # Field name made lowercase.
    empleoid = models.ForeignKey('Empleos', models.DO_NOTHING, db_column='EmpleoId')  # Field name made lowercase.
    casaid = models.ForeignKey(Casas, models.DO_NOTHING, db_column='CasaId')  # Field name made lowercase.
    niveleducativoid = models.ForeignKey('Niveleseducativos', models.DO_NOTHING, db_column='NivelEducativoId')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    ingresopersonal = models.DecimalField(db_column='IngresoPersonal', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Empadronados'


class Empleos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    empleo = models.CharField(db_column='Empleo', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Empleos'


class Encuestasinidetrabajadores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    casaid = models.ForeignKey(Casas, models.DO_NOTHING, db_column='CasaId')  # Field name made lowercase.
    censoid = models.ForeignKey(Censos, models.DO_NOTHING, db_column='CensoId')  # Field name made lowercase.
    investigadorid = models.ForeignKey('Investigadores', models.DO_NOTHING, db_column='InvestigadorId')  # Field name made lowercase.
    fechainicio = models.DateTimeField(db_column='FechaInicio')  # Field name made lowercase.
    fechafin = models.DateTimeField(db_column='FechaFin')  # Field name made lowercase.
    respuesta = models.CharField(db_column='Respuesta', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    totalencuestados = models.IntegerField(db_column='TotalEncuestados')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EncuestasINIDETrabajadores'


class Encuestasminedescolares(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    centroeducativoid = models.ForeignKey(Centroseducativos, models.DO_NOTHING, db_column='CentroEducativoId')  # Field name made lowercase.
    censoid = models.ForeignKey(Censos, models.DO_NOTHING, db_column='CensoId')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    investigadorid = models.ForeignKey('Investigadores', models.DO_NOTHING, db_column='InvestigadorId')  # Field name made lowercase.
    fechainicio = models.DateTimeField(db_column='FechaInicio')  # Field name made lowercase.
    fechafin = models.DateTimeField(db_column='FechaFin')  # Field name made lowercase.
    respuesta = models.CharField(db_column='Respuesta', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    totalencuestados = models.IntegerField(db_column='TotalEncuestados')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EncuestasMINEDEscolares'


class Estadosciviles(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    estadocivil = models.CharField(db_column='EstadoCivil', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EstadosCiviles'


class Estudiantes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    personaid = models.ForeignKey('Personas', models.DO_NOTHING, db_column='PersonaId')  # Field name made lowercase.
    tipoeducacionid = models.ForeignKey('Tiposdeeducaciones', models.DO_NOTHING, db_column='TipoEducacionId')  # Field name made lowercase.
    añoescolarid = models.ForeignKey(Añosescolares, models.DO_NOTHING, db_column='AñoEscolarId')  # Field name made lowercase.
    tutorid = models.ForeignKey('Tutores', models.DO_NOTHING, db_column='TutorId')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    codigoestudiante = models.CharField(db_column='CodigoEstudiante', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Estudiantes'


class Infraestructuras(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    materialcontruccionid = models.ForeignKey('Materialesconstrucciones', models.DO_NOTHING, db_column='MaterialContruccionId')  # Field name made lowercase.
    tipodetechoid = models.ForeignKey('Tiposdetechos', models.DO_NOTHING, db_column='TipoDeTechoId')  # Field name made lowercase.
    tipodepisoid = models.ForeignKey('Tiposdepisos', models.DO_NOTHING, db_column='TipoDePisoId')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Infraestructuras'


class Investigadores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    primernombre = models.CharField(db_column='PrimerNombre', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    segundonombre = models.CharField(db_column='SegundoNombre', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='PrimerApellido', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='SegundoApellido', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    edad = models.IntegerField(db_column='Edad')  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    cuentaid = models.ForeignKey(Cuentasinvestigadoresadmin, models.DO_NOTHING, db_column='CuentaId', unique=True)  # Field name made lowercase.
    administradorid = models.ForeignKey(Administradores, models.DO_NOTHING, db_column='AdministradorId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Investigadores'


class Materialesconstrucciones(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    materialcontruccion = models.CharField(db_column='MaterialContruccion', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    estado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MaterialesConstrucciones'


class Municipios(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cantidadbarrios = models.IntegerField(db_column='CantidadBarrios')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    departamentoid = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='DepartamentoId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Municipios'


class Niveleseducativos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    niveleducativo = models.CharField(db_column='NivelEducativo', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    grado = models.IntegerField(db_column='Grado', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NivelesEducativos'


class Personas(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    primernombre = models.CharField(db_column='PrimerNombre', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    segundonombre = models.CharField(db_column='SegundoNombre', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='PrimerApellido', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='SegundoApellido', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fechadenacimiento = models.DateField(db_column='FechaDeNacimiento')  # Field name made lowercase.
    edad = models.IntegerField(db_column='Edad')  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Personas'


class Relacionesparentescos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    relacion = models.CharField(db_column='Relacion', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelacionesParentescos'


class Reportes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tiporeporte = models.CharField(db_column='TipoReporte', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    espublico = models.BooleanField(db_column='EsPublico', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(blank=True, null=True)
    administradorid = models.ForeignKey(Administradores, models.DO_NOTHING, db_column='AdministradorId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reportes'


class Tiposdeeducaciones(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    centroeducativoid = models.ForeignKey(Centroseducativos, models.DO_NOTHING, db_column='CentroEducativoId')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TiposDeEducaciones'


class Tiposdeeducacionesdocentes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    docenteid = models.ForeignKey(Docentes, models.DO_NOTHING, db_column='DocenteId')  # Field name made lowercase.
    tipoeducacionid = models.ForeignKey(Tiposdeeducaciones, models.DO_NOTHING, db_column='TipoEducacionId')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TiposDeEducacionesDocentes'


class Tiposdepisos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tipopiso = models.CharField(db_column='TipoPiso', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    estado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TiposDePisos'


class Tiposdetechos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tipodetecho = models.CharField(db_column='TipoDeTecho', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    estado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TiposDeTechos'


class Tutores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    personaid = models.ForeignKey(Personas, models.DO_NOTHING, db_column='PersonaId')  # Field name made lowercase.
    cedula = models.CharField(db_column='Cedula', max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tutores'
        
