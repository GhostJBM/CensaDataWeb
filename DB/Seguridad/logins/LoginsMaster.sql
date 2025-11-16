USE MASTER
GO
--Login Administrador
Create LOGIN UsuarioAdministrador
WITH PASSWORD = 'Login'
	MUST_CHANGE,
	DEFAULT_DATABASE = CensaData,
	CHECK_EXPIRATION = ON
GO
--Login Invvesigador
Create LOGIN UsuarioInvestigador
WITH PASSWORD = 'Login'
	MUST_CHANGE,
	DEFAULT_DATABASE = CensaData,
	CHECK_EXPIRATION = ON
GO