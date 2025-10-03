from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify
from .database import db
from sqlalchemy import null, text
from .models import Users
from .auth import generate_token, verify_token
from .schemas import UserSchema,TokenSchema, LoginSchema
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
    if Users.query.filter_by(email=data.email).first():
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

@bp.route('/login', methods=['POST'])
def user_autenticate():
    try:
        data = LoginSchema(**request.json)
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    
    if not Users.query.filter_by(email=data.email).first():
        return jsonify({'error': 'Usuário não existe'}), 404

    #token_hase=generate_token(data.name,data.password)
    User = db.session.query(Users).filter(Users.email == data.email).first()

    payload = verify_token(User.password_hash)

    if ("password" in payload):
        if (payload['password'] == data.password):

            User.token_acess = generate_token({'email':data.email, "exp": datetime.utcnow() + timedelta(hours=1)})
            db.session.commit()    
            return jsonify({'message':'autorizado'}), 200

        else:
            return jsonify({'error': 'Senha incorreta'}), 401
    else:
          if payload.status == '498':
            return jsonify({'error': 'Token expirado'}), 498
          else:
            return jsonify({'error': 'Não autorizado'}), 401
    
    
@bp.route('/list', methods=['POST'])
def list():
    try:
        #User = db.session.query(Users).all()
        #print(User.name)
        token = TokenSchema(**request.json)

        User = db.session.query(Users).filter(Users.email == token.email).first()

        payload = verify_token(User.token_acess)

        print(payload)
        # expirado: {'error': 'expired token', 'status': '498'} -- realizar login novamente....
        # inválido: {'error' : 'invalid token', 'status':'401'} -- verificar quais passos realizar

        return jsonify({'message': 'autenticado'}), 201
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    