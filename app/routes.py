import os
from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__)


@api_bp.get("/")
def home():
    return "Welcome to DevOps CI/CD Project", 200


@api_bp.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "flask-devops-demo",
        "environment": os.getenv("APP_ENV", "development"),
    }), 200


@api_bp.get("/api/info")
def api_info():
    return jsonify({
        "application": "Flask DevOps CI/CD Demo",
        "version": "1.0.0",
        "environment": os.getenv("APP_ENV", "development"),
        "author": "GitHub Actions Learning Project",
    }), 200
