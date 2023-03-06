from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ


# criar a conn com o banco
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)


# criar tabela de usuário
class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)

    def json(self):
        return {
            'id': self.id,
            'nome': self.usuario,
            'email': self.email
        }


db.create_all()


# home
@app.route('/home', methods=['GET'])
def home():
    return make_response(jsonify({
        'mensagem': 'minha home'
    }), 200)


# usuario adicionar
@app.route('/usuarios', methods=['POST'])
def usuario_adicionar():
    try:
        usuario_request = request.get_json()
        usuario_novo = Usuario(
            nome=usuario_request['nome'],
            email=usuario_request['email']
        )
        db.session.add(usuario_novo)
        db.session.commit()

        return make_response(jsonify({
            'mensagem': 'usuário criado com sucesso'
        }), 201)
    except e:
        return make_response(jsonify({
            'mensagem': 'erro ao criar usuário'
        }), 500)


# usuario obter todos
@app.route('/usuarios', methods=['GET'])
def usuario_obter_todos():
    try:
        usuarios = Usuario.query.all()

        return make_response(jsonify({
            'usuarios': [Usuario.json() for usuario in usuarios]
        }), 200)
    except e:
        return make_response(jsonify({
            'mensagem': 'erro ao obter todos os usuário'
        }), 500)


# usuario obter por id
@app.route('/usuarios/<int:id>', methods=['GET'])
def usuario_obter_por_id(id: int):
    try:
        usuario = Usuario.query.filter_by(id=id).first()
        if usuario:
            return make_response(jsonify({
                'usuario': Usuario.json()
            }), 200)

        return make_response(jsonify({
            'mensagem': 'usuário não encontrado'
        }), 404)
    except e:
        return make_response(jsonify({
            'mensagem': 'erro ao obter usuário por id'
        }), 500)


# usuario atualizar
@app.route('/usuarios/<int:id>', methods=['PUT'])
def usuario_obter_por_id(id: int):
    try:
        usuario = Usuario.query.filter_by(id=id).first()
        if(usuario):
            usuario_request = request.get_json()
            usuario.nome = usuario_request['nome']
            usuario.email = usuario_request['email']

            db.session.commit()

            return make_response(jsonify({
                'mensagem': 'usuário atualizado'
            }), 201)

        return make_response(jsonify({
            'mensagem': 'usuário não encontrado'
        }), 404)
    except e:
        return make_response(jsonify({
            'mensagem': 'erro ao atualizar usuário'
        }), 500)


# usuario deletar
@app.route('/usuarios/<int:id>', methods=['PUT'])
def usuario_obter_por_id(id: int):
    try:
        usuario = Usuario.query.filter_by(id=id).first()
        if(usuario):
            db.session.delete(usuario)
            db.session.commit()

            return make_response(jsonify({
                'mensagem': 'usuário deletado'
            }), 201)

        return make_response(jsonify({
            'mensagem': 'usuário não encontrado'
        }), 404)
    except e:
        return make_response(jsonify({
            'mensagem': 'erro ao deletar usuário'
        }), 500)