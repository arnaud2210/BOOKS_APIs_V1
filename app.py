from models import Book, Category, setup_db, db
from flask import Flask
from flask import jsonify, request, abort
from flask_migrate import Migrate
from flask_cors import CORS

#############################################################
# fonction permettant d'afficher les éléments d'une liste
#############################################################


def paginate(request):
    items = [item.format() for item in request]
    return items

##############################
# Lister tous les livres
##############################


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    migrate = Migrate(app, db)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

    """@app.route('/v1/')
    def welcome():
        return jsonify({
            "message": "WELCOME !",
            "name": "bookapi",
            "version": 1,
            "read":"https://github.com/arnaud2210/BOOKS_APIs_V1"
        })"""

    @app.route('/books')
    def get_books():
        try:
            books = Book.query.all()
            books = paginate(books)
            return jsonify({
                'success': True,
                'status_code': 200,
                'books': books,
                'total_books': len(books)
            })
        except:
            abort(404)
        finally:
            db.session.close()

    #################################################
    # Chercher un livre en particulier par son id
    #################################################

    @app.route('/books/<int:id>')
    def get_book(id):
        book = Book.query.get(id)
        if book is None:
            abort(404)
        else:
            return book.format()

    ################################################
    # Lister la liste des livres d'une categorie
    ################################################

    @app.route('/categories/<int:id>/books')
    def book_category(id):
        try:
            category = Category.query.get(id)
            books = Book.query.filter_by(categorie_id=id).all()
            books = paginate(books)
            return jsonify({
                'Success': True,
                'Status_code': 200,
                'total': len(books),
                'classe': category.format(),
                'books': books
            })
        except:
            abort(404)
        finally:
            db.session.close()

    #######################################
    # Lister toutes les categories
    #######################################

    @app.route('/categories')
    def get_categories():
        categories = Category.query.all()
        categories = paginate(categories)
        if categories is None:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'status_code': 200,
                'category': categories,
                'total': len(categories)
            })

    ########################################
    # Chercher une categorie par son id
    ########################################

    @app.route('/categories/<int:id>')
    def get_category(id):
        category = Category.query.get(id)
        if category is None:
            abort(404)
        else:
            return category.format()

    ############################
    # Supprimer un livre
    ############################

    @app.route('/books/<int:id>', methods=['DELETE'])
    def del_book(id):
        try:
            book = Book.query.get(id)
            book.delete()
            return jsonify({
                'success': True,
                'id_book': id,
                'new_total': Book.query.count()
            })
        except:
            abort(404)
        finally:
            db.session.close()

    #############################
    # Supprimer une categorie
    #############################

    @app.route('/categories/<int:id>', methods=['DELETE'])
    def del_category(id):
        try:
            category = Category.query.get(id)
            category.delete()
            return jsonify({
                'success': True,
                'status': 200,
                'id_cat': id,
                'new_total': Category.query.count()
            })
        except:
            abort(404)
        finally:
            db.session.close()

    ###########################################
    # Modifier les informations d'un livre
    ###########################################

    @app.route('/books/<int:id>', methods=['PATCH'])
    def change_book(id):
        body = request.get_json()
        book = Book.query.get(id)
        try:
            if 'titre' in body and 'auteur' in body and 'editeur' in body:
                book.titre = body['titre']
                book.auteur = body['auteur']
                book.editeur = body['editeur']
            book.update()
            return book.format()
        except:
            abort(404)

    ########################################
    # Modifier le libellé d'une categorie
    ########################################

    @app.route('/categories/<int:id>', methods=['PATCH'])
    def change_name(id):
        body = request.get_json()
        category = Category.query.get(id)
        try:
            if 'categorie' in body:
                category.libelle_categorie = body['categorie']
            category.update()
            return category.format()
        except:
            abort(404)

    ##############################################
    # Rechercher un livre par son titre ou son auteur
    ##############################################
    @app.route('/books/<string:word>')
    def search_book(word):
        mot = '%'+word+'%'
        titre = Book.query.filter(Book.titre.like(mot)).all()
        titre = paginate(titre)
        return jsonify({
            'books': titre
        })

    @app.route('/categories', methods=['POST'])
    def add_category():
        body = request.get_json()
        new_categorie = body['libelle_categorie']
        category = Category(libelle_categorie=new_categorie)
        category.insert()
        return jsonify({
            'success': True,
            'added': category.format(),
            'total_categories': Category.query.count()
        })

    @app.route('/books', methods=['POST'])
    def add_book():
        body = request.get_json()
        isbn = body['code_ISBN']
        new_titre = body['titre']
        new_date = body['date_publication']
        new_auteur = body['auteur']
        new_editeur = body['editeur']
        categorie_id = body['categorie_id']
        book = Book(isbn=isbn, titre=new_titre, date_publication=new_date,
                    auteur=new_auteur, editeur=new_editeur, categorie_id=categorie_id)
        book.insert()
        count = Book.query.count()
        return jsonify({
            'success': True,
            'added': book.format(),
            'total_books': count,
        })

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': "Ressource non disponible"
        }), 404

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=False)
