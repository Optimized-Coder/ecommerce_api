from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import path

DB_NAME = 'main.db'
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # app.config.from_pyfile('../config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    # postgres://ecommerce_api_products_user:pn1snLX3wCYeDUEyygL9JhCb6UR3d0nX@dpg-cft0221a6gdotccftgfg-a.frankfurt-postgres.render.com/ecommerce_api_products

    db.init_app(app)
    
    # test route
    @app.route('/test')
    def test():
        return 'Success'

    # === blueprints ===
    # main
    from .routes.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/')
    # products
    from .routes.main import bp_2 as products_bp
    app.register_blueprint(products_bp, url_prefix='/products')

    # models
    from .models.products import Product

    create_database(app)
    
    return app

def create_database(app):
    if not path.exists('core/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Database created successfully')