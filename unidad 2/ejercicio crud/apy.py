# Creando un servidor Web con Flask para proporcionar servicios
# mediante los métodos GET, PUT, DELETE, POST
# Jose Manuel Gutierrez

import json
import sqlite3
from flask import Flask, request, jsonify


app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('crud.db')
    conn.row_factory = sqlite3.Row
    return conn


# Método GET donde busca un nombre
@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM doctores')
    data = cursor.fetchall()
    for reg in data:
       registros.append(dict(reg))
    conn.close()
    return jsonify(json.dumps(registros))

@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO doctores(name,  edad, sexo, peso,  altura, especialidad,  email,  telefono ) VALUES(?,?,?,?,?,?,?,?)'
    cursor.execute(insert, [record['name'], record['edad'], record['sexo'], record['peso'], record['altura'],record['especialidad'], record['email'], record['telefono'] ])
    conn.commit()
    return jsonify(record)

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
   
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'UPDATE doctores SET email = ? WHERE name= ?'
    cursor.execute(delete, [record['email'], record['name']])
    conn.commit()
    return jsonify(record)

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
   
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM doctores WHERE name= ?'
    cursor.execute(delete, [record['name']])
    conn.commit()
    return jsonify(record)




app.run(debug=True)