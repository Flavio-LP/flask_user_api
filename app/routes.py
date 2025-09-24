import os
from dotenv import load_dotenv
from flask import Blueprint
from .database import db
from sqlalchemy import text


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