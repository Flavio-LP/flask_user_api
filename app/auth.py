import jwt
import os
from datetime import datetime, timedelta

SECRET_KEY = '1234'
#os.getenv('SECRET_KEY', 'sua_chave_secreta')

def generate_token(user,password):
    payload = {
        'user': user,
        'password': password
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['user']
    except jwt.ExpiredSignatureError:
        return None