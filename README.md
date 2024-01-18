Microservicio Flask con Docker

Este repositorio contiene un microservicio simple en Flask para gestionar operaciones de archivos dentro de un contenedor Docker. El microservicio proporciona puntos finales para recuperar, listar y eliminar archivos. Además, se incluyen scripts de automatización para construir, ejecutar y probar el microservicio utilizando Docker.

Estructura de Archivos
app.py: El script principal en Python que implementa el microservicio Flask.
Dockerfile: Archivo de configuración para construir la imagen de Docker.
script_docker.py: Script de automatización para construir, ejecutar y probar el microservicio con Docker.

Uso:
Construir la Imagen de Docker --> Este script automatiza el proceso de construcción de la imagen de Docker. Utiliza el Dockerfile para crear una imagen llamada my_python_microservice.

Ejecutar el Contenedor Docker --> El script ejecuta el contenedor Docker, mapeando el puerto 5000 en el host al puerto 5000 en el contenedor. El microservicio Flask estará accesible en http://127.0.0.1:5000.

Probar el Microservicio
Después de ejecutar el contenedor, el script envía solicitudes HTTP de ejemplo al microservicio para probar su funcionalidad.
El script de prueba realiza las siguientes acciones:
  -Obtiene el contenido de un archivo (file1 en este ejemplo).
  -Lista todos los archivos disponibles.
  -Elimina un archivo (file5 en este ejemplo).

Detener el Contenedor Docker --> El script detiene automáticamente el contenedor Docker después de la prueba.

Estructura de Directorios

-archivos/: Directorio donde se almacenan los archivos dentro del contenedor.
-app.py: Implementación del microservicio Flask.
-Dockerfile: Archivo de configuración para construir la imagen de Docker.
-script_docker.py: Script de automatización para construir, ejecutar y probar el microservicio.

Notas
-Asegúrate de que Docker esté instalado en tu sistema antes de ejecutar el script de automatización.
-Ajusta el tiempo de espera en time.sleep(10) en script_docker.py si es necesario para permitir que el contenedor se inicialice completamente antes de la prueba.
