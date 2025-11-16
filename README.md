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
   3. Generar el virtual enviroment (.venv) si no está generado.
    ``
      python -m venv .venv
    ``
```
   python -m venv .venv
```
   
   4. Instalar las librerías necesarias.

     pip install django==5.2.7
     pip install django-mssql-backend==2.8.1
     pip install djangorestframework==3.16.1
     pip install djangorestframework-simplejwt==5.5.1
     pip install drf-yasg==1.21.11
     pip install pyodbc==5.3.0
     pip install mssql-django==1.6
   
   5. Configurar la conexión con la base de datos en el config del framework.
      5.1 ejecutamos el archivo loginMaster.sql en DB/Seguridad/Logins
      5.2 Ejecutamos los archivo en DB/Seguridad/Roles AdministradorRole.sql y InvestigadorRole.sql
      5.3 Ejecutamos el archivo Usuarios.sql en DB/Seguridad/logins
      5.4 ejectuamos todos los archivos en DB/Triggers y procedimientos almacenados
      5.5 nos conectamos al servidor de BD con el UsuarioAdministrador en caso de querer acceso total o con el UsuarioInvestigador en caso de querer acceso limitado
      5.6 Cambiamos la contraseña del usuario como se nos indica en el Managaments Studio
      5.7 Cambios el usuario y la contraseña en CensaData/config/settings.py
         DATABASES = {
            'default': {
               'ENGINE': 'mssql',  
               'NAME': 'CensaData',      
               'HOST': 'localhost\\SQLEXPRESS',  #coloque su servidor de db        
               'USER':'UsuarioAdministrador',    #UsuarioAdministrador o UsuarioInvestigador
               "PASSWORD":'Login',               #Contraseña cambiada previamente
               'PORT': '',               
               'OPTIONS': {
                  'driver': 'ODBC Driver 17 for SQL Server', # driver de sql server
            },
    }
}
   6. Correr el servidor local.

   ```
   python manage.py runserver
   ```
   
   7. Probar los endpoints haciendo uso del JWT.
      Para la documentación el equipo implemento una libreria con la cual atravez de un ENDPoint usted puede descargarla e importarla a aplicaciones como postman o APIDog por ejemplo; el end point es:
      -su servidor-/redoc/ ejemplo http://127.0.0.1:8000/redoc/, le da en download y tiene la documentacion de las apis del proyecto en caso de errores puede contactar con el equipo


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
├── DB/                     # Carpeta para scripts SQL
|   ├── Seguridad/          # Carpeta con los scripts de logins y roles de la base de datos(necesaria)
|   |   ├── logins/         # Carpeta con los logins del proyecto
|   |   |   ├── LoginsMaster.sql        #logins del proyecto para la conexión entre el backend y la bd
|   |   └── Roles/                      #carpeta con los roles de la bd
|   |       ├── AdministradorRole.sql
|   |       └── InvestigadorRole.sql
|   ├── Triggers y procedimientos almacenados/         #carpeta con los trigger y procedure de la bd
|   |   ├── Procedimientos Almacenados y funciones.sql
|   |   └── TriggersCantidades.sql
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
