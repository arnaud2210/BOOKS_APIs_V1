import json
from os import abort
from models import app, Book, Category
from flask import jsonify


# fonction permettant de lister les éléments d'une liste


def paginate(request):
    items = [item.format() for item in request]
    return items

# Lister tous les livres


@app.route('/books')
def get_books():
    books = Book.query.all()
    books = paginate(books)
    if books is None:
        abort(404)
    else:
        return jsonify({
            'success': True,
            'status': 200,
            'books': books,
            'total_books': len(books)
        })


# chercher un livre en particulier par son id
@app.route('/books/<int:id>')
def get_book(id):
    book = Book.query.get(id)
    if book is None:
        abort(404)
    else:
        return jsonify({
            'success': True,
            'status': 200,
            'book': book.format()
        })


# Lister la liste des livres d'une categorie
@app.route('/categories/<int:id>/books')
def book_category(id):
    category = Category.query.get(id)


# Lister toutes les categories


@app.route('/categories')
def get_categories():
    categories = Category.query.all()
    categories = paginate(categories)
    if categories is None:
        abort(404)
    else:
        return jsonify({
            'success': True,
            'status': 200,
            'category': categories,
            'total': len(categories)
        })


# chercher une categorie par son id


@app.route('/categories/<int:id>')
def get_category(id):
    category = Category.query.get(id)
    if category is None:
        abort(404)
    else:
        return jsonify({
            'success': True,
            'status': 200,
            'category': category.format()
        })


# supprimer un livre
@app.route('/books/<int:id>', methods=['DELETE'])
def del_book(id):
    book = Book.query.get(id)
    book.delete()
    return jsonify({
        'success': True,
        'id_book': id,
        'new_total': Book.query.count()
    })


# supprimer une categorie
@app.route('/categories/<int:id>', methods=['DELETE'])
def del_category(id):
    category = Category.query.get(id)
    category.delete()
    return jsonify({
        'success': True,
        'status': 200,
        'id_cat': id,
        'new_total': Category.query.count()
    })
