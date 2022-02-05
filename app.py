from models import Book, Category, setup_db, db
from flask import Flask
from flask import jsonify, request, abort
from flask_migrate import Migrate

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

    @app.route('/books/categories/<int:id>')
    def book_category(id):
        category = Category.query.get(id)
        books = Book.query.filter_by(categorie_id=id).all()
        books = paginate(books)
        return jsonify({
            'Success': True,
            'Status_code': 200,
            'classe': category.format(),
            'books': books 
        })

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
