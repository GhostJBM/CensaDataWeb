# CensaDataWeb
Aplicacion web como proyecto integrador de estudiantes de segundo año de Ingeniería en Sistemas destinada a la gestión de censos de las diferentes instituciones del país (INIDE y MINED por ahora).

## Tecnologías usadas.
- Python 3.12.6
- Django Rest Framework.
- SQL Server Management Studio (SQL Server).
- API Dog.
- Visual studio code.
- Github.

## Instalación.
### Requerimientos.
   - Python 3.12.6.
   - Django 4+.
   - SQL Server.
   - pip / virtual enviroment (.venv).
### Setup.
   1. Clonar el repositorio github.
   2. Correr el script DML Y DDL de la base de datos alojado en [Base de datos](https://github.com/GhostJBM/CensaDataWeb/tree/main/DB).
   4. Generar el virtual enviroment (.venv) si no está generado.
```
   python -m venv .venv
```
   3. Instalar las librerías necesarias.

     pip install django==5.2.7
     pip install django-mssql-backend==2.8.1
     pip install djangorestframework==3.16.1
     pip install djangorestframework-simplejwt==5.5.1
     pip install drf-yasg==1.21.11
     pip install pyodbc==5.3.0
     pip install mssql-django==1.6
   
   4. Configurar la conexión con la base de datos en el config del framework.
   5. Correr el servidor local.

   ```
   python manage.py runserver
   ```
   
   6. Probar los endpoints haciendo uso del JWT.

## Estructura del proyecto.
```plaintext
CensaDataWeb/
├── .venv/                 
├── CensaData/                 
│   ├── migrations/         # Migraciones de la base de datos
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py           # Modelos de datos
│   ├── permissions.py 
│   ├── serializers.py      # Serializadores para DRF
│   ├── test.py
│   ├── urls.py             # Rutas específicas de la app
│   └── views.py            # Vistas de la app 
├── DB/                     # Carpeta opcional para scripts SQL
│   ├── CensaDataDDL.sql
│   └── CensaDataDML.sql
├── config/                 # Carpeta principal del proyecto Django
│   ├── __init__.py
│   ├── asgi.py             # Configuración para ASGI
│   ├── settings.py         # Configuración del proyecto (incluye DB)
│   ├── urls.py             # Rutas globales
│   └── wsgi.py             # Configuración para WSGI
├── LICENSE
├── README.md               # Documentación del proyecto
└── manage.py
```
## Licencia.
Este proyecto está bajo licencia de Apache License 2.0
## Autores.
- Adrian Antonio Medina Cubillo.
- Francisco Jose Moncada Mejia.
- Josiel Benavidez Morales.
