import json
from flask import Flask, jsonify, request
from config import config
from flaskext.mysql import MySQL

application = Flask(__name__)
application.config.from_object(config['development'])

conexion = MySQL(application)

@application.route('/')
def hello_world():
    return "Hola Mundo"

@application.route('/containers/<json_obj>', methods=['POST'])
def hellow_world(json_obj):
    try:
        jsonn = request.get_json(json_obj)
        #print(request.json['listaContenedores'])
        print(jsonn["presupuesto"])
        listaContenedores = jsonn['listaContenedores']
        print("--------------------------------------------")
        for data in listaContenedores:
            print("Nombre: ", data["nombreContenedor"])
            print("Costo: ", data["costo"])
            print("KPI: ", data["kpi"])
        return jsonify({'Mensaje': 'Contenedor Registrado'})
    except Exception as e:
        return jsonify({'Mensaje': 'Error'})