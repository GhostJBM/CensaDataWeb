from django.urls import path, include
from rest_framework import routers
from CensaData.views import *
from django.contrib.auth import views as auth_views
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
router.register(r'contactosEmpadronados', ContactosEmpadronadosViewSet)
router.register(r'tiposDePisos', TiposDePisosViewSet)
router.register(r'tiposDeTechos', TiposDeTechosViewSet)
router.register(r'materialesConstrucciones', MaterialesConstruccionViewSet)
router.register(r'Discapacidades', DiscapacidadesViewSet)
router.register(r'DiscapacidadesPersonas', DiscapacidadesPersonasViewSet)


urlpatterns = [
# Tus endpoints
    path('censoCompleto/', CensoCompletoINIDETrabajadoresViewSet.as_view()),
    

    path('EncuestaCompleta/', EncuestaINIDETrabajadosCompletaViewSet.as_view()),

    path('', include(router.urls)),
    
    ## Restaurar contraseña
    path('recovery/request/', RecoveryPasswordView.as_view(), name="recovery-request"),
    path('recovery/verify/', VerificarPasswordView.as_view(), name="recovery-verify"),
    path('recovery/changePassword/', changePasswordView.as_view(), name="recovery-changePassword"),
    
    ## reportes y estadisticas
    path('estadisticas/', EstadisticasINIDEView.as_view()),
    path("reportes/pdf/", ReportesPDFview.as_view()),
    path("reportes/", ReportesINIDEView.as_view()),
    path("reportes/IsPublic/",ReportesINIDEPublicView.as_view()),
    path("reportes/publicos/pdf/", ReportesPublicosView.as_view()),
    path("reportes/publicos/", reportePublicVisitanteView.as_view())
]