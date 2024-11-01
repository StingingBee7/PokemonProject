import pymysql.cursors
from config import *

def start_rds_connection():
    print(USERNAME,PASSWORD,PORT)
    try:
        connection = pymysql.connect(host=ENDPOINT, port=PORT,user=USERNAME, password=PASSWORD, db = DBNAME, cursorclass=CURSORCLASS, ssl_ca=SSL_CA)
        print('RDS Connection Successful')
    except Exception as e:
        print(f'RDS Connection Failed: {e}')
        connection = None
    return connection

connection = start_rds_connection()

with connection.cursor() as cursor:
    sql = f'SELECT * FROM pokemonstats'
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

connection.commit()
