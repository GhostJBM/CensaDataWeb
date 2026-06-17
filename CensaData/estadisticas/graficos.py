import  pandas as pd
from pathlib import  Path

class estadisticas:
    BaseDirec = Path(__file__).resolve().parent
    ruta = BaseDirec / "Dataset__censadata.csv"
    df=pd.read_csv(ruta,delimiter=";")
    
    def estadisticasPorIngreso(dfIngreso=df):
        conteo = dfIngreso["IngresoPersonal"].value_counts()
        data = {
            "TipodeGrafico":"bar",
            "titulo":"Ingreso Personal",
            "descripcion":"Este gráfico muestra la distribución de los ingresos personales declarados por los encuestados, permitiendo identificar tramos de ingreso más frecuentes en la población censada.",
            "labels":conteo.index.tolist(),
            "series":[
                {
                    "nombre":"Cantidad",
                    "values": conteo.values.tolist()
                }
            ]
        }
        return data
    def estadisticasPorNivelEducativo(dfIngreso=df):
        conteo = dfIngreso["NivelEducativo"].value_counts()
        data = {
            "TipodeGrafico":"bar",
            "titulo":"Niveles educativos",
            "descripcion":"Este gráfico presenta la proporción de personas según el nivel educativo alcanzado, facilitando la comprensión del perfil formativo de la población registrada.",
            "labels":conteo.index.tolist(),
            "series":[{
                "nombre":"Cantidad",
                "values":conteo.values.tolist()
            }]
        }
        return data
    def estadisticasPorEmpleo(dfIngreso=df):
        conteo = dfIngreso["Empleo"].value_counts()
        data = {
            "TipodeGrafico":"bar",
            "titulo":"Empleos",
            "descripcion":"Este gráfico resume la situación ocupacional de la población, mostrando las categorías de empleo más representativas dentro del censo.",
            "labels":conteo.index.tolist(),
            "series":[
                {
                    "nombre":"Cantidad",
                    "values":conteo.values.tolist()
                }
            ]
        }
        return data
    def estadisticasPorEstadoCivil(dfIngreso=df):
        conteo = dfIngreso["EstadoCivil"].value_counts()
        data = {
            "TipodeGrafico":"bar",
            "titulo":"Estados civiles",
            "descripcion":"Este gráfico muestra la distribución de los estados civiles de la población encuestada, lo que ayuda a entender la composición social del conjunto de datos.",
            "labels":conteo.index.tolist(),
            "series":[{
                "nombre":"Cantidad",
                "values":conteo.values.tolist()
            }]
        }
        return data
    def estadisticasPorEdades(df=df):
        bins = [0 ,13, 18, 60, 100]
        labels = ['Niño: 0 a 12', 'Joven: 13 a 17', 'Adulto: 18 a 59', 'Adulto Mayor: 60 en adelante']
        
        
        df['grupos_edad'] = pd.cut(
            df['Edad'],
            bins=bins,
            labels=labels,
            include_lowest=True
        )

        conteo_edades = (
            df.groupby('grupos_edad', observed=False)
            .size()
            .reset_index(name='Cantidad')
        )
        
        data = {
            "tipo":"bar",
            "titulo":"Estadísticas por edad",
            "descripcion":"Este gráfico agrupa a la población por rangos de edad, permitiendo observar la estructura etaria predominante en la muestra.",
            "labels":conteo_edades.grupos_edad.tolist(),
            "series":[{
                "nombre":"Cantidad",
                "values":conteo_edades.Cantidad.tolist()
            }]
        }
        return data
    def estadisticasIngresosNivelEducativo(df=df):
        ingresos_totales = df.groupby('NivelEducativo', as_index=False)['IngresoPersonal'].count()
        
        data={
            "tipo":"bar",
            "titulo":"Cantidad de personas con ingresos por nivel educativo",
            "descripcion":"Este gráfico presenta la cantidad de personas con ingreso registrado por nivel educativo, lo que permite identificar la relación entre educación e inserción laboral.",
            "labels":ingresos_totales.NivelEducativo.tolist(),
            "series":[{
                "nombre":"Cantidad",
                "values":ingresos_totales.IngresoPersonal.tolist()
            }]
        }
        return data
    def estadisticasDesempleados(df=df):
        bins = [ 18, 35, 60]
        labels = [ 'Adulto Joven de 18 a 34', 'Adulto de 35 a 60']

        df['grupos_trabajo'] = pd.cut(
            df['Edad'],
            bins=bins,
            labels=labels,
            include_lowest=True
            )
        # Filtrar desempleados
        desempleados = df[df['Empleo'] == 'Desempleado']
        
        
        # Contar desempleados por grupo de edad
        conteo = (
            desempleados.groupby('grupos_trabajo' , observed=False)
            .size()
            .reset_index(name='Cantidad')
        )
        data = {
            "tipo":"bar",
            "titulo":"Gráfico de desempleo total",
            "descripcion":"Este gráfico muestra la cantidad de personas desempleadas por rango de edad, lo que facilita identificar los grupos etarios con mayor incidencia de desempleo.",
            "labels":conteo.grupos_trabajo.tolist(),
            "series":[{
                "nombre":"Cantidad",
                "values":conteo.Cantidad.tolist()
            }]
        }
        return data
    def estadisticasEstadosCivilEmpleoRelacion(df=df):
        
        pass
    def estadisticasGrupoDeEdadYnivelEducativo(df=df):
        pass
    def estadisticaDesempleadosMujeresEdad(df=df):
        bins = [0 ,13, 18, 60, 100]
        labels = ['Niño: 0 a 12', 'Joven: 13 a 17', 'Adulto: 18 a 59', 'Adulto Mayor: 60 en adelante']
        
        
        df['grupos_edad'] = pd.cut(
            df['Edad'],
            bins=bins,
            labels=labels,
            include_lowest=True
        )
        cantidad_de_Mujeres_Desempleadas_Por_edades = (
        df.query("Empleo == 'Desempleado' and Sexo == 'F'")
            .groupby('grupos_edad', observed=False)
            .size()
            .reset_index(name='Cantidad')
        )
        data = {
            "tipo":"bar",
            "titulo":"Cantidad de mujeres desempleadas por edad",
            "descripcion":"Este gráfico muestra la incidencia del desempleo entre mujeres por rango de edad, destacando los grupos con mayor afectación.",
            "labels":labels,
            "series":[{
                "nombre":"Cantidad",
                "values":cantidad_de_Mujeres_Desempleadas_Por_edades.Cantidad.tolist()
            }]
        }
        return data
    def estadisticasEmpleadosMujeresEdad(df=df):
        bins = [0 ,13, 18, 60, 100]
        labels = ['Niño: 0 a 12', 'Joven: 13 a 17', 'Adulto: 18 a 59', 'Adulto Mayor: 60 en adelante']
        
        
        df['grupos_edad'] = pd.cut(
            df['Edad'],
            bins=bins,
            labels=labels,
            include_lowest=True
        )
        # Mujeres empleadas agrupadas por edad
        cantidad_de_Mujeres_Empleadas_Por_edades = (
            df.query("Empleo != 'Desempleado' and Sexo == 'F'")
            .groupby('grupos_edad', observed=False)
            .size()
            .reset_index(name='Cantidad')
        )
        data = {
            "tipo":"bar",
            "titulo":"Cantidad de mujeres empleadas por edad",
            "descripcion":"Este gráfico ilustra la distribución de mujeres empleadas según rango de edad, permitiendo comparar niveles de ocupación femenina en distintos grupos etarios.",
            "labels":labels,
            "series":[{
                "nombre":"Cantidad",
                "values":cantidad_de_Mujeres_Empleadas_Por_edades.Cantidad.tolist()
            }]
        }
        return data
    def estadisticasDesempleadosHombresEdad(df=df):
        bins = [0 ,13, 18, 60, 100]
        labels = ['Niño: 0 a 12', 'Joven: 13 a 17', 'Adulto: 18 a 59', 'Adulto Mayor: 60 en adelante']
        
        
        df['grupos_edad'] = pd.cut(
            df['Edad'],
            bins=bins,
            labels=labels,
            include_lowest=True
        )
        cantidad_de_Hombres_Desempleados_Por_edades = (
        df.query("Empleo == 'Desempleado' and Sexo == 'M'")
            .groupby('grupos_edad', observed=False)
            .size()
            .reset_index(name='Cantidad')
        )
        
        data = {
            "Tipo":"bar",
            "titulo":"Hombres desempleados por edad",
            "descripcion":"Este gráfico examina la incidencia del desempleo entre hombres de diferentes grupos de edad, destacando aquellos tramos etarios donde se concentra la mayor proporción de personas sin empleo.",
            "labels":labels,
            "series":[{
                "nombre":"Cantidad",
                "values":cantidad_de_Hombres_Desempleados_Por_edades.Cantidad.tolist()
            }]
        }
        return data
    def estadisticasEmpleadosHombresEdad(df=df):
        bins = [0 ,13, 18, 60, 100]
        labels = ['Niño: 0 a 12', 'Joven: 13 a 17', 'Adulto: 18 a 59', 'Adulto Mayor: 60 en adelante']
        
        
        df['grupos_edad'] = pd.cut(
            df['Edad'],
            bins=bins,
            labels=labels,
            include_lowest=True
        )
        cantidad_de_Hombres_Empleados_Por_edades = (
            df.query("Empleo != 'Desempleado' and Sexo == 'M'")
            .groupby('grupos_edad', observed=False)
            .size()
            .reset_index(name='Cantidad')
        )
        
        data ={
            "tipo":"bar",
            "titulo":"Hombres empleados por edad",
            "descripcion":"Este gráfico muestra la distribución de hombres empleados por rango de edad, con el fin de identificar los principales grupos etarios que participan en el mercado laboral.",
            "labels":labels,
            "series":[{
                "nombre":"Cantidad",
                "values":cantidad_de_Hombres_Empleados_Por_edades.Cantidad.tolist()
            }]
        }
        return data
    def estadisticasPersonasIngresosBarrios(df=df):
        df_barrios = (
        df.groupby('barrio')
        .agg(
            PersonasBarrio=('IngresoPersonal', 'count'),
            IngresoPromedio=('IngresoPersonal', 'mean')
        )
        .reset_index()
        )

        data = {
            "tipo": "bar",
            "titulo": "Cantidad de personas e ingreso promedio por barrio",
            "descripcion": "Este gráfico combina el número de personas censadas con el ingreso promedio por barrio, lo que ayuda a identificar zonas con mayor densidad poblacional y diferencias económicas entre sectores geográficos.",
            "labels": df_barrios["barrio"].tolist(),
            "series": [
                {
                    "nombre": "Personas",
                    "values": df_barrios["PersonasBarrio"].tolist()
                },
                {
                    "nombre": "Ingreso Promedio",
                    "values": df_barrios["IngresoPromedio"].round(2).tolist()
                }
            ]
        }       

        return data