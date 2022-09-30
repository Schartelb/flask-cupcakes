"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


default_pic = "https://tinyurl.com/demo-cupcake"


class Cupcake(db.Model):
    """Cupcakes"""
    __tablename__ = "cupcakes"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    flavor = db.Column(db.Text,
                       nullable=False)
    size = db.Column(db.Text, nullable=False)

    rating = db.Column(db.Float, nullable=False)

    image = db.Column(db.Text,
                      nullable=False,
                      default=default_pic)

    def __repr__(self):
        """Show cupcake info"""
        c = self
        return f"<{c.size} {c.flavor} Cupcake, rated: {c.rating}>"


