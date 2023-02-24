from . import bp_2 as product
from ...models.products import Product
from ... import db

from flask import render_template, request

genres = set()

def get_genres():
    records = Product.query.all()
    for record in records:
        genres.add(record.genre)
    return genres



@product.route('/')
def index():
    get_genres()

    sort = request.args.get('sort')

    context = {
        'title': 'Products | Book Bros',
        'Product': Product,
        'records': Product.query
        .order_by(sort)
        .all(),
        'genres': genres
    }

    return render_template(
        'product_list.html',
        **context
    )

@product.route('/<genre_tag>/')
def by_genre(genre_tag):

    sort = request.args.get('sort')
    
    get_genres()

    context = {
        'title': 'Products | Book Bros',
        'Product': Product,
        'records': Product.query
        .order_by(sort)
        .filter_by(genre=genre_tag.title())
        .all(),
        'genres': genres
    }

    return render_template(
        'product_list.html',
        **context
    )

