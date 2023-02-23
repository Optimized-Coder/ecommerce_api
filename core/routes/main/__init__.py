from flask import Blueprint

bp = Blueprint('main', __name__)

bp_2 = Blueprint('products', __name__)

from . import routes
from . import product_routes