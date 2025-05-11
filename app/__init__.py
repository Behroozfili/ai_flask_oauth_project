from flask import Flask
from app.auth import init_oauth
from dotenv import load_dotenv
from app.routes import init_routes
import os

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "fallback-secret-key") 
    init_oauth(app)  
    init_routes(app)

    return app
