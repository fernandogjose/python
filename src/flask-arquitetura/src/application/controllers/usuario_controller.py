from flask import request, jsonify, make_response
from src.domain.models.usuario import Usuario
from src.domain.services.usuario_service import UsuarioService


def init_app(app):
    @app.route("/usuario", methods=['GET'])
    def get():
        print(app.config.get('SQLALCHEMY_DATABASE_URI'))
        return jsonify(
            {
                "nome": f"Esta é a minha {app.config.get('TITLE')}"
            }
        )

    @app.route("/usuario/<int:id>", methods=['GET'])
    def get_por_id(id: int):
        return jsonify(
            {
                "id": id
            }
        )

    @app.route("/usuario", methods=['POST'])
    def post():
        usuario_request = request.get_json()
        usuario_adicionar = Usuario(
            nome=usuario_request['nome'],
            email=usuario_request['email'],
            senha=usuario_request['senha'],
            idade=usuario_request['idade']
        )

        usuario_service: UsuarioService = UsuarioService()
        usuario_service.adicionar(usuario_adicionar=usuario_adicionar)

        return make_response(jsonify({
            'mensagem': 'usuário criado com sucesso'
        }), 201)
