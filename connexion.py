from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

database = 'library'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}/{}'.format(
    'naud', 'naud.2002', 'localhost:5432', database)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
