
from flask import redirect, request, session, url_for, jsonify, current_app
from app.auth import google, get_current_user
from app.ai import analyze_text
import secrets


def init_routes(app):

    @app.route("/")
    def root():
        return jsonify({"message": "API with OAuth and Hugging Face AI"})

    @app.route("/login")
    def login():
        redirect_uri = url_for('auth', _external=True)

        if not hasattr(current_app, 'google_oauth'):
            return "Internal Server Error: OAuth not configured", 500

        # Save next path in session
        session['next'] = request.args.get('next') or '/analyze'

        # Generate nonce and save in session
        nonce = secrets.token_urlsafe(16)
        session['nonce'] = nonce

        # Send nonce with redirect
        return current_app.google_oauth.authorize_redirect(redirect_uri, nonce=nonce)

    @app.route("/auth")
    def auth():
        if not hasattr(current_app, 'google_oauth'):
            return "Internal Server Error: OAuth not configured", 500

        token = current_app.google_oauth.authorize_access_token()

        # Get nonce from session
        nonce = session.get('nonce')
        if not nonce:
            return "Session expired or invalid", 400

        # Include nonce in parse_id_token to prevent Replay attacks
        user = current_app.google_oauth.parse_id_token(token, nonce=nonce)
        session['user'] = user

        # Retrieve next URL from session and redirect to it
        next_url = session.pop('next', '/analyze')
        return redirect(next_url)

    @app.route("/analyze", methods=["GET", "POST"])
    def analyze():
        user = get_current_user()
        if not user:
            return jsonify({"error": "Unauthorized"}), 401

        if request.method == "POST":
            text = request.form.get("text")
            if not text:
                return jsonify({"error": "No text provided"}), 400

            result = analyze_text(text)
            return jsonify(result)
        else:
            return '''
                <h2>Text Analysis with MLOps</h2>
                <form method="post">
                    <textarea name="text" rows="6" cols="60" placeholder="Enter your text here..."></textarea><br>
                    <input type="submit" value="Analyze">
                </form>
            '''
