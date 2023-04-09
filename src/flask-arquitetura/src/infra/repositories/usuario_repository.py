from src.infra.extensions.database import db
from src.domain.models.usuario import Usuario


class UsuarioRepository:
    def adicionar(self, usuario: Usuario):
        db.session.add(usuario)
        db.session.commit()
