from .. import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, title, author, genre, price, description):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.description = description

    def __repr__(self) -> str:
        return f'{self.title}'

