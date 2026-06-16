# CensaDataWeb
Aplicacion web como proyecto integrador de estudiantes de segundo año de Ingeniería en Sistemas destinada a la gestión de censos de las diferentes instituciones del país (INIDE y MINED por ahora).

## Tecnologías usadas.
- Python 3.12.6
- Django Rest Framework.
- SQL Server Management Studio (SQL Server).
- SWAGGER/OPENAPI.
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
   2. restaurar la bd alojado en [Base de datos](https://github.com/GhostJBM/CensaDataWeb/tree/main/DB).
   3. Generar el virtual enviroment (.venv) si no está generado.
    ``
      python -m venv .venv
    ``
```
   python -m venv .venv
```
   
   4. Instalar las librerías necesarias.

     pip install django==5.2.7
      pip install gunicorn==26.0.0
      pip install django-cors-headers==4.9.0
      pip install whitenoise==6.12.0
      pip install pandas==3.0.3
      pip install reportlab==4.5.1
      pip install aws==0.2.5
      pip install bcrypt==5.0.0
      pip install boto==2.49.0
      pip install cffi==2.0.0
      pip install cryptography==46.0.3
      pip install decorator==5.2.1
      pip install Deprecated==1.3.1
      pip install djangorestframework==3.16.1
      pip install djangorestframework_simplejwt==5.5.1
      pip install drf-yasg==1.21.11
      pip install fabric==3.2.2
      pip install inflection==0.5.1
      pip install invoke==2.2.1
      pip install mssql-django==1.6
      pip install packaging==25.0
      pip install paramiko==4.0.0
      pip install prettytable==3.17.0
      pip install pycparser==2.23
      pip install pydantic==2.13.3
      pip install pydantic_core==2.46.3
      pip install PyJWT==2.10.1
      pip install PyNaCl==1.6.1
      pip install pyodbc==5.3.0
      pip install pytz==2025.2
      pip install PyYAML==6.0.3
      pip install sqlparse==0.5.3
      pip install typing-inspection==0.4.2
      pip install typing_extensions==4.15.0
      pip install tzdata==2025.2
      pip install uritemplate==4.2.0
      pip install wcwidth==0.2.14
      pip install wrapt==2.0.1
      pip install matplotlib==3.10.9
      pip install python-dotenv==1.2.2
   
   5. Configurar la conexión con la base de datos en el config del framework.
      - 5.1 Ejecutamos el archivo loginMaster.sql en DB/Seguridad/Logins
      - 5.2 Ejecutamos los archivo en DB/Seguridad/Roles AdministradorRole.sql y InvestigadorRole.sql
      - 5.3 Ejecutamos el archivo Usuarios.sql en DB/Seguridad/logins
      - 5.4 Ejectuamos todos los archivos en DB/Triggers y procedimientos almacenados 
      - 5.5 Nos conectamos al servidor de BD con el UsuarioAdministrador en caso de querer acceso total o con el UsuarioInvestigador en caso de querer acceso limitado
      - 5.6 Cambiamos la contraseña del usuario en caso de que lo requeramos y en las .env cambios las credenciales viejas por las nuevas.
      - 5.7 Cambios el usuario y la contraseña en CensaData/config/settings.py
```plaintext
       DATABASES = {
            'default': {
        'ENGINE': 'mssql',  
        'NAME': 'CensaData',      
        'HOST': os.getenv("HOST_NAME"),        
        'USER': os.getenv("DB_USER_NAME"),
        "PASSWORD":os.getenv("DB_PASSWORD"),  
        'PORT': '1433',               
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'Encrypt': 'yes',
            'TrustServerCertificate': 'no',
            'charset':'utf8mb4',
            'use_unicode':True,
            'conection_timeout': 30,
      },
   }
}

      6.1 Crear las migraciones a la bd
      python manage.py migrate
```
   7. Correr el servidor local.

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
│   ├── estadisticas/       #Estadisticas simulando el DW
│   ├      ├── Datast_censadata.csv
│   ├      ├── Ceensadataset.ipynb
│   ├      └── graficos.py               
│   ├── migrations/         # Migraciones de la base de datos
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py  # Modelos de datos
|   ├── services.py # services layer/ logica y validaciones       
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
