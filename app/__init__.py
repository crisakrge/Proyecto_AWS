import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instancias globales
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # 1. Configuración de Base de Datos con prioridad
    # Si TESTING es True o DATABASE_URL no existe, usamos SQLite para no romper el CI/CD
    default_db = 'sqlite:///local.db'
    database_url = os.environ.get('DATABASE_URL')
    
    if os.environ.get('FLASK_ENV') == 'testing':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url or default_db
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'senior-cloud-secret')

    # 2. Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # 3. Registrar Blueprints e importar Modelos
    with app.app_context():
        # Importación interna para evitar ciclos
        from app import models 
        from app.auth.routes import auth_bp
        from app.inventory.routes import inv_bp
        from app.dashboard.routes import dash_bp

        app.register_blueprint(auth_bp, url_prefix='/auth')
        app.register_blueprint(inv_bp, url_prefix='/inventory')
        app.register_blueprint(dash_bp, url_prefix='/dashboard')

    @app.route('/')
    def health_check():
        # Lógica de detección de entorno para el JSON de respuesta
        env_type = "local"
        if os.environ.get('DATABASE_URL'):
            env_type = "aws"
            
        return {
            "status": "online", 
            "environment": env_type
        }

    return app