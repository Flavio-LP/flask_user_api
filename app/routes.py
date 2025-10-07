from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify, render_template
from flasgger import Swagger
from .database import db
from sqlalchemy import null, text
from .models import Users
from .auth import generate_token, verify_token
from .schemas import UserSchema,TokenSchema, LoginSchema
from pydantic import ValidationError


bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET'])
def register():
   return render_template('index.html')

@bp.route('/select', methods=['GET'])
def query():
    """
    Consulta data e hora do banco
    ---
    responses:
      200:
        description: Data e hora atual do banco
        schema:
          type: string
    """
    result = db.session.execute(text('SELECT NOW();'))
    now = result.fetchone()[0]
    print('Data e hora do banco:', now)
    return f"<p>Data e hora do banco: {now}</p>"

@bp.route('/register', methods=['POST'])
def create():
    """
    Criar novo usuário
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: "José Silva"
            email:
              type: string
              example: "jose@exemplo.com"
            password:
              type: string
              example: "1234"
          required:
            - name
            - email
            - password
    responses:
      201:
        description: Usuário criado com sucesso
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Usuário criado com sucesso!"
      400:
        description: Erro de validação
      409:
        description: Usuário já existe
    """
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
    """
    Autenticar usuário
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
              example: "jose@exemplo.com"
            password:
              type: string
              example: "1234"
          required:
            - email
            - password
    responses:
      200:
        description: Login realizado com sucesso
        schema:
          type: object
          properties:
            message:
              type: string
              example: "autorizado"
      401:
        description: Não autorizado
      404:
        description: Usuário não encontrado
      498:
        description: Token expirado
    """
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
    
    
@bp.route('/users', methods=['POST'])
def list():
    """
    Listar todos os usuários
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
              example: "jose@exemplo.com"
          required:
            - email
    responses:
      200:
        description: Lista de usuários
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              email:
                type: string
      400:
        description: Erro de validação
      401:
        description: Token inválido
    """
    try:
        #print(User.name)
        token = TokenSchema(**request.json)

        User = db.session.query(Users).filter(Users.email == token.email).first()

        payload = verify_token(User.token_acess)

        if ('error' in payload):
            return jsonify({'error': payload['error']}), int(payload['status'])
        
        Users_db = db.session.query(Users).all()

        users = []
        
        for user in Users_db:    

            users.append({
                'id' : user.id,
                'name' : user.name,
                'email' : user.email
            })



        return jsonify(sorted(users, key=lambda x: x['id']))

        #return jsonify({'message': 'autenticado'}), 201
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    