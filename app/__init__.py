import os  # <--- Indispensable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///local.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    # Importar y registrar blueprints
    from app.auth.routes import auth_bp
    from app.inventory.routes import inv_bp
    from app.dashboard.routes import dash_bp
    
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