from django.urls import path, include
from rest_framework import routers
from CensaData.views import AdministradoresViewSet, InvestigadoresViewSet

urlpatterns = [
    path('api/', include('CensaData.urls')), 
]
