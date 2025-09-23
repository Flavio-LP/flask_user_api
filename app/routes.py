import os
from dotenv import load_dotenv
from flask import Blueprint


bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET'])
def register():
   #PG = os.environ.get('PG_HOST')
   #print(PG)
   return "<p>Teste</p>"