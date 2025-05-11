from authlib.integrations.flask_client import OAuth
from flask import session, current_app
from app.config import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET


# Setup OAuth
oauth = OAuth()
google = None

def init_oauth(app):
    global google
    oauth.init_app(app)
    
    google = oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
        client_kwargs={
            'scope': 'openid email profile'
        }
    )
    app.google_oauth = google

def get_current_user():
    return session.get('user')
