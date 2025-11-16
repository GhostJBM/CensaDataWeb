
USE CensaData
GO

--Todos estos triggers son para el control de cuando se hace un cambio en la base de datos de uno de las siguientes tablas

--Sumar un registro a la cantidad
CREATE TRIGGER TRG_Sumar_Municipio
ON dbo.Municipios
AFTER INSERT
AS
BEGIN
	UPDATE Departamentos
	SET CantidadMunicipios = CantidadMunicipios + 1
	WHERE Id IN (SELECT DepartamentoId FROM inserted);
END;
GO

--Para restar municipios
CREATE TRIGGER TRG_Restar_Municipio
ON dbo.Municipios
AFTER INSERT
AS
BEGIN
	UPDATE Departamentos
	SET CantidadMunicipios = CantidadMunicipios -1
	WHERE Id IN (SELECT Estado = 0);
END;
GO

--sumar barrios
CREATE TRIGGER TRG_Sumar_Barrio
ON dbo.Barrios
AFTER INSERT
AS
BEGIN
	UPDATE Municipios
	SET CantidadBarrios = CantidadBarrios + 1
	WHERE Id IN (SELECT MunicipioId FROM inserted);
END;
GO

--restar barrios
CREATE TRIGGER TRG_Restar_Barrio
ON dbo.Barrios
AFTER INSERT
AS
BEGIN
	UPDATE Municipios
	SET CantidadBarrios = CantidadBarrios - 1
	WHERE Id IN (SELECT Estado = 0);
END;
GO

--sumar casas
CREATE TRIGGER TRG_Sumar_Casa
ON dbo.Casas
AFTER INSERT
AS
BEGIN
	UPDATE Barrios
	SET CantidadCasas = CantidadCasas + 1
	WHERE Id IN (SELECT BarrioId FROM inserted);
END;
GO

--restar casas
CREATE TRIGGER TRG_Restar_Casa
ON dbo.Casas
AFTER INSERT
AS
BEGIN
	UPDATE Barrios
	SET CantidadCasas = CantidadCasas - 1
	WHERE Id IN (SELECT Estado = 0);
END;
GO