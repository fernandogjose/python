from src.infra.extensions.database import db


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer)
