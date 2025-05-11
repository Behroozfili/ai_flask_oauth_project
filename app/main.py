from flask import Flask
from app.auth import init_oauth
from app.routes import init_routes
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "fallback-secret-key")

    try:
        init_oauth(app)
    except Exception as e:
        print(f"!!! Error in init_oauth: {e}")  # Only log errors if something fails

    try:
        init_routes(app)  # This line is important
    except Exception as e:
        print(f"!!! Error in init_routes: {e}")  # Only log errors if something fails

    return app
