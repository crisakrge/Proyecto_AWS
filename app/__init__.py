# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuración básica (usa variables de entorno en producción)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-777')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///local.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Registro de Blueprints (Estructura modular)
    from app.auth.routes import auth_bp
    from app.inventory.routes import inv_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(inv_bp, url_prefix='/inventory')

    @app.route('/')
    def index():
        return "Dashboard AWS Inventory - Status: Running"

    return app