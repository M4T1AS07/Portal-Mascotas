README -- Portal de Adopción de Mascotas
-------------------------------
Este proyecto es un portal de adopción de mascotas desarrollado con el framework Django.
Permite:

-Registrar y mostrar mascotas.
-Filtrar por especie, edad y ubicación.
-Enviar solicitudes de adopción.
-Administrar datos desde el panel de Django Admin.

Requisitos
-----------
Antes de comenzar, asegúrate de tener instalado en tu computadora:

-Python 3.10 o superior
-pip (gestor de paquetes de Python, viene con Python)
-SQLite (ya viene incluido con Python, no necesitas instalar nada extra)

Y si no lo tiene instalado el comando para instalarlo es el siguiente:
-sudo apt install python3
-python3 --versión (sirve para verificar la versión instalada de Python)

Instalación
------------
1.Descargar o descomprimir el proyecto
Extrae la carpeta del proyecto en tu computadora.

2.Abrir la terminal en la carpeta del proyecto
Es decir, cd portaladopcion donde está el archivo manage.py.

3.Instalar dependencias necesarias
Ejecuta en la terminal:

-pip install Django
-pip install pillow

-Django es el framework web.
-Pillow permite manejar imágenes de mascotas.


4.Aplicar migraciones (crear base de datos):
Python manage.py migrate


5.Iniciar el servidor de desarrollo:
Python manage.py runserver

6.Abrir en el navegador:
 http://127.0.0.1:8000/


Estructura del proyecto
-------------------------
portaladopcion/
│
├── manage.py              # Archivo principal de Django
├── db.sqlite3             # Base de datos SQLite
├── portal/                # Aplicación principal con modelos, vistas y templates
├── mascotas/              # Carpeta con imágenes subidas de mascotas
└── templates/             # Archivos HTML del portal


Notas importantes
------------------
Las imágenes de las mascotas se guardan en la carpeta mascotas/.

Si deseas entrar al panel de administración de Django:
 1.Crea un superusuario con:
Python manage.py createsuperuser

 2.Luego ingresa en:
http://127.0.0.1:8000/admin/

Con esto ya deberías poder ejecutar y usar el Portal de Adopción de Mascotas fácilmente.

Grupo: Renato Briones, Roberto Rengifo, Matias Paredes 
