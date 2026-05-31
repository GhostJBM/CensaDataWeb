from django.urls import path, include
from rest_framework import routers
from CensaData.views import *

router = routers.DefaultRouter()

router.register(r'investigadores', InvestigadoresViewSet)
router.register(r'administradores', AdministradoresViewSet)
router.register(r'cuentasInvestigadores', CuentasInvestigadoresViewSet)
router.register(r'añosEscolares', añosEscolaresViewSet)
router.register(r'añosEscolaresDocentes', añosEscolaresDocentesViewSet)
router.register(r'barrios', BarriosViewSet)
router.register(r'casas', CasasViewSet)
router.register(r'centrosEducativos', CentrosEducativosViewSet)
router.register(r'centrosEducativosDocentes', CentrosEducativosDocentesViewSet)
router.register(r'contactosCentrosEducativos', ContactosCentrosEducativosViewSet)
router.register(r'contactosDirectores', ContactosDirectoresViewSet)
router.register(r'contactosDocentes', ContactosDocentesViewSet)
router.register(r'contactosInvestigadores', ContactosInvestigadoresViewSet)
router.register(r'departamentos', DepartamentosViewSet)
router.register(r'directores', DirectoresViewSet)
router.register(r'docentes', DocentesViewSet)
router.register(r'docentesEstudiantes', DocentesEstudiantesViewSet)
router.register(r'empadronados', EmpadronadosViewSet)
router.register(r'empleos', EmpleosViewSet)
router.register(r'Censos',CensosViewSet)
router.register(r'Infraestructuras',InfraestructurasViewSet)
router.register(r'NivelesEducativos',NivelesEduactivosViewSet)
router.register(r'encuestasIniDeTrabajadores', EncuestasInideTrabajadoresViewSet)
router.register(r'encuestasMineDescoclares', EncuestasMinedEscolaresViewSet)
router.register(r'estadosCiviles', EstadosCivilesViewSet)
router.register(r'estudiantes', EstudiantesViewSet)
router.register(r'municipios', MunicipiosViewSet)
router.register(r'personas', PersonasViewSet)
router.register(r'relacionesParentescos', RelacionesParentescosViewSet)
router.register(r'tiposDeEducaciones', TiposDeEducacionesViewSet)
router.register(r'tiposDeEducacionesDocentes', TiposDeEducacionesDocentesViewSet)
router.register(r'tutores', TutoresViewSet)



urlpatterns = [path('',include(router.urls)), path('censo/', CensoCompletoINIDETrabajadoresViewSet.as_view())]

urlpatterns = [path('',include(router.urls)), path('EncuestaCompleta/', EncuestaINIDETrabajadosCompletaViewSet.as_view())]