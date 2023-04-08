from flask import jsonify, request
from flask_restful import Resource


class HomeResource(Resource):
    def get(self):
        args = request.args
        print(args)

        return jsonify(
            {
                "mensagem": "meu primeiro app está funcionando com o debug mode"
            }
        )

    def post(self):
        return jsonify(
            {
                "nome": "nome"
            }
        )
