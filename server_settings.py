from flask import Flask, redirect, url_for, render_template, request
from flask_socketio import SocketIO, send, emit
from flask_mysqldb import MySQL

# Create the Flask app
app = Flask(__name__)
# Create SQL Connection
mysql = MySQL(app)
# Connect to Database on localhost
#app.config['MYSQL_HOST'] = '0.0.0.0'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'root'
#app.config['MYSQL_DB'] = 'RFID2'
# Create socketio object
socketio = SocketIO(app)