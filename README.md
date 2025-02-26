# proyecto_tienda_comestibles
# Django 5

Instrucciones para correr.
1. crear un archivo: .env
Con los siguientes parametros de la base de datos PosgreSql:
   
DB_NAME = database_name
DB_USER = database_user
DB_PASSWORD = user_password
DB_HOST = localhost
DB_PORT = 5432  

2. Ejecutar el siguiente commando:
   python manage.py migrate
4. python manage.py runserver

   URLS activos:
   
   http://127.0.0.1:8000/categorias/
   http://127.0.0.1:8000/productos/
