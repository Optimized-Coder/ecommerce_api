from . import bp_2 as product
from ...models.products import Product
from ... import db

from flask import render_template

genres = set()

def get_genres():
    for record in Product.query.all():
        genres.add(record.genre)
    return genres

@product.route('/')
def index():
    get_genres()

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

@product.route('/<genre_tag>/')
def by_genre(genre_tag):
    get_genres()

    context = {
        'title': 'Products | Book Bros',
        'Product': Product,
        'records': Product.query.filter_by(genre=genre_tag.title()).all(),
        'genres': genres
    }

    return render_template(
        'product_list.html',
        **context
    )

