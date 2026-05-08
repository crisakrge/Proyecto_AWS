from flask import Blueprint
inv_bp = Blueprint('inventory', __name__)

@inv_bp.route('/sync')
def sync():
    return "Syncing AWS Infrastructure..."