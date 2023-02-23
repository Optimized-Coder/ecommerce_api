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

@main.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        description = request.form.get('description')

        new_product = Product(
            name = name,
            price = price,
            description = description
        )

        db.session.add(new_product)
        db.session.commit()
        print(f'{new_product.name} created')

        return redirect(url_for('main.index'))

    context = {
        'title': 'Add Product',
    }

    return render_template(
        'add.html',
        **context
    )

# 
@main.route('/<int:id>/delete', methods=['DELETE', 'GET'])
def delete_product(id):
    record = Product.query.filter_by(id=id).first()
    db.session.delete(record)
    db.session.commit()

    return redirect(url_for('main.index'))

@main.route('/<int:id>/edit/', methods=['GET', 'PUT'])
def edit_record(id):
    record = Product.query.filter_by(id=id).first()
    if request.method == 'PUT':

        record.name = request.form.get('name')
        record.price = request.form.get('price')
        record.description = request.form.get('description')


    context = {
        'title': 'Edit Data',
        'id': id,
        'record': record
    }

    return render_template(
        'edit.html',
        **context
    )
