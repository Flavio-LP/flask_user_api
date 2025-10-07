import jwt
import os
from datetime import datetime, timedelta

SECRET_KEY = os.getenv('SECRET_KEY', 'sua_chave_secreta')

def generate_token(payload):
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return {'error' : 'expired token', 'status':'498'}
    except jwt.InvalidTokenError:
        return {'error' : 'invalid token', 'status':'401'}