from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager
from .main.routes import main
import os

def create_app():
    app = Flask(__name__)

    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_KEY_SECRET')
    jwt = JWTManager(app)

    app.register_blueprint(main)
    return app
    