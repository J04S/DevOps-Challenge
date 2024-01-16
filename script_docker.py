import os
import subprocess
import requests
import time
from flask import Flask

app = Flask(__name__)

ARCHIVOS_DIR = "archivos"
API_URL = "http://127.0.0.1:5000"  # Cambia esto si tu aplicación se ejecuta en un puerto diferente
CONTAINER_ID = None  # Variable para almacenar el identificador del contenedor


def ejecutar_servidor_flask():
    app.run(host='0.0.0.0', port=5000)

def construir_contenedor():
    try:
        subprocess.run(["docker", "build", "-t", "my_python_microservice", "."], check=True)
        print("Imagen Docker construida exitosamente.")
    except subprocess.CalledProcessError as e:
         print(f"Error al ejecutar el contenedor Docker. Código de salida: {e.returncode}")
         print(f"Salida estándar: {e.stdout}")
         print(f"Error estándar: {e.stderr}")

def ejecutar_contenedor():
    global CONTAINER_ID  # Necesitas declarar la variable global

    try:
        # Ejecuta el contenedor y obtén el identificador
        result = subprocess.run(["docker", "run", "-p", "5000:5000", "-d","my_python_microservice"], check=True, capture_output=True)
        CONTAINER_ID = result.stdout.decode().strip()
        print("Contenedor Docker ejecutándose en el puerto 5000. ID:", CONTAINER_ID)

    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el contenedor Docker: {e}")

def detener_contenedor():
    global CONTAINER_ID

    if CONTAINER_ID:
        try:
            # Detén el contenedor usando el identificador
            subprocess.run(["docker", "stop", CONTAINER_ID], check=True)
            print("Contenedor Docker detenido.")
        except subprocess.CalledProcessError as e:
            print(f"Error al detener el contenedor Docker: {e}")

def realizar_peticiones_api():
    # Peticiones a la API después de levantar el contenedor
    try:
        # Obtener un archivo
        filename = "file1"
        response = requests.get(f"{API_URL}/get_file/{filename}")
        print("Respuesta de obtener archivo:", response.json())

        # Listar archivos
        response = requests.get(f"{API_URL}/list_files")
        print("Listado de archivos:", response.json())

        # Eliminar un archivo
        filename = "file5"
        response = requests.delete(f"{API_URL}/delete_file/{filename}")
        print("Respuesta de eliminar archivo:", response.json())

    except Exception as e:
        print(f"Error al realizar peticiones a la API: {e}")
    finally:
        # Detener el contenedor después de realizar las peticiones
        detener_contenedor()

if __name__ == "__main__":
    construir_contenedor()
    ejecutar_contenedor()
    time.sleep(10)  # Esperar 10 segundos (ajusta según sea necesario)
    realizar_peticiones_api()

