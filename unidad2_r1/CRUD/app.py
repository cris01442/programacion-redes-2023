# Creando un servidor Web con Flask para proporcionar servicios
# mediante los métodos GET, PUT, DELETE, POST
# Gabriel Barrón R.

import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Establece la conexión con la base de datos
def get_db_connection():
    conn = sqlite3.connect('BaseDeDatos.db')
    conn.row_factory = sqlite3.Row
    return conn

# Método GET para obtener todos los registros de la tabla Asignaturas
@app.route('/asignaturas', methods=['GET'])
def get_asignaturas():
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Asignaturas')
    data = cursor.fetchall()
    for reg in data:
        registros.append(dict(reg))
    conn.close()
    return jsonify(registros)

# Método GET para obtener todos los registros de la tabla Estudiantes
@app.route('/estudiantes', methods=['GET'])
def get_estudiantes():
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Estudiantes')
    data = cursor.fetchall()
    for reg in data:
        registros.append(dict(reg))
    conn.close()
    return jsonify(registros)

# Método PUT para crear un registro en la tabla Asignaturas
@app.route('/asignaturas', methods=['PUT'])
def create_asignatura():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO Asignaturas (id, nombre, descripcion, creditos, nivel, profesor, horario, salon) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(insert, (record['id'], record['nombre'], record['descripcion'], record['creditos'], record['nivel'], record['profesor'], record['horario'], record['salon']))
    conn.commit()
    return jsonify(record)

# Método PUT para crear un registro en la tabla Estudiantes
@app.route('/estudiantes', methods=['PUT'])
def create_estudiante():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO Estudiantes (id, idAsignatura, nombre, apellido, fechaNacimiento, genero, direccion, telefono, email, promedio, fechaIngreso) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(insert, (record['id'], record['idAsignatura'], record['nombre'], record['apellido'], record['fechaNacimiento'], record['genero'], record['direccion'], record['telefono'], record['email'], record['promedio'], record['fechaIngreso']))
    conn.commit()
    return jsonify(record)

# Método DELETE para eliminar un registro de la tabla Asignaturas
@app.route('/asignaturas', methods=['DELETE'])
def delete_asignatura():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM Asignaturas WHERE id = ?'
    cursor.execute(delete, (record['id'],))
    conn.commit()
    return jsonify(record)

# Método DELETE para eliminar un registro de la tabla Estudiantes
@app.route('/estudiantes', methods=['DELETE'])
def delete_estudiante():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM Estudiantes WHERE id = ?'
    cursor.execute(delete, (record['id'],))
    conn.commit()
    return jsonify(record)

# Método POST para actualizar un registro en la tabla Asignaturas
@app.route('/asignaturas', methods=['POST'])
def update_asignatura():
    record = json.loads(request.data)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    update = 'UPDATE Asignaturas SET nombre = ?, descripcion = ?, creditos = ?, nivel = ?, profesor = ?, horario = ?, salon = ? WHERE id = ?'
    cursor.execute(update, (record['nombre'], record['descripcion'], record['creditos'], record['nivel'], record['profesor'], record['horario'], record['salon'], record['id']))
    conn.commit()
    return jsonify(record)

# Método POST para actualizar un registro en la tabla Estudiantes
@app.route('/estudiantes', methods=['POST'])
def update_estudiante():
    record = json.loads(request.data)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    update = 'UPDATE Estudiantes SET idAsignatura = ?, nombre = ?, apellido = ?, fechaNacimiento = ?, genero = ?, direccion = ?, telefono = ?, email = ?, promedio = ?, fechaIngreso = ? WHERE id = ?'
    cursor.execute(update, (record['idAsignatura'], record['nombre'], record['apellido'], record['fechaNacimiento'], record['genero'], record['direccion'], record['telefono'], record['email'], record['promedio'], record['fechaIngreso'], record['id']))
    conn.commit()
    return jsonify(record)

# Inicia el servicio
if __name__ == '__main__':
    app.run(debug=True)
