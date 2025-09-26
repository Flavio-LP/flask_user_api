from flask import Blueprint, request, jsonify
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

@bp.route('/register', methods=['POST'])
def create():
    json = request.json
    print(json)
    return jsonify({"resultado": f"Dado JSON: {json}"}), 201