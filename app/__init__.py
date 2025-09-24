import os
from flask import Flask
from .database import db
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app