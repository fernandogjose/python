from src.infra.extensions.database import db
from src.domain.models.usuario import Usuario


def init_app(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

        db.session.add(Usuario(nome='Fernando', email='fernandogjose@gmail.com', senha='12345', idade=41))
        db.session.add(Usuario(nome='Priscila', email='priscilaecoaprender@gmail.com', senha='12345', idade=41))
        db.session.commit()

        # users = db.session.execute(db.select(Usuario)).scalars()
