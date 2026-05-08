# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local.db'
    
    db.init_app(app)

    # Importar blueprints DESPUÉS de db.init_app
    from app.auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    return app