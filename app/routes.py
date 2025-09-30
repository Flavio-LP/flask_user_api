from flask import Blueprint, request, jsonify
from .database import db
from sqlalchemy import text
from .models import Users
from .auth import generate_token, verify_token
from .schemas import UserSchema,TokenSchema
from pydantic import ValidationError


bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET'])
def register():
   return "<p>Teste</p>"

@bp.route('/select', methods=['GET'])
def query():
    result = db.session.execute(text('SELECT NOW();'))
    now = result.fetchone()[0]
    print('Data e hora do banco:', now)
    return f"<p>Data e hora do banco: {now}</p>"

@bp.route('/register', methods=['POST'])
def create():
    try:
        # Valida e carrega os dados recebidos
        data = UserSchema(**request.json)
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400

    # Verifica se o usuário já existe
    if Users.query.filter_by(username=data.username).first():
        return jsonify({'error': 'Usuário já existe'}), 409
    
    user = Users(
        username=data.username,
        password_hash=generate_token(data.username,data.password)
    )
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'Usuário criado com sucesso!'}), 201

@bp.route('/consultar', methods=['POST'])
def user_autenticate():
    try:
        data = UserSchema(**request.json)
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    
    if not Users.query.filter_by(username=data.username).first():
        return jsonify({'error': 'Usuário não existe'}), 404

    password_hash=generate_token(data.username,data.password)
    User = db.session.query(Users).filter(Users.username == data.username).first()
    
    if (User.password_hash == password_hash):
        return jsonify({'message':'autorizado'}), 200
    
    return jsonify({'error': 'Senha incorreta'}), 401
    
@bp.route('/list', methods=['GET'])
def list():
    try:
        token = TokenSchema(**request.json)
        print(token)
        return jsonify({'message': 'autenticado'}), 201
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    