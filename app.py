from flask import Flask
from config.db_config import PostgreSQL

app = Flask(__name__)

coone = PostgreSQL(database='backendatlauncher', host = 'localhost', password = '142536', user = 'postgres')
coone.connection
print('Conectado')

app.run(port=5000, host='localhost', debug=True)