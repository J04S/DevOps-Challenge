import os
from flask import Flask, request, jsonify

app = Flask(__name__)

ARCHIVOS_DIR = "archivos"

# Endpoint para solicitar un archivo
@app.route('/get_file/<filename>', methods=['GET'])
def get_file(filename):
    file_path = os.path.join(ARCHIVOS_DIR, filename)

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            return jsonify({"filename": filename, "content": content})
    else:
        return jsonify({"error": "Archivo no encontrado"}), 404

# Endpoint para listar los archivos disponibles
@app.route('/list_files', methods=['GET'])
def list_files():
    files = os.listdir(ARCHIVOS_DIR)
    return jsonify({"files": files})

# Endpoint para borrar un archivo
@app.route('/delete_file/<filename>', methods=['DELETE'])
def delete_file(filename):
    file_path = os.path.join(ARCHIVOS_DIR, filename)

    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({"message": f"Archivo {filename} eliminado"})
    else:
        return jsonify({"error": "Archivo no encontrado"}), 404

if __name__ == '__main__':
    if not os.path.exists(ARCHIVOS_DIR):
        os.makedirs(ARCHIVOS_DIR)
    app.run(host='0.0.0.0', port=5000)
