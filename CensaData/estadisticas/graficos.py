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
            "labels":conteo.index.tolist(),
            "series":[{
                "nombre":"Cantidad",
                "values":conteo.values.tolist()
            }]
        }
        return data
    def estadisticasPorEdades(df=df):
        bins = [0 ,13, 18, 60, 100]
        labels = ['Niño', 'Joven', 'Adulto', 'Adulto Mayor']
        
        
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
            "titulo":"Estadisticas por edad",
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
            "labels":ingresos_totales.NivelEducativo.tolist(),
            "series":[{
                "nombre":"Cantidad",
                "values":ingresos_totales.IngresoPersonal.tolist()
            }]
        }
        return data
    def estadisticasDesempleados(df=df):
        bins = [ 18, 35, 60]
        labels = [ 'Joven', 'Adulto']

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
            "titulo":"Grafico de desempleo total",
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
        labels = ['Niño', 'Joven', 'Adulto', 'Adulto Mayor']
        
        
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
            "labels":labels,
            "series":[{
                "nombre":"Cantidad",
                "values":cantidad_de_Mujeres_Desempleadas_Por_edades.Cantidad.tolist()
            }]
        }
        return data
    def estadisticasEmpleadosMujeresEdad(df=df):
        bins = [0 ,13, 18, 60, 100]
        labels = ['Niño', 'Joven', 'Adulto', 'Adulto Mayor']
        
        
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
            "titulo":"Cantidad de mujeres desempleadas por edad",
            "labels":labels,
            "series":[{
                "nombre":"Cantidad",
                "values":cantidad_de_Mujeres_Empleadas_Por_edades.Cantidad.tolist()
            }]
        }
        return data
    def estadisticasDesempleadosHombresEdad(df=df):
        bins = [0 ,13, 18, 60, 100]
        labels = ['Niño', 'Joven', 'Adulto', 'Adulto Mayor']
        
        
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
            "labels":labels,
            "series":[{
                "nombre":"Cantidad",
                "values":cantidad_de_Hombres_Desempleados_Por_edades.Cantidad.tolist()
            }]
        }
        return data
    def estadisticasEmpleadosHombresEdad(df=df):
        bins = [0 ,13, 18, 60, 100]
        labels = ['Niño', 'Joven', 'Adulto', 'Adulto Mayor']
        
        
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
            "titulo":"Hombres emplados por edad",
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