import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instancias globales
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # 1. Configuración (DEBE IR PRIMERO)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL', 
        'postgresql://admin_user:seidor*2026@localhost:5432/inventory_db'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'senior-cloud-secret')

    # 2. Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # 3. Registrar Blueprints e importar Modelos
    with app.app_context():
        from app.auth.routes import auth_bp
        from app.inventory.routes import inv_bp
        from app.dashboard.routes import dash_bp
        from app import models # Esto asegura que Migrate vea las tablas

        app.register_blueprint(auth_bp, url_prefix='/auth')
        app.register_blueprint(inv_bp, url_prefix='/inventory')
        app.register_blueprint(dash_bp, url_prefix='/dashboard')

    @app.route('/')
    def health_check():
        return {
            "status": "online", 
            "environment": "aws" if os.environ.get('DATABASE_URL') else "local"
        }

    return app