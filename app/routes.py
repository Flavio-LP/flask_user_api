from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify
from .database import db
from sqlalchemy import null, text
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
    if Users.query.filter_by(name=data.name).first():
        return jsonify({'error': 'Usuário já existe'}), 409
    

    user = Users(
        name=data.name,
        password_hash=generate_token({'email':data.email, 'password':data.password}),
        token_acess = generate_token({'email':data.email, "exp": datetime.utcnow() + timedelta(hours=1)}),
        email = data.email
    )
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'Usuário criado com sucesso!'}), 201

@bp.route('/consultar', methods=['POST'])
def user_autenticate():
    try:
        data = TokenSchema(**request.json)
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    
    if not Users.query.filter_by(name=data.name).first():
        return jsonify({'error': 'Usuário não existe'}), 404

    #token_hase=generate_token(data.name,data.password)
    User = db.session.query(Users).filter(Users.name == data.name).first()

    payload = verify_token(data.token)

    # verificar lógica de validação do token
    #if "status" in payload:
    #    if payload.status == '498':
    #        return jsonify({'error': 'Token expirado'}), 498
    #    else:
    #        return jsonify({'error': 'Não autorizado'}), 401
    #else:
    #    
    
    if ( User.token_acess == data.token ):
        return jsonify({'message':'autorizado'}), 200
    
    return jsonify({'error': 'Não autorizado'}), 401
    
@bp.route('/list', methods=['GET'])
def list():
    try:
        User = db.session.query(Users).all()
        print(User.name)
        token = TokenSchema(**request.json)
        print(token)
        return jsonify({'message': 'autenticado'}), 201
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    