Microservicio de Archivos con Flask y Docker

Este repositorio contiene un simple microservicio de archivos implementado en Python con Flask y Docker. El microservicio permite realizar operaciones básicas en archivos, como obtener el contenido de un archivo, listar archivos disponibles y eliminar archivos.

Contenido del Repositorio
app.py: Este archivo contiene la implementación del servidor Flask que maneja las operaciones relacionadas con archivos. Proporciona tres endpoints principales:

/get_file/<filename>: Obtiene el contenido de un archivo específico.
/list_files: Lista todos los archivos disponibles.
/delete_file/<filename>: Elimina un archivo específico.
script_docker.py: Este script se encarga de construir, ejecutar y detener el contenedor Docker que aloja el microservicio. También realiza algunas solicitudes de prueba a la API después de que el contenedor esté en funcionamiento.

Dockerfile: El archivo de configuración de Docker que define la imagen del contenedor. Utiliza la imagen base de Python 3.8, instala las dependencias especificadas en requirements.txt y configura el comando para ejecutar la aplicación Flask.

requirements.txt: Archivo que enumera las dependencias de Python necesarias para ejecutar la aplicación, en este caso, Flask.

Instrucciones de Uso
Requisitos Previos
Asegúrate de tener Docker instalado en tu sistema.

Pasos para Ejecutar
Ejecuta el siguiente comando en la terminal desde el directorio raíz del repositorio para ejecutar el script
Python3 script_docker.py

Notas Adicionales
La aplicación Flask se ejecuta en el puerto 5000, asegúrate de que este puerto esté disponible en tu sistema.
El contenido de los archivos se almacena en el directorio archivos. Asegúrate de que este directorio esté presente y accesible para el contenedor.
Ajusta los tiempos de espera en el script según sea necesario para garantizar que las operaciones se realicen después de que el contenedor esté completamente en funcionamiento.
¡Disfruta explorando y utilizando este simple microservicio de archivos!





