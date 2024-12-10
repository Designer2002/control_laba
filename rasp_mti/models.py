from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000), nullable=False)
    datetime = db.Column(db.String(100), nullable=True)

