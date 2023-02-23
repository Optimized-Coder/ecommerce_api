from . import bp_2 as product
from ...models.products import Product
from ... import db

from flask import render_template



@product.route('/')
def index():
    genres = set()
    for record in Product.query.all():
        genres.add(record.genre)
    
    context = {
        'title': 'Products | Book Bros',
        'Product': Product,
        'records': Product.query.all(),
        'genres': genres
    }

    return render_template(
        'product_list.html',
        **context
    )