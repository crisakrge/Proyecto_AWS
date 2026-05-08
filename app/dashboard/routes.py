from flask import Blueprint

dash_bp = Blueprint('dashboard', __name__)

@dash_bp.route('/')
def index():
    return {"message": "Welcome to Dashboard"}