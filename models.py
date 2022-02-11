import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
import postgres
load_dotenv()

database = 'library'
passw = os.getenv('db_pass')

db_path = "postgresql://vojabfzacqpmcl:e3b72026821fbfb5fb89995cf40c35d1eb3cd8dc16a7283c45afdd09c0a81f23@ec2-50-19-32-96.compute-1.amazonaws.com:5432/dbjq4p5nchq6fg"

db = SQLAlchemy()


def setup_db(app, path=db_path):

    app.config['SQLALCHEMY_DATABASE_URI'] = db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)
    db.create_all()


class Category(db.Model):

    __tablename__ = 'categories'

    id_cat = db.Column(db.Integer, primary_key=True)
    libelle_categorie = db.Column(db.String(50))
    books = db.relationship('Book', backref='categories', lazy=True)

    def __init__(self, libelle_categorie):
        self.libelle_categorie = libelle_categorie

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id_cat,
            'categorie': self.libelle_categorie
        }


class Book(db.Model):

    __tablename__ = 'books'

    id_book = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(12), nullable=False)
    titre = db.Column(db.String(200), nullable=False)
    date_publication = db.Column(db.String(10), nullable=False)
    auteur = db.Column(db.String(200), nullable=False)
    editeur = db.Column(db.String(150), nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey(
        'categories.id_cat'), nullable=False)

    def __init__(self, isbn, titre, date_publication, auteur, editeur, categorie_id):
        self.isbn = isbn
        self.titre = titre
        self.date_publication = date_publication
        self.auteur = auteur
        self.editeur = editeur
        self.categorie_id = categorie_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id_book,
            'code_ISBN': self.isbn,
            'titre': self.titre,
            'auteur': self.auteur,
            'editeur': self.editeur,
            'date_publication': self.date_publication
        }

