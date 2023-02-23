from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import path

DB_NAME = 'main.db'
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    db.init_app(app)
    
    @app.route('/test')
    def test():
        return 'Success'

    # views

    # models

    create_database(app)
    
    return app

def create_database(app):
    if not path.exists('core/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Database created successfully')