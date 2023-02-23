from . import bp as main
from flask import jsonify, request, render_template, redirect, url_for
from ...models.products import Product
from ... import db


@main.route('/')
def index():
    if request.method == 'GET':
        for product in Product.query.all():
            return f'{product.name} | {product.price} | {product.description}'

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