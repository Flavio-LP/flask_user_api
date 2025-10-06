import os
from flask import Flask
from flasgger import Swagger
from .database import db
from dotenv import load_dotenv
from . import models

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }
    
    swagger = Swagger(app, config=swagger_config)

    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app