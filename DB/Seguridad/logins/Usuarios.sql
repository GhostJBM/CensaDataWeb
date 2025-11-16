USE CensaData
GO

CREATE USER UserAdministrador FOR LOGIN UsuarioAdministrador
ALTER ROLE Administrador ADD MEMBER UserAdministrador
GO


CREATE USER UserInvestigador FOR LOGIN UsuarioInvestigador
ALTER ROLE Investigador ADD MEMBER UserInvestigador
GO