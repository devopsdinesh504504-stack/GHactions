import os
from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["DEBUG"] = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.config["PORT"] = int(os.getenv("PORT", "5000"))

    from app.routes import api_bp

    app.register_blueprint(api_bp)

    return app
