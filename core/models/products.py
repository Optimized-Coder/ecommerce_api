from .. import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __repr__(self) -> str:
        return f'{self.name}'