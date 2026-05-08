from flask import Blueprint
inv_bp = Blueprint('inventory', __name__)

@inv_bp.route('/')
def index():
    return "Syncing AWS inventory..."
