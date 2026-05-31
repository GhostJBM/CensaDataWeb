## Distintos servicios del proyecto
from django.db import transaction 
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
import math

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
    class validacionesBarrios:
        def valiExiste(data): 
            try:
               if Barrios.objects.filter(nombre=data["nombre"], municipioid_id=data["municipioid"]).exists():
                raise ExcepcionNegocio("El Barrio Ya existe")
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


class GetElement:
    pass

class GetAllElement:
    pass
