## Distintos servicios del proyecto
from django.db import transaction 
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
from django.core.mail import send_mail
import math, secrets
from .estadisticas.graficos import estadisticas
from io import BytesIO
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, HRFlowable)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import cm
import matplotlib 
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import time
from django.core.cache import cache
import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed

##Clase de excepciones
class ExcepcionNegocio(Exception):
    pass

#Clase de validaciones
class validaciones:
    def validarfecha(self, data):
        try:
            Cfechainiciocenso = datetime.strptime(data["fechainiciocenso"], "%Y-%m-%d")
            fecha = datetime.now()
            fechaActual = datetime(fecha.year,fecha.month, fecha.day)
        
            if Cfechainiciocenso < fechaActual:
                raise ExcepcionNegocio("La fecha de inicio no puede ser menor a la fecha actual")
            
            Cfechafincenso =datetime.strptime(data["fechafincenso"],"%Y-%m-%d")
            if Cfechafincenso < Cfechainiciocenso:
                raise ExcepcionNegocio("La fecha de fin no puede ser menor a la de inicio")
            elif Cfechafincenso < fechaActual:
                raise ExcepcionNegocio("La fecha de fin no puede ser menor a la fecha actual")
        except ValueError as e:
            raise e
    def validarFechaInicio(self, data):
        try:
            fechaInicio = datetime.strptime(data["fechainiciocenso"], "%Y-%m-%d")
        except ValueError:
            raise ExcepcionNegocio( "Fecha de inicio Invalida")
    def validarfechafinal(self, data):
        try:
            Cfechafincenso = datetime.strptime(data["fechafincenso"],"%Y-%m-%d")
        except ValueError:
            raise ExcepcionNegocio( "La fecha de fin es incorrecta")
    
    ##validaciones para nombre
    def ValNombreCenso(self, data):
        try:
            nombre = data["nombrecenso"]
        except:
            raise ExcepcionNegocio("se requiere el nombre")
        
    # validaciones para el total de poblacion
    def ValPoblaciontotal(self, data):
        try:
            poblacion = int(data["poblaciontotal"])
        except:
            raise ExcepcionNegocio("se requiere la poblacion")
    def valPoblacionIncorrecta(self, data):
            poblacion = int(data["poblaciontotal"])
            if poblacion < 1:
                raise ExcepcionNegocio("La poblacion tiene que ser mayor a 0")
    def validarExistenciafecha(self, data):
        try:
            Cfechainiciocenso = data["fechainiciocenso"]
        except:
            raise ExcepcionNegocio("Se requiere la fecha de inicio")
        try:
            Cfechafincenso = data["fechafincenso"]
        except:
            raise ExcepcionNegocio("Se requiere la fecha de fin")
        
        
## Crear Censo INIDE Trabajadores
class CensoInideService:
    @transaction.atomic
    def CrearCenso(self,data):
        try:
            ##validaciones de existencia
            validaciones.ValNombreCenso(self,data)
            validaciones.validarExistenciafecha(self,data)
            
            #validaciones para la poblacion
            validaciones.ValPoblaciontotal(self, data)
            validaciones.valPoblacionIncorrecta(self,data)
            
            ##validaciones para la fechas
            validaciones.validarFechaInicio(self,data)
            validaciones.validarfechafinal(self,data)
            validaciones.validarfecha(self,data)
            
            
            ##opereaciones de censo
            poblacion = int(data["poblaciontotal"])
            Cfechainiciocenso = datetime.strptime(data["fechainiciocenso"], "%Y-%m-%d")
            Cfechafincenso =datetime.strptime(data["fechafincenso"],"%Y-%m-%d")
        
            n = poblacion * (math.pow(1.96,2))*0.5 * 0.5 
            m = (math.pow(0.05,2))*poblacion +(math.pow(1.96,2))*0.5*0.5
            Muestrapoblacion = round(n/m)

            #creacion
            Censos.objects.create(
                nombrecenso = data["nombrecenso"],
                poblaciontotal = poblacion,
                fechainiciocenso = Cfechainiciocenso,
                fechafincenso = Cfechafincenso,
                muestrapoblacional = Muestrapoblacion,
                cantidadencuestados = 0,
                cantidadrespuestaspositivas = 0,
                cantidadrespuestasnegativas = 0,
                cantidadencuestas = 0,
                cantidadcasasencuestadas = 0,
                estado = 1
            )
        
            message = "Censo Creado"
            return message
        except ValueError as e:
            return e
        
class validacionesEncuesta:
    def validarExistencias(self, data):
        try:
            casa = data["Casa"]
        except:
            raise ExcepcionNegocio("Faltan los datos de casa")
        try:
            encuesta = data["encuestainide"]
        except:
            raise ExcepcionNegocio("Faltan los datos de encuesta")
        try:
            Personas = data["personas"]
        except:
            raise ExcepcionNegocio("Faltan los datos de personas")
        try:
            Empadronados = data["empadronados"]
        except:
            raise ExcepcionNegocio("Faltan los datos de personas")
    def validarInvestigador(self, user):
        try:
            investigador = Investigadores.objects.get(cuentaid = user.id)
            id = investigador.id
        except:
            raise ExcepcionNegocio("user invalido")
    def validartiposCasas(self, data):
        casa = data["Casa"]
        try:
            numero = int(casa["numcasa"])
        except:
            raise ExcepcionNegocio("El numero de casa es invalido")
        try:
            barrio = int(casa["barrioid"])
        except:
            raise ExcepcionNegocio("el barrio no es valido")
        try:
            infraestructura = int(casa["infraestructuraid"])
        except:
            raise ExcepcionNegocio("La infraestructura no es valida")
    def validarTiposEncuesta(self, data):
        encuesta = data["encuestainide"]
        try:
            fecha = datetime.strptime(encuesta["fechainicio"],"%Y-%m-%d")
        except:
            raise ExcepcionNegocio("La fecha de inicio no es valida")
        try:
            fecha = datetime.strptime(encuesta["fechafin"], "%Y-%m-%d")
        except:
            raise ExcepcionNegocio("La fecha de fin no es valida")
        try:
            fechaActual = datetime.now()
            fechaActual = datetime(fechaActual.year, fechaActual.month, fechaActual.day)
            fecha = datetime.strptime(encuesta["fechainicio"],"%Y-%m-%d")
            fechafin = datetime.strptime(encuesta["fechafin"], "%Y-%m-%d")
            if fecha < fechaActual:
                raise ExcepcionNegocio ("La fecha de inicio no puede ser menor a la actual")
            if fechafin < fecha:
                raise ExcepcionNegocio("La fecha de fin no puede ser menor a la de inicio")
        except ValueError as e:
            raise e
    def validarEdad(self, data):
        try:
            fechaNa = datetime.strptime(data["fechanacimiento"],"%Y-%m-%d")
            fechaActual = datetime.now()
            
            edad = fechaActual.year - fechaNa.year
            
            if(fechaActual.month, fechaActual.day)< (fechaNa.month, fechaNa.day):
                edad -= 1
                
            return int(edad)
        except:
            raise ExcepcionNegocio(f"La fecha de nacimiento de {data} esta mal")
    def validarCedula(self, data):
        try:
            cedula = str(data["numerocedula"])
        
            if len(cedula) != 14    :
                raise ExcepcionNegocio("La cedula tiene que tener un largo de 14")
            return cedula
        except:
            return None

        
        
class EncuestaInideService:

    @transaction.atomic
    def CrearEncuesta(self,data, user):
        
        validacionesEncuesta.validarExistencias(self, data)
        validacionesEncuesta.validarInvestigador(self, user)
        validacionesEncuesta.validartiposCasas(self, data)
        validacionesEncuesta.validarTiposEncuesta(self, data)
        
        investigador = Investigadores.objects.get(cuentaid = user.id)
        casa = data["Casa"]
        encuesta = data["encuestainide"]
        EPersonas = data["personas"]
        EEmpadronados = data["empadronados"]
        
        
        #Encuesta
        fechaInicioEncuesta = datetime.strptime(encuesta["fechainicio"],"%Y-%m-%d")
        fechaFinEncuesta = datetime.strptime(encuesta["fechafin"], "%Y-%m-%d")
        
        infraestructura = Infraestructuras.objects.get(id=casa["infraestructuraid"])
        barrio = Barrios.objects.get(id = casa["barrioid"])
        
        #Casa
        Ecasa = Casas.objects.create(
            numcasa = int(casa["numcasa"]),
            cantidadhombres = 0,
            cantidadmujeres = 0,
            infraestructuraid = infraestructura,
            barrioid = barrio,
            serviciodeagua = int(casa["serviciodeagua"]),
            serviciodeenergia = int(casa["serviciodeenergia"]),
            ingresofamiliar = 0,
            estado = 1
        )
        
        censo = Censos.objects.get(id = encuesta["censoid"])
        
        Encuesta = Encuestasinidetrabajadores.objects.create(
            casaid = Ecasa,
            censoid = censo,
            investigadorid = investigador,
            fechainicio = fechaInicioEncuesta,
            fechafin = fechaFinEncuesta,
            respuesta = encuesta["respuesta"],
            totalencuestados = 0,
            estado = 1
        )

        #personas y empadronados
        for p, e in zip(EPersonas.values(), EEmpadronados.values()):

            persona = Personas.objects.create(
            primernombre=p["primernombre"],
            segundonombre=p["segundonombre"],
            primerapellido=p["primerapellido"],
            segundoapellido=p["segundoapellido"],
            fechadenacimiento=datetime.strptime(p["fechanacimiento"], "%Y-%m-%d"),
            edad=validacionesEncuesta.validarEdad(self, p),
            sexo=p["sexo"],
            estado = 1
        )
            relacion = Relacionesparentescos.objects.get(id=e["relacionid"])
            empleo = Empleos.objects.get(id=e["empleoid"])
            estadocivil = Estadosciviles.objects.get(id=e["estadocivilid"]) 
            Nivel = Niveleseducativos.objects.get(id=e["niveleducativoid"])
            
            cedula = validacionesEncuesta.validarCedula(self,e)
            empadronado = Empadronados.objects.create(
            personaid=persona,
            relacionid=relacion,
            numerocedula=cedula,
            estadocivilid=estadocivil,
            empleoid=empleo,
            niveleducativoid=Nivel,
            casaid = Ecasa,
            ingresopersonal = e["ingresopersonal"],
            estado = 1
        )
            
## otras clases
class validacionesInidividualesIncercion:
    class validacionesPersonas:
        def valiExiste(data):
            try:
                fecha = validacionesInidividualesIncercion.validacionesPersonas.valiFecha(data["fechadenacimiento"])
                if Personas.objects.filter(primernombre=data["primernombre"], 
                                        primerapellido = data["primerapellido"], fechadenacimiento = fecha).exists():
                    raise ExcepcionNegocio("La persona ya existe")
            except Exception as e:
                raise ExcepcionNegocio(e)
        def edad(fecha):
            try:
                fechaNa = datetime.strptime(str(fecha),"%Y-%m-%d")
                fechaActual = datetime.now()
            
                edad = fechaActual.year - fechaNa.year
            
                if(fechaActual.month, fechaActual.day)< (fechaNa.month, fechaNa.day):
                    edad -= 1
                
                return int(edad)
            except:
                raise ExcepcionNegocio(f"La fecha de nacimiento de {fecha} esta mal")
        def valiSexo(sexo):
            sexoV = None
            try:
                sexoV = chr(sexo).upper()
                if sexoV != "F" or sexoV != "M":
                    raise ExcepcionNegocio("Sexo invalido")
            except:
                raise ExcepcionNegocio("El sexo solo puede ser de una letra")
            return sexoV
            
        def valiFecha(fecha):
            fechaValida = None
            try:
                fechaValida = datetime.strptime(str(fecha), "%Y-%m-%d")
            except ExcepcionNegocio as e:
                raise e("La fecha es invalida")
            return fechaValida
    class validacionesBarrios:
        def valiExiste(data): 
            try:
                if Barrios.objects.filter(nombre=data["nombre"], municipioid_id=data["municipioid"]).exists():
                    raise ExcepcionNegocio("El Barrio Ya existe")
                return True
            except Exception as e:
                raise ExcepcionNegocio(e)
    class validacionesDepartamentos:
        def valiExiste(data):
            try:
                if Departamentos.objects.filter(nombre=data["nombre"]).exists():
                    raise ExcepcionNegocio("El barrio ya existe")
            except:
                raise ExcepcionNegocio("El Departamento ya existe")
    class validacionesMunicipios:
        def valiExiste(data):
            try:
                if Municipios.objects.filter(nombre = data["nombre"], departamentoid_id = data["departamentoid"]):
                    raise ExcepcionNegocio("El municipio ya existe")
            except:
                raise ExcepcionNegocio("El municipio ya existe")
    class validacionesEstadoCiviles:
        def valiExiste(data):
            try:
                if Estadosciviles.objects.filter(estadocivil = data["estadocivil"]).exists():
                    raise ExcepcionNegocio("El estado civil ya existe")
            except:
                raise ExcepcionNegocio("El estado civil ya existe")
    class validacionesEmpleos:
        def valiExiste(data):
            try:
                if Empleos.objects.filter(empleo=data["empleo"]).exists():
                    raise ExcepcionNegocio("El Empleo ya existe")
            except:
                raise ExcepcionNegocio("El Empleo ya existe")
    class validacionesInfraestructura:
        def valiExisteTipoTecho(data):
            try:
                if Tiposdetechos.objects.filter(tipodetecho = data["tipodetecho"]).exists():
                    raise ExcepcionNegocio("El tipo de techo ya existe")
            except:
                raise ExcepcionNegocio("El tipo de techo ya existe")
        def ValiExisteTipoPiso(data):
            try:
                if Tiposdepisos.objects.filter(tipodepiso = data["tipodepiso"]).exists():
                    raise ExcepcionNegocio("El tipo de piso ya existe")
            except:
                raise ExcepcionNegocio("El tipo de piso ya existe")
        def valiExisteMaterialContruccion(data):
            try:
                if Materialesconstrucciones.objects.filter(materialcontruccion = data["materialcontruccion"]).exists():
                    raise ExcepcionNegocio("El material de contruccion ya existe")
            except:
                raise ExcepcionNegocio("El material de contruccion ya existe")
    class validacionesRelacionParentesco:
        def valiExiste(data):
            try:
                if Relacionesparentescos.objects.filter(relacion = data["relacion"]).exists():
                    raise ExcepcionNegocio("La relacion ya existe")
            except:
                raise ExcepcionNegocio("La relacion ya existe")
    class validacionesDiscapacidades:
        def valiExiste(data):
            try:
                if Discapacidades.objects.filter(discapacidad = data["discapacidad"]).exists():
                    raise ExcepcionNegocio("La discapacidad ya existe")
            except:
                raise ExcepcionNegocio("La discapacidad ya existe")
    class validacionesNivelesEducativos:
        def valiExiste(data):
            try:
                if Niveleseducativos.objects.filter(niveleducativo= data["niveleducativo"], grado = data["grado"]).exists():
                    raise ExcepcionNegocio("El nivel educativo ya existe")
            except:
                raise ExcepcionNegocio("El nivel educativo ya existe")
    class ValidacionesInvestigadoresAdmin:
        def valiExisteInves(data):
            try:
                if Investigadores.objects.filter(primernombre=data["primernombre"], primerapellido = data["primerapellido"], sexo=data["sexo"], edad = data["edad"], cuentaid_id = data["cuentaid"], administradorid_id=data["administradorid"]):
                    raise ExcepcionNegocio("El Investigador ya existe")
            except:
                raise ExcepcionNegocio("El investigador ya existe")
        def valiExistAdmin(data):
            try:
                if Investigadores.objects.filter(primernombre=data["primernombre"], primerapellido = data["primerapellido"], sexo=data["sexo"], edad = data["edad"], cuentaid_id = data["cuentaid"], administradorid_id=data["administradorid"]):
                    raise ExcepcionNegocio("El Administrador ya existe")
            except:
                raise ExcepcionNegocio("El administrador ya existe")
        def segundoNombre(data):
            try: 
                segundo = data["segundonombre"]
                return segundo
            except:
                return None
        def segundoApellido(data):
            try:
                segundo = data["segundoapellido"]
                return segundo
            except:
                return None
        def sexo(sexo):
            try:
                s = str(sexo).upper()
                if s == "M" or s == "F":
                    return s
                else:
                    raise ExcepcionNegocio("solo se permite F o M")
            except:
                raise ExcepcionNegocio("El sexo es invalido")
        def edad(edad):
            try:
                e = int(edad)
                
                if e < 0:
                    raise ExcepcionNegocio("La edad no puede ser menor a 0")
                return e
            except:
                raise ExcepcionNegocio("La edad es invalida")
        def cuenta(Id):
            try:
                
                cuenta = Cuentasinvestigadoresadmin.objects.get(id=Id.id)
                
                return cuenta
            except:
                raise ExcepcionNegocio("La cuenta no existe")
        def admin(Id):
            try:
                admin = Administradores.objects.get(id = Id.id)
                return admin
            except:
                raise ExcepcionNegocio("El administrador no existe")
        def contantoExistente(data):
            try:
                contacto = Contactosinvestigadores.objects.filter(contacto = data["contacto"], investigadorid_id = data["investigadorid"]).exists()
                if contacto:
                    raise ExcepcionNegocio("El contacto ya existe para este investigador")
            except Exception as e:
                raise ExcepcionNegocio(e)
    class validacionesIndividualesEmpadronados:
        def valiExisteContato(data):
            try:
                contacto = Contactosempadronados.objects.filter(contacto = data["contacto"], empadronadoid_id = data["empadronadoid"]).exists()
                if contacto:
                    raise ExcepcionNegocio("El contacto ya existe para este empadronado")
            except Exception as e:
                raise ExcepcionNegocio(e)
    class validacionesInfraestructura:
        class materialesContruccion:
            def existe(data):
                try:
                    if Materialesconstrucciones.objects.filter(materialcontruccion = data["materialcontruccion"]):
                        raise ExcepcionNegocio("El material ya existe")
                except ValueError as e:
                    raise ExcepcionNegocio(e)
        class tipodepiso:
            def existe(data):
                try:
                    if Tiposdepisos.objects.filter(tipopiso=data["tipopiso"]):
                        raise ExcepcionNegocio("el piso ya existe")
                except ValueError as e:
                    raise ExcepcionNegocio(e)
        class tipodetecho:
            def existe(data):
                try:
                    if Tiposdetechos.objects.filter(tipodetecho=data["tipodetecho"]):
                        raise ExcepcionNegocio("el techo ya existe")
                except ValueError as e:
                    raise ExcepcionNegocio(e)
    class ValidacionesDiscapacidadesPersona:
        def DiscPersonExiste(data):
            try:
                if Discapacidadespersonas.objects.filter(discapacidadid=data["discapacidadid"], personaid=data["discapacidadid"]):
                    raise ExcepcionNegocio("Ya existe")
            except ValueError as e:
                raise ExcepcionNegocio(e)

class EstadisticasServicies:
    CACHE_TIMEOUT = 600  # 10 minutos
    
    GRF = {
        "estadisticas por ingreso":estadisticas.estadisticasPorIngreso,
        "estadisticas por nivel educativo":estadisticas.estadisticasPorNivelEducativo,
        "estadisticas por empleo":estadisticas.estadisticasPorEmpleo,
        "estadisticas por estado civil":estadisticas.estadisticasPorEstadoCivil,
        "estadisticas por edades":estadisticas.estadisticasPorEdades,
        "estadisticas por Ingresos basados en el nivel educativo":estadisticas.estadisticasIngresosNivelEducativo,
        "estadisticas desempleados general":estadisticas.estadisticasDesempleados,
        "estadisticas desempleadas mujeres por edad":estadisticas.estadisticaDesempleadosMujeresEdad,
        "estadisticas empleadas mujeres por edad":estadisticas.estadisticasEmpleadosMujeresEdad,
        "estadisticas desempleados hombres por edad":estadisticas.estadisticasDesempleadosHombresEdad,
        "estadisticas empleados hombres por edad":estadisticas.estadisticasEmpleadosHombresEdad,
        "estadisticas ingresos de personas por barrios":estadisticas.estadisticasPersonasIngresosBarrios
    }
    
    @staticmethod
    def _sanitizar_cache_key(tipo):
        """Sanitiza la clave de caché reemplazando espacios por guiones bajos."""
        return f"grafico_{tipo.replace(' ', '_')}"
    
    @staticmethod
    def getGrafico(tipo, GRF=GRF):
        """
        Obtiene un gráfico con caché de 10 minutos.
        Evita regenerar datos si ya están en caché.
        """
        cache_key = EstadisticasServicies._sanitizar_cache_key(tipo)
        cached = cache.get(cache_key)
        if cached:
            return cached
            
        funcion = GRF.get(tipo)
        if funcion is None:
            raise ExcepcionNegocio("grafico invalido")
        
        resultado = funcion()
        cache.set(cache_key, resultado, EstadisticasServicies.CACHE_TIMEOUT)
        return resultado
    
    @staticmethod
    def getGraficosMultiples(tipos, max_workers=4, GRF=GRF):
        """
        Obtiene múltiples gráficos en paralelo usando ThreadPoolExecutor.
        Reduce significativamente el tiempo de carga cuando se necesitan varios gráficos.
        
        Args:
            tipos: Lista de tipos de gráficos a obtener
            max_workers: Número máximo de workers (threads) paralelos
        
        Returns:
            Dict con tipo como clave y gráfico como valor
        """
        graficos_dict = {}
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Crear futures para todos los gráficos
            futures = {
                executor.submit(EstadisticasServicies.getGrafico, tipo): tipo 
                for tipo in tipos
            }
            
            # Recopilar resultados conforme se completan
            for future in as_completed(futures):
                tipo = futures[future]
                try:
                    graficos_dict[tipo] = future.result()
                except Exception as e:
                    graficos_dict[tipo] = None
        
        return graficos_dict
    
    @staticmethod
    def limpiarCache(tipo=None):
        """
        Limpia el caché de gráficos.
        Si tipo es None, limpia todos los gráficos.
        """
        if tipo is None:
            # Limpiar todos los gráficos
            for tipo_grafico in EstadisticasServicies.GRF.keys():
                cache_key = EstadisticasServicies._sanitizar_cache_key(tipo_grafico)
                cache.delete(cache_key)
        else:
            cache_key = EstadisticasServicies._sanitizar_cache_key(tipo)
            cache.delete(cache_key)
    
    @staticmethod
    def _generar_imagen_cached(labels, values, nombre_serie):
        """
        Genera y cachea una imagen PNG de un gráfico de barras.
        Reutiliza imágenes en caché si existen.
        """
        import hashlib
        
        # Crear una clave única basada en los datos
        datos_str = f"{nombre_serie}_{'_'.join(str(l) for l in labels)}_{'_'.join(str(v) for v in values)}"
        cache_key = f"grafico_img_{hashlib.md5(datos_str.encode()).hexdigest()}"
        
        # Intentar obtener del caché
        img_cached = cache.get(cache_key)
        if img_cached:
            img_cached.seek(0)
            return img_cached
        
        # Generar nueva imagen
        fig, ax = plt.subplots(figsize=(10, 5))  # Reducido de (12, 6)
        
        ax.bar([str(x) for x in labels], values)
        
        ax.set_xlabel("Categorías")
        ax.set_ylabel("Valores")
        plt.xticks(rotation=45, ha="right")
        fig.tight_layout()
        
        img_buffer = BytesIO()
        plt.savefig(img_buffer, format="png", dpi=100, bbox_inches='tight')  # Reducido de dpi=150
        plt.close(fig)
        
        img_buffer.seek(0)
        
        # Guardar en caché por 1 hora
        cache.set(cache_key, img_buffer, 3600)
        
        return img_buffer

class ReportesService:
    def existe(data, user):
        if Reportes.objects.filter(tiporeporte=data["tiporeporte"], administradorid=user):
            return ExcepcionNegocio("El reporte ya existe")
        return True
    def createReporte(user, data):
        ReportesService.existe(data, user)
        Reportes.objects.create(
            tiporeporte = data["tiporeporte"],
            espublico = 0,
            estado = 1,
            administradorid = user
        )
    class ispublic:
        @staticmethod
        def ReporteAPublic(data):
            upda = Reportes.objects.filter(id=data.id).first()
            upda.espublico = 1
            upda.save()
            return upda
    class generarPDF:

        @staticmethod
        def generarReporteCompleto():
            t0 = time.perf_counter()
            buffer = BytesIO()
            doc = SimpleDocTemplate(
                buffer,
                pagesize=letter,
                leftMargin=2*cm,
                rightMargin=2*cm,
                topMargin=3*cm,
                bottomMargin=2.5*cm
            )

            def header_footer(canvas, doc):
                canvas.saveState()
                width, height = letter
                canvas.setFont("Helvetica-Bold", 9)
                canvas.setFillColor(colors.HexColor("#2F4B7C"))
                canvas.drawString(doc.leftMargin, height - 1.2*cm, "CENSADATA - Reporte Estadístico General")
                canvas.setStrokeColor(colors.HexColor("#C8D1E0"))
                canvas.setLineWidth(0.5)
                canvas.line(doc.leftMargin, height - 1.3*cm, width - doc.rightMargin, height - 1.3*cm)
                canvas.setFont("Helvetica", 8)
                canvas.setFillColor(colors.grey)
                canvas.drawRightString(width - doc.rightMargin, doc.bottomMargin - 0.8*cm, f"Página {canvas.getPageNumber()}")
                canvas.restoreState()

            styles = getSampleStyleSheet()
            styles.add(ParagraphStyle(
                name="TitleLarge",
                parent=styles["Title"],
                fontName="Helvetica-Bold",
                fontSize=26,
                leading=30,
                textColor=colors.HexColor("#2F4B7C"),
                spaceAfter=12
            ))
            styles.add(ParagraphStyle(
                name="SectionHeading",
                parent=styles["Heading1"],
                fontName="Helvetica-Bold",
                fontSize=18,
                leading=22,
                textColor=colors.HexColor("#1E3A59"),
                spaceBefore=12,
                spaceAfter=10
            ))
            styles.add(ParagraphStyle(
                name="SubHeading",
                parent=styles["Heading2"],
                fontName="Helvetica-Bold",
                fontSize=14,
                leading=18,
                textColor=colors.HexColor("#2E4A75"),
                spaceBefore=10,
                spaceAfter=8
            ))
            styles.add(ParagraphStyle(
                name="SubHeading2",
                parent=styles["Heading3"],
                fontName="Helvetica-Bold",
                fontSize=12,
                leading=15,
                textColor=colors.HexColor("#1B3256"),
                spaceBefore=8,
                spaceAfter=6
            ))
            styles.add(ParagraphStyle(
                name="BodyTextCustom",
                parent=styles["BodyText"],
                fontName="Helvetica",
                fontSize=11,
                leading=16,
                spaceAfter=10,
                alignment=4
            ))
            styles.add(ParagraphStyle(
                name="BodySmall",
                parent=styles["BodyText"],
                fontName="Helvetica",
                fontSize=9,
                leading=12,
                textColor=colors.grey,
                spaceAfter=6,
                alignment=4
            ))
            estilos_visuales = {
                "separator": HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#C8D1E0"), spaceBefore=10, spaceAfter=10)
            }
            elementos = []



            elementos.append(
                Paragraph(
                    "CENSADATA",
                    styles["TitleLarge"]
                )
            )

            elementos.append(Spacer(1, 12))

            elementos.append(
                Paragraph(
                    "Reporte Estadístico General",
                    styles["SectionHeading"]
                )
            )

            elementos.append(Spacer(1, 10))

            elementos.append(
                Paragraph(
                """
                    Informe sintético de Censadata con datos de población,
                    educación, empleo y distribución territorial.
                    """,
                    styles["BodyTextCustom"]
                    )
            )

            elementos.append(Spacer(1, 14))

            elementos.append(
                Paragraph(
                    "Resumen Ejecutivo",
                    styles["SubHeading"]
                )
            )

            elementos.append(Spacer(1, 6))

            elementos.append(
                    Paragraph(
                        """
                        Este reporte presenta indicadores clave de la
                        población registrada, apoyando el análisis y la
                        toma de decisiones con información consolidada.
                        """,
                        styles["BodyTextCustom"]
                    )
            )

            elementos.append(Spacer(1, 14))

            secciones = {
                "Demografía": [
                    "estadisticas por edades",
                    "estadisticas por estado civil"
                ],

                "Educación": [
                    "estadisticas por nivel educativo"
                ],

                "Economía": [
                    "estadisticas por ingreso",
                    "estadisticas por empleo",
                    "estadisticas por Ingresos basados en el nivel educativo",
                    "estadisticas desempleados general",
                    "estadisticas desempleadas mujeres por edad",
                    "estadisticas empleadas mujeres por edad",
                    "estadisticas desempleados hombres por edad",
                    "estadisticas empleados hombres por edad"
                ],

                "Distribución Geográfica": [
                    "estadisticas ingresos de personas por barrios"
                ]
            }

    

            for nombre_seccion, tipos in secciones.items():

                elementos.append(PageBreak())

                elementos.append(
                    Paragraph(
                        nombre_seccion,
                        styles["SectionHeading"]
                    )
                )

                elementos.append(estilos_visuales["separator"])
                elementos.append(Spacer(1, 12))
                print("Inicio:", time.perf_counter() - t0)
                
                # Obtener todos los gráficos de esta sección en paralelo
                graficos_dict = EstadisticasServicies.getGraficosMultiples(tipos)
                
                for tipo in tipos:

                    grafico = graficos_dict.get(tipo)

                    if not grafico:
                        continue

                    elementos.append(
                        Paragraph(
                            grafico.get("titulo", tipo),
                            styles["SubHeading"]
                        )
                    )                 

                    descripcion_grafico = grafico.get("descripcion")
                    if descripcion_grafico:
                        elementos.append(
                            Paragraph(
                                descripcion_grafico,
                                styles["BodyTextCustom"]
                            )
                        )
                        elementos.append(Spacer(1, 10))

                    labels = grafico.get("labels", [])

                    for serie in grafico.get("series", []):

                        elementos.append(
                            Paragraph(
                                serie.get("nombre", "serie"),
                                styles["SubHeading2"]
                            )
                        )

                        values = serie.get("values", [])
                        img_buffer = EstadisticasServicies._generar_imagen_cached(labels, values, serie.get("nombre", "serie"))

                        elementos.append(
                            Image(
                                img_buffer,
                                width=450,
                                height=250
                            )
                        )
                        elementos.append(estilos_visuales["separator"])
                        elementos.append(
                            Spacer(1, 16)
                        )


            elementos.append(PageBreak())

            elementos.append(
                Paragraph(
                    "Conclusión",
                    styles["SectionHeading"]
                )
            )

            elementos.append(estilos_visuales["separator"])
            elementos.append(Spacer(1, 10))

            elementos.append(
                Paragraph(
                    """
                    La información presentada permite analizar
                    distintos aspectos de la población registrada,
                    incluyendo variables demográficas, educativas,
                    económicas y territoriales.
                    """,
                    styles["BodyTextCustom"]
                )
            )
            print("Graficos:", time.perf_counter() - t0)

            doc.build(elementos, onFirstPage=header_footer, onLaterPages=header_footer)
            print("PDF:", time.perf_counter() - t0)
            buffer.seek(0)

            return buffer

class RecoveryPasswordService:
    @staticmethod
    def sendEmail(email, code):
            send_mail(
            subject="Recuperación de contraseña",
            message=f"Tu código de recuperacion de 6 digitos es {code}",
            from_email="censadata@gmail.com",
            recipient_list=[email],
            fail_silently=False,
        )
    @staticmethod
    def create_recoveryCode(cuentaid):
        
        code = str(secrets.randbelow(900000) + 100000)
        RecoveryPasswordService.sendEmail(cuentaid.Correo, code)
        RecoveryPassword.objects.filter(
            cuentaid = cuentaid,
            estado = True
        ).update(estado = False)
        
        RecoveryPassword.objects.create(
            cuentaid = cuentaid,
            coderecovery = make_password(code),
            expires = timezone.now() + timezone.timedelta(minutes = 10),
            estado = True
        )
    @staticmethod
    def verifyCode(cuentaid, code):
        recovery = RecoveryPassword.objects.filter(
            cuentaid = cuentaid,
            estado = True
        ).first()
        
        if not recovery:
            raise ExcepcionNegocio("No existe una solicitud de recuperación activa para esta cuenta")
        
        if recovery.expires < timezone.now():
            raise ExcepcionNegocio("la solicitud de recuperación ha expirado")
        
        if not check_password(code,
                            recovery.coderecovery):
            raise ExcepcionNegocio("No se ha ingresado el código correcto")
        
        Token = secrets.token_urlsafe(32)
        
        recovery.tokenrecovery = Token
        recovery.estado = False
        recovery.save()
        return Token
        
    @staticmethod    
    def changePassword(token, new_password):
        
        recovery = RecoveryPassword.objects.filter(
            tokenrecovery = token
        ).first()
        
        if not recovery:
            return False
        
        User = Cuentasinvestigadoresadmin.objects.get(
            id=recovery.cuentaid.id
        )
        
        User.set_password(new_password)
        User.save()
        
        recovery.delete()
        
        return True 
    
    