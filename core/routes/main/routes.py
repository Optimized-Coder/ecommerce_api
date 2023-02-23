from . import bp as main
from flask import jsonify, request, render_template, redirect, url_for
from ...models.products import Product
from ... import db


@main.route('/')
def index():
    
    context = {
        'title': 'Home',
        'Product': Product
    }

    return render_template(
        'index.html',
        **context
    )

@main.route('/add/', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        price = request.form.get('price')
        genre = request.form.get('genre')
        description = request.form.get('description')

        new_product = Product(
            title = title,
            author = author,
            genre = genre,
            price = float(price),
            description = description
        )

        db.session.add(new_product)
        db.session.commit()
        print(f'{new_product.title} created')

        return redirect(url_for('products.index'))

    context = {
        'title': 'Add Product',
    }

    return render_template(
        'admin/add.html',
        **context
    )

# 
@main.route('/<int:id>/delete/', methods=['DELETE', 'GET'])
def delete_product(id):
    record = Product.query.filter_by(id=id).first()
    db.session.delete(record)
    db.session.commit()

    return redirect(url_for('products.index'))

@main.route('/<int:id>/edit/', methods=['GET', 'PUT'])
def edit_record(id):
    record = Product.query.filter_by(id=id).first()
    if request.method == 'PUT':

        record.title = request.form.get('title')
        record.author = request.form.get('author')
        record.price = request.form.get('price')
        record.gemre = request.form.get('genre')
        record.description = request.form.get('description')


    context = {
        'title': 'Edit Data',
        'id': id,
        'record': record
    }

    return render_template(
        'admin/edit.html',
        **context
    )
