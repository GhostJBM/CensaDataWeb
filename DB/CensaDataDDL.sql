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
    [PrimerNombre] varchar(30),
    [SegundoNombre] varchar(30),
    [PrimerApellido] varchar(30),
    [SegundoApellido] varchar(30),
    [Edad] int,
    [Sexo] char,
    [Estado] bit,
    [CuentaId] int,
    CONSTRAINT [PK_Administradores] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[AñosEscolares] (
    [Id] int IDENTITY(1,1),
    [AñoEscolar] varchar(30),
    [TipoEducacionId] int,
    [Estado] bit,
    CONSTRAINT [PK_AñosEscolares] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[AñosEscolaresDocentes] (
    [Id] int IDENTITY(1,1),
    [DocenteId] int,
    [AñoEscolarId] int,
    [Estado] bit,
    CONSTRAINT [PK_AñosEscolaresDocentes] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Barrios] (
    [Id] int IDENTITY(1,1),
    [Nombre] varchar(30),
    [CantidadCasas] int,
    [Estado] bit,
    [MunicipioId] int,
    CONSTRAINT [PK_Barrios] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Casas] (
    [Id] int IDENTITY(1,1),
    [NumCasa] int,
    [CantidadHombres] int,
    [CantidadMujeres] int,
    [TotalPersonas] AS [CantidadHombres]+[CantidadMujeres],
    [Estado] bit,
    [BarrioId] int,
    CONSTRAINT [PK_Casas] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[CentrosEducativos] (
    [Id] int IDENTITY(1,1),
    [Nombre] varchar(30),
    [BarrioId] int,
    [Estado] bit,
    [DirectorId] int,
    CONSTRAINT [PK_CentrosEducativos] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[CentrosEducativosDocentes] (
    [Id] int IDENTITY(1,1),
    [DocenteId] int,
    [CentroEducativoId] int,
    [Estado] bit,
    CONSTRAINT [PK_CentrosEducativosDocentes] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[ContactosCentrosEducativos] (
    [Id] int IDENTITY(1,1),
    [Contacto] int,
    [CentroEducativoId] int,
    [Estado] bit,
    CONSTRAINT [PK_ContactosCentrosEducativos] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[ContactosDirectores] (
    [Id] int IDENTITY(1,1),
    [Contacto] int,
    [DirectorID] int,
    [Estado] bit,
    CONSTRAINT [PK_Contactos_Directores] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[ContactosDocentes] (
    [Id] int IDENTITY(1,1),
    [Contacto] int,
    [DocenteId] int,
    [Estado] bit,
    CONSTRAINT [PK_ContactosDocentes] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[ContactosInvestigadores] (
    [Id] int IDENTITY(1,1),
    [Contacto] int,
    [Estado] bit,
    [InvestigadorId] int,
    CONSTRAINT [PK_ContactosInvestigadores] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[ContactosTutores] (
    [Id] int IDENTITY(1,1),
    [Contacto] int,
    [TutorId] int,
    [Estado] bit,
    CONSTRAINT [PK_ContactosTutores] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[CuentasAdministradores] (
    [Id] int IDENTITY(1,1),
    [Usuario] varchar(30),
    [Contraseña] varchar(30),
    [Estado] bit,
    CONSTRAINT [PK_CuentasAdministradores] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[CuentasInvestigadores] (
    [Id] int IDENTITY(1,1),
    [usuario] varchar(30),
    [password] varchar(128),
    is_active bit default 1,
    is_staff bit default 0,
    is_superuser bit default 0,
    last_login DateTime NULL,
    [Estado] bit,
    CONSTRAINT [PK_CuentasInvestigadores] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Departamentos] (
    [Id] int IDENTITY(1,1),
    [Nombre] varchar(30),
    [CantidadMunicipios] int,
    [Estado] bit,
    CONSTRAINT [PK_Departamentos] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Directores] (
    [Id] int IDENTITY(1,1),
    [Cedula] char(14),
    [PersonaId] int,
    [Estado] bit,
    CONSTRAINT [PK_Directores] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Docentes] (
    [Id] int IDENTITY(1,1),
    [PersonaId] int,
    [Cedula] char(14),
    [Estado] bit,
    [Especialidad] varchar,
    CONSTRAINT [PK_Docentes] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[DocentesEstudiantes] (
    [Id] int IDENTITY(1,1),
    [DocenteId] int,
    [EstudianteId] int,
    [Estado] bit,
    CONSTRAINT [PK_DocentesEstudiantes] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Empadronados] (
    [Id] int IDENTITY(1,1),
    [PersonaId] int,
    [RelacionId] int,
    [EstadoCivilId] int,
    [EmpleoId] int,
    [EncuestaINIDEId] int,
    [CasaId] int,
    [Estado] bit,
    CONSTRAINT [PK_Empadronados] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Empleos] (
    [Id] int IDENTITY(1,1),
    [Empleo] varchar(30),
    [Estado] bit,
    CONSTRAINT [PK_Empleos] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Encuestas] (
    [Id] int IDENTITY(1,1),
    [Fecha] date,
    [Estado] bit,
    [InvestigadorId] int,
    CONSTRAINT [PK_Encuestas] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[EncuestasINIDETrabajadores] (
    [Id] int IDENTITY(1,1),
    [Estado] bit,
    [CasaId] int,
    [EncuestaId] int,
    CONSTRAINT [PK_EncuestasINIDETrabajadores] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[EncuestasMINEDEscolares] (
    [Id] int IDENTITY(1,1),
    [CentroEducativoId] int,
    [EncuestaId] int,
    [Estado] bit,
    CONSTRAINT [PK_EncuestasMINEDEscolares] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[EstadosCiviles] (
    [Id] int IDENTITY(1,1),
    [EstadoCivil] varchar(30),
    [Estado] bit,
    CONSTRAINT [PK_EstadosCiviles] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Estudiantes] (
    [Id] int IDENTITY(1,1),
    [PersonaId] int,
    [TipoEducacionId] int,
    [AñoEscolarId] int,
    [TutorId] int,
    [Estado] bit,
    [CodigoEstudiante] varchar(15),
    CONSTRAINT [PK_Estudiantes] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Investigadores] (
    [Id] int IDENTITY(1,1),
    [PrimerNombre] varchar(30),
    [SegundoNombre] varchar(30),
    [PrimerApellido] varchar(30),
    [SegundoApellido] varchar(30),
    [Edad] int,
    [Sexo] char,
    [Estado] bit,
    [CuentaId] int,
    CONSTRAINT [PK_Investigadores] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Municipios] (
    [Id] int IDENTITY(1,1),
    [Nombre] varchar(30),
    [CantidadBarrios] int,
    [Estado] bit,
    [DepartamentoId] int,
    CONSTRAINT [PK_Municipios] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Personas] (
    [Id] int IDENTITY(1,1),
    [PrimerNombre] varchar(30),
    [SegundoNombre] varchar(30),
    [PrimerApellido] varchar(30),
    [SegundoApellido] varchar(30),
    [FechaDeNacimiento] date,
    [Edad] int,
    [Sexo] char,
    [Estado] bit,
    CONSTRAINT [PK_Personas] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[RelacionesParentescos] (
    [Id] int IDENTITY(1,1),
    [Relacion] varchar(30),
    [Estado] bit,
    CONSTRAINT [PK_RelacionesParentescos] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[TiposDeEducaciones] (
    [Id] int IDENTITY(1,1),
    [Nombre] varchar(30),
    [CentroEducativoId] int,
    [Estado] bit,
    CONSTRAINT [PK_TiposDeEducaciones] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[TiposDeEducacionesDocentes] (
    [Id] int IDENTITY(1,1),
    [DocenteId] int,
    [TipoEducacionId] int,
    [Estado] bit,
    CONSTRAINT [PK_TiposDeEducacionesDocentes] PRIMARY KEY ([Id])
);

CREATE TABLE [dbo].[Tutores] (
    [Id] int IDENTITY(1,1),
    [PersonaId] int,
    [Cedula] char(14),
    [Estado] bit,
    CONSTRAINT [PK_Tutores] PRIMARY KEY ([Id])
);

