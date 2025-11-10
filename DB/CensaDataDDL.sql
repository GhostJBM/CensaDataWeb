USE master
GO

CREATE DATABASE [CensaData]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'CensaData_Data', FILENAME = N'C:\DB2025\CensaData_data.mdf' , SIZE = 8192KB , MAXSIZE = 102400KB , FILEGROWTH = 2048KB )
 LOG ON 
( NAME = N'CensaData_Log', FILENAME = N'C:\DB2025\CensaData_Log.ldf' , SIZE = 5120KB , MAXSIZE = 102400KB , FILEGROWTH = 2048KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
USE CensaData
GO

CREATE TABLE [dbo].[Administradores] (
    [Id] int IDENTITY(1,1),
    [PrimerNombre] varchar(30) NOT NULL,
    [SegundoNombre] varchar(30)NOT NULL,
    [PrimerApellido] varchar(30)NOT NULL,
    [SegundoApellido] varchar(30)NOT NULL,
    [Edad] int NOT NULL Constraint CK_AdministradorEdad CHECK(Edad > 17 ),
    [Sexo] char NOT NULL,
    [Estado] bit default 1,
    [CuentaId] int NOT NULL Constraint FK_CuentasInvestigadoresAdmin_Administrador Foreign Key References dbo.CuentasInvestigadoresAdmin(id),
    CONSTRAINT [PK_Administradores] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[AñosEscolares] (
    [Id] int IDENTITY(1,1) ,
    [AñoEscolar] varchar(30) NOT NULL,
    [TipoEducacionId] int NOT NULL Constraint FK_TiposDeEducaciones_AñosEscolares Foreign Key References dbo.TiposDeEducaciones(id),
    [Estado] bit default 1,
    CONSTRAINT [PK_AñosEscolares] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[AñosEscolaresDocentes] (
    [Id] int IDENTITY(1,1) NOT NULL,
    [DocenteId] int NOT NULL Constraint FK_Docentes_AñosEscolaresDocentes Foreign Key References dbo.Docentes(id),
    [AñoEscolarId] int NOT NULL Constraint FK_AñosEscolares_AñosEscolaresDocentes Foreign Key References dbo.AñosEscolares(id),
    [Estado] bit default 1,
    CONSTRAINT [PK_AñosEscolaresDocentes] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Barrios] (
    [Id] int IDENTITY(1,1),
    [Nombre] varchar(30) NOT NULL,
    [CantidadCasas] int NOT NULL,
    [Estado] bit default 1,
    [MunicipioId] int NOT NULL Constraint FK_Municipios_Barrios Foreign Key References dbo.Municipios(id),
    CONSTRAINT [PK_Barrios] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Casas] (
    [Id] int IDENTITY(1,1),
    [NumCasa] int NOT NULL,
    [CantidadHombres] int NOT NULL,
    [CantidadMujeres] int NOT  NULL,
    [TotalPersonas] AS [CantidadHombres]+[CantidadMujeres],
    [Estado] bit default 1,
    [BarrioId] int NOT NULL Constraint FK_Barrios_Casas Foreign Key References dbo.Barrios(id),
    CONSTRAINT [PK_Casas] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[CentrosEducativos] (
    [Id] int IDENTITY(1,1),
    [Nombre] varchar(30) NOT NULL,
    [BarrioId] int NOT NULL Constraint FK_Barrios_CentrosEducativos Foreign Key References dbo.Barrios(id),
    [Estado] bit default 1,
    [DirectorId] int NOT NULL Constraint FK_Directores_CentrosEducativos Foreign Key References dbo.Directores(id),
    CONSTRAINT [PK_CentrosEducativos] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[CentrosEducativosDocentes] (
    [Id] int IDENTITY(1,1),
    [DocenteId] int NOT NULL Constraint FK_Docentes_CentrosEducativosDocentes Foreign Key References dbo.Docentes(id),
    [CentroEducativoId] int NOT NULL Constraint FK_CentrosEducativos_CentrosEducativosDocentes Foreign Key References dbo.CentrosEducativos(id),
    [Estado] bit default 1,
    CONSTRAINT [PK_CentrosEducativosDocentes] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[ContactosCentrosEducativos] (
    [Id] int IDENTITY(1,1),
    [Contacto] int NOT NULL,
    [CentroEducativoId] int NOT NULL Constraint FK_CentrosEducativos_Contactos Foreign Key References dbo.CentrosEducativos(id),
    [Estado] bit default 1,
    CONSTRAINT [PK_ContactosCentrosEducativos] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[ContactosDirectores] (
    [Id] int IDENTITY(1,1),
    [Contacto] int NOT NULL,
    [DirectorID] int NOT NULL Constraint FK_Directores_Contactos Foreign Key References dbo.Directores(id),
    [Estado] bit default 1,
    CONSTRAINT [PK_Contactos_Directores] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[ContactosDocentes] (
    [Id] int IDENTITY(1,1),
    [Contacto] int NOT NULL,
    [DocenteId] int NOT NULL Constraint FK_Docentes_Contactos Foreign Key References dbo.Docentes(id),
    [Estado] bit default 1,
    CONSTRAINT [PK_ContactosDocentes] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[ContactosInvestigadores] (
    [Id] int IDENTITY(1,1),
    [Contacto] int NOT NULL,
    [Estado] bit default 1,
    [InvestigadorId] int  NOT NULL Constraint FK_Investigadores_Contactos Foreign Key References dbo.Investigadores(id),
    CONSTRAINT [PK_ContactosInvestigadores] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[ContactosTutores] (
    [Id] int IDENTITY(1,1),
    [Contacto] int NOT NULL,
    [TutorId] int NOT NULL Constraint FK_Tutores_Contactos Foreign Key References dbo.Tutores(id),
    [Estado] bit default 1,
    CONSTRAINT [PK_ContactosTutores] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[CuentasInvestigadoresAdmin] (
    [Id] int IDENTITY(1,1),
    [usuario] varchar(30) NOT NULL,
    [password] varchar(128) NOT NULL,
    is_active bit default 1,
    is_staff bit default 0,
    is_superuser bit default 0,
    last_login DateTime NULL,
    [Estado] bit default 1,
    Role varchar(30) NOT NULL,
    CONSTRAINT [PK_CuentasInvestigadoresAdmin] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Departamentos] (
    [Id] int IDENTITY(1,1),
    [Nombre] varchar(30) NOT NULL,
    [CantidadMunicipios] int NOT NULL,
    [Estado] bit default 1,
    CONSTRAINT [PK_Departamentos] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Directores] (
    [Id] int IDENTITY(1,1),
    [Cedula] char(14) NOT NULL,
    [PersonaId] int NOT NULL Constraint FK_Personas_Directores Foreign Key References dbo.Personas(id),
    [Estado] bit default 1,
    CONSTRAINT [PK_Directores] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Docentes] (
    [Id] int IDENTITY(1,1),
    [PersonaId] int NOT NULL Constraint FK_Personas_Docentes Foreign Key References dbo.Personas(id),
    [Cedula] char(14) NOT NULL,
    [Estado] bit default 1,
    [Especialidad] varchar(100) NOT NULL,
    CONSTRAINT [PK_Docentes] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[DocentesEstudiantes] (
    [Id] int IDENTITY(1,1),
    [DocenteId] int NOT NULL Constraint FK_Docentes_DocentesEstudiantes Foreign Key References dbo.Docentes(id),
    [EstudianteId] int NOT NULL Constraint FK_Personas_Empadronados Foreign Key References dbo.Personas(id),
    [Estado] bit default 1,
    CONSTRAINT [PK_DocentesEstudiantes] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Empadronados] (
    [Id] int IDENTITY(1,1),
    [PersonaId] int NOT NULL Constraint FK_Personas_Empadronados Foreign Key References dbo.Personas(id),
    [RelacionId] int NOT NULL Constraint FK_Relaciones_Empadronados Foreign Key References dbo.RelacionesParentescos(id),
    [EstadoCivilId] int NOT NULL Constraint FK_EstadosCiviles_Empadronados Foreign Key References dbo.EstadosCiviles(id),
    [EmpleoId] int NOT NULL Constraint FK_Empleos_Empadronados Foreign Key References dbo.Empleos(id),
    [CasaId] int NOT NULL Constraint FK_Casas_Empadronados Foreign Key References dbo.Casas(id),
    [Estado] bit default 1,
    CONSTRAINT [PK_Empadronados] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Empleos] (
    [Id] int IDENTITY(1,1),
    [Empleo] varchar(30) NOT NULL,
    [Estado] bit default 1,
    CONSTRAINT [PK_Empleos] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Encuestas] (
    [Id] int IDENTITY(1,1),
    [Fecha] date NOT NULL,
    [Estado] bit default 1,
    [InvestigadorId] int NOT NULL Constraint FK_Investigadores_Encuestas Foreign Key References dbo.Investigadores(id),
    CONSTRAINT [PK_Encuestas] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[EncuestasINIDETrabajadores] (
    [Id] int IDENTITY(1,1),
    [Estado] bit default 1,
    [CasaId] int NOT NULL Constraint FK_Casas_EncuestasINIDETrabajadores Foreign Key References dbo.Casas(id),
    [EncuestaId] int NOT NULL Constraint FK_Encuestas_EncuestasINIDETrabajadores Foreign Key References dbo.Encuestas(id),
    CONSTRAINT [PK_EncuestasINIDETrabajadores] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[EncuestasMINEDEscolares] (
    [Id] int IDENTITY(1,1),
    [CentroEducativoId] int NOT NULL Constraint FK_CentrosEducativos_EncuestasMINEDEscolares Foreign Key References dbo.CentrosEducativos(id),
    [EncuestaId] int NOT NULL Constraint FK_Encuestas_EncuestasMINEDEscolares Foreign Key References dbo.Encuestas(id),
    [Estado] bit default 1,
    CONSTRAINT [PK_EncuestasMINEDEscolares] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[EstadosCiviles] (
    [Id] int IDENTITY(1,1),
    [EstadoCivil] varchar(30) NOT NULL,
    [Estado] bit default 1,
    CONSTRAINT [PK_EstadosCiviles] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Estudiantes] (
    [Id] int IDENTITY(1,1),
    [PersonaId] int NOT NULL Constraint FK_Personas_Estudiantes Foreign Key References dbo.Personas(id),
    [TipoEducacionId] int NOT NULL Constraint FK_TiposDeEducaciones_Estudiantes Foreign Key References dbo.TiposDeEducaciones(id),
    [AñoEscolarId] int NOT NULL Constraint FK_AñosEscolares_Estudiantes Foreign Key References dbo.AñosEscolares(id),
    [TutorId] int NOT NULL Constraint FK_Tutores_Estudiantes Foreign Key References dbo.Tutores(id),
    [Estado] bit default 1,
    [CodigoEstudiante] varchar(15) NOT NULL,
    CONSTRAINT [PK_Estudiantes] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Investigadores] (
    [Id] int IDENTITY(1,1),
    [PrimerNombre] varchar(30) NOT NULL,
    [SegundoNombre] varchar(30) NULL,
    [PrimerApellido] varchar(30)NOT NULL,
    [SegundoApellido] varchar(30) NULL,
    [Edad] int NOT NULL Constraint CK_InvestigadorEdad CHECK(Edad > 17 ),
    [Sexo] char NOT NULL,
    [Estado] bit default 1,
    [CuentaId] int NOT NULL Constraint FK_CuentasInvestigadoresAdmin_Investigadores Foreign Key References dbo.CuentasInvestigadoresAdmin(id),
    CONSTRAINT [PK_Investigadores] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Municipios] (
    [Id] int IDENTITY(1,1),
    [Nombre] varchar(30) NOT NULL,
    [CantidadBarrios] int NOT NULL,
    [Estado] bit default 1,
    [DepartamentoId] int NOT NULL Constraint FK_Departamentos_Municipios Foreign Key References dbo.Departamentos(id),
    CONSTRAINT [PK_Municipios] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Personas] (
    [Id] int IDENTITY(1,1),
    [PrimerNombre] varchar(30) NOT NULL,
    [SegundoNombre] varchar(30) NULL,
    [PrimerApellido] varchar(30) NOT NULL,
    [SegundoApellido] varchar(30) NULL,
    [FechaDeNacimiento] date NOT NULL,
    [Edad] int NOT NULL Constraint CK_PersonaEdad CHECK(Edad> 0 ),
    [Sexo] char NOT NULL,
    [Estado] bit default 1,
    CONSTRAINT [PK_Personas] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[RelacionesParentescos] (
    [Id] int IDENTITY(1,1),
    [Relacion] varchar(30) NOT NULL,
    [Estado] bit default 1,
    CONSTRAINT [PK_RelacionesParentescos] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[TiposDeEducaciones] (
    [Id] int IDENTITY(1,1),
    [Nombre] varchar(30) NOT NULL,
    [CentroEducativoId] int NOT NULL Constraint FK_CentrosEducativos_TiposEducaciones Foreign Key References dbo.CentrosEducativos(id),
    [Estado] bit default 1,
    CONSTRAINT [PK_TiposDeEducaciones] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[TiposDeEducacionesDocentes] (
    [Id] int IDENTITY(1,1),
    [DocenteId] int NOT NULL Constraint FK_Docentes_TiposEduacionesDocentes Foreign Key References dbo.Docentes(id),
    [TipoEducacionId] int NOT NULL Constraint FK_TiposDeEduaciones_TiposEduacionesDocentes Foreign Key References dbo.TiposDeEducaciones(id),
    [Estado] bit default 1,
    CONSTRAINT [PK_TiposDeEducacionesDocentes] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Tutores] (
    [Id] int IDENTITY(1,1),
    [PersonaId] int NOT NULL Constraint FK_Personas_Tutores Foreign Key References dbo.Personas(id),
    [Cedula] char(14) NOT NULL,
    [Estado] bit default 1,
    CONSTRAINT [PK_Tutores] PRIMARY KEY ([Id])
);

