from flask import jsonify


def init_app(app):
    @app.route("/homepage", methods=['GET'])
    def get():
        print(app.config.get('SQLALCHEMY_DATABASE_URI'))
        return jsonify(
            {
                "nome": f"AAAEsta é a minha {app.config.get('TITLE')}"
            }
        )

    @app.route("/homepage/<int:id>", methods=['GET'])
    def get_por_id(id: int):
        return jsonify(
            {
                "id": id
            }
        )

    @app.route("/homepage/<nome>", methods=['GET'])
    def get_por_nome(nome: str):
        return jsonify(
            {
                "nome": nome
            }
        )