from src.domain.models.usuario import Usuario
from src.infra.repositories.usuario_repository import UsuarioRepository


class UsuarioService:
    def __init__(self, usuario_repository: UsuarioRepository = None) -> None: # type: ignore
        self.usuario_repository = usuario_repository or UsuarioRepository()

    def adicionar(self, usuario_adicionar: Usuario) -> Usuario:
        self.usuario_repository.adicionar(usuario=usuario_adicionar)
        return usuario_adicionar
