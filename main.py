import os
from dotenv import load_dotenv
from app import create_app
from app.database import db

load_dotenv()

app = create_app()

if __name__ == '__main__':
    app.run()