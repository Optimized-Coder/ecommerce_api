from . import bp_2 as product
from ...models.products import Product
from ... import db

from flask import render_template

@product.route('/')
def index():
    
    context = {
        'title': 'Products | Book Bros'
    }

    return render_template(
        'product_list.html',
        **context
    )