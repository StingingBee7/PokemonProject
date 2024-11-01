import flask
from flask import request, jsonify
from config import *
import pymysql.cursors
from rds_connection import start_rds_connection


app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/api/v1/resources/mons', methods = ['GET'])

def pokemon_type():
    if 'Type' in request.args:
        Type = str(request.args['Type'])
    else:
        return "Error: No type provided. Please specify a type."


    connection = start_rds_connection()

    with connection.cursor() as cursor:
        sql = f'SELECT * FROM pokemonstats WHERE Type = {Type}'
        cursor.execute(sql)
        result = cursor.fetchall()
    return jsonify(result)
