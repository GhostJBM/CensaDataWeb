from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from CensaData.views import meViewSet
from django.http import HttpResponse
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from CensaData.views import CustomeTokenObtainPairView

schema_view = get_schema_view(
    openapi.Info(
        title="CensaData API",
        default_version='v2',
        description="API documentation for CensaData project",
    ),
    public=True,
    
    permission_classes=[permissions.AllowAny],
)

def home(request):
    return HttpResponse("OK")

urlpatterns = [
    path("",home),
    path('admin/', admin.site.urls),

    path('api/', include('CensaData.urls')), 
    path('me/', meViewSet.as_view(), name='me'),
    path('api/token/', CustomeTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    
    path('', include('django_prometheus.urls')),
    path("silk/", include('silk.urls'), name='silk')
]


        