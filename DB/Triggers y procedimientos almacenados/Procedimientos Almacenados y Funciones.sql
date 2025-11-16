USE CensaData
GO

--Procedimiento almacenado creado para las estadisticas de los barrios, se usa en el backend
CREATE OR ALTER PROCEDURE SP_EstadisticasGruposPorBarrio @BarrioId INT
AS
BEGIN

SELECT COUNT(CASE WHEN p.Edad BETWEEN 0 AND 12 THEN 1 END) AS niños,
	   COUNT(CASE WHEN p.Edad BETWEEN 13 AND 17 THEN 1 END) AS Jovenes,
	   COUNT(CASE WHEN p.Edad BETWEEN 18 AND 59 THEN 1 END) AS adultos,
	   COUNT(CASE WHEN p.Edad > 60 THEN 1 END) AS [Adultos mayores],
	   b.Nombre AS Barrio
From dbo.Empadronados as em
INNER JOIN dbo.Personas AS p
on em.PersonaId = p.Id
INNER JOIN dbo.Casas as c
ON c.Id = em.CasaId
INNER JOIN dbo.Barrios as b
ON b.Id = c.BarrioId
WHERE b.Id = @BarrioId
GROUP BY b.Nombre
HAVING COUNT(p.Id) > 0
END
GO

--procedimiento almacenado estadisticas por departamentos con respecto al estado civil
CREATE  OR ALTER PROCEDURE SP_EstadisticaEstadoCivilPorDepartamento @DepartamentoId INT  
AS  
BEGIN  
 SELECT SUM(CASE WHEN ec.EstadoCivil = 'Casado' THEN 1 ELSE 0 END ) AS Casado,  
     SUM(CASE WHEN ec.EstadoCivil = 'Divorciado' THEN 1 ELSE 0 END) AS Divorciado,  
     SUM(CASE WHEN ec.EstadoCivil = 'Soltero' THEN 1 ELSE 0 END ) AS Soltero,  
     SUM(CASE WHEN ec.EstadoCivil = 'Viudo' THEN 1 ELSE 0 END ) AS Viudo,  
     d.Nombre AS Departamento,  
     SUM(CASE WHEN ec.EstadoCivil = 'Unión Libre' THEN 1 ELSE 0 END ) AS [Union libre]  
 FROM Empadronados AS e  
 INNER JOIN EstadosCiviles AS ec ON   
 E.EstadoCivilId = ec.Id  
 INNER JOIN Casas AS c  
 ON e.CasaId = c.Id  
 INNER JOIN Barrios AS b  
 ON b.Id = c.BarrioId  
 INNER JOIN Municipios AS m  
 ON m.Id = b.MunicipioId  
 INNER JOIN Departamentos AS d  
 ON d.Id = m.DepartamentoId  
 WHERE d.Id = @DepartamentoId  
 GROUP BY d.Nombre  
 ORDER BY d.Nombre  
END  
GO

--funcion Desviacion
CREATE OR ALTER FUNCTION dbo.Fn_Desviacion()
RETURNS Float
AS  BEGIN
DECLARE @Sigma FLOAT 
	SELECT @Sigma = STDEVP(p.Edad * 1.0)
	FROM Empadronados AS e
	INNER JOIN Personas AS p
	ON E.PersonaId = p.Id 
	RETURN @Sigma 
END 
GO
--Funcion Media
CREATE OR ALTER FUNCTION dbo.Fn_Media()
RETURNS FLOAT
AS  BEGIN
DECLARE @Media FLOAT;
		SELECT @Media = AVG(p.Edad * 1.0)
		FROM Empadronados AS e
		INNER JOIN Personas AS p
		ON p.Id = e.PersonaId
		RETURN @Media
END  
GO
--funcion tabular
CREATE OR ALTER FUNCTION dbo.Fn_PersonasCasasMayorIgual4()
RETURNS TABLE
RETURN(
	SELECT c.NumCasa,
	       c.TotalPersonas
	FROM Empadronados AS e
	RIGHT JOIN Casas AS c
	ON c.Id = e.CasaId
	INNER JOIN Personas AS p
	ON p.Id = e.PersonaId
	WHERE c.TotalPersonas >= 4 AND e.RelacionId = 1)
GO

--procedimiento para la lectura de investigador
CREATE OR ALTER PROCEDURE SP_InvestigadorRead
AS
BEGIN
	SELECT i.PrimerNombre, i.SegundoNombre, i.PrimerApellido, i.SegundoApellido, i.Sexo, i.Edad
	FROM Investigadores AS i
END
GO

--procedimiento para buscar
CREATE OR ALTER PROCEDURE SP_BuscarInves @Investigador1 VARCHAR(20), @Investigador2 VARCHAR(20) NULL
AS 
BEGIN
	SELECT I.PrimerNombre,
		   I.SegundoNombre,
		   I.PrimerApellido,
		   I.SegundoApellido,
		   I.Edad,
		   I.Sexo,
		   C.Usuario,
		   C.Contraseña,
		   con.Contacto
	FROM Investigadores AS i
	INNER JOIN CuentasInvestigadores AS c
	ON c.Id = i.CuentaId
	INNER JOIN ContactosInvestigadores AS con
	ON i.Id = con.InvestigadorId
	WHERE i.PrimerNombre = @Investigador1 AND (i.SegundoNombre = @Investigador2 OR @Investigador2 IS NULL)
END
GO

CREATE OR ALTER PROCEDURE SP_TotalDePersonasEmpleadasODesempleadas  
AS  
BEGIN  
 SELECT SUM(CASE WHEN e.EmpleoId <> 21 THEN 1 ELSE 0 END) AS Empleado,  
     SUM(CASE WHEN e.EmpleoId = 21 THEN 1 ELSE 0 END) AS Desempleado  
 FROM Empadronados AS e  
 INNER JOIN Empleos AS em  
 ON em.Id = e.EmpleoId  
 INNER JOIN Personas AS p  
 ON e.PersonaId = p.Id  
 WHERE p.Edad >= 18  
END  