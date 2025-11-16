USE CensaData
GO

CREATE ROLE Investigador
GO


USE CensaData
GO
-- todos los ro4les de Investigador
grant SELECT ON Administradores to Investigador
grant SELECT ON AñosEscolares to Investigador
grant SELECT, INSERT, UPDATE, DELETE ON AñosEscolaresDocentes to Investigador
grant SELECT ON Barrios to Investigador
grant SELECT, INSERT, UPDATE, DELETE ON Casas to Investigador
grant SELECT ON CentrosEducativos to Investigador
grant SELECT, INSERT, UPDATE, DELETE ON CentrosEducativosDocentes to Investigador
grant SELECT, INSERT, UPDATE, DELETE ON ContactosCentrosEducativos to Investigador
grant SELECT, INSERT, UPDATE, DELETE ON ContactosTutores to Investigador
grant SELECT, INSERT, UPDATE, DELETE ON ContactosInvestigadores to Investigador
grant SELECT, INSERT, UPDATE, DELETE ON ContactosDirectores to Investigador
grant SELECT, INSERT, UPDATE, DELETE ON ContactosDocentes to Investigador
grant SELECT, INSERT, UPDATE, DELETE ON CuentasInvestigadoresAdmin to Investigador
grant SELECT ON Departamentos to Investigador
grant SELECT, INSERT, UPDATE, DELETE ON Docentes to Investigador
grant SELECT, INSERT, UPDATE, DELETE ON Empadronados to Investigador
grant SELECT ON Empleos to Investigador
grant SELECT, INSERT, UPDATE, DELETE ON Encuestas to Investigador
grant SELECT, INSERT, UPDATE, DELETE ON EncuestasINIDETrabajadores to Investigador
grant SELECT, INSERT, UPDATE, DELETE ON EncuestasMINEDEscolares to Investigador
grant SELECT ON	EstadosCiviles to Investigador
grant SELECT, INSERT, UPDATE, DELETE ON Estudiantes to Investigador
grant SELECT ON Investigadores to Investigador
grant SELECT ON Municipios to Investigador
grant SELECT, INSERT, UPDATE, DELETE ON Personas to Investigador
grant SELECT ON RelacionesParentescos to Investigador
grant SELECT ON TiposDeEducaciones to Investigador
grant SELECT, INSERT, UPDATE, DELETE ON TiposDeEducacionesDocentes to Investigador
grant SELECT, INSERT, UPDATE, DELETE ON Tutores to Investigador