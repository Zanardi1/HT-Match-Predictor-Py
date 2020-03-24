from flask import Blueprint
from flask import render_template

connected_bp = Blueprint('connected_bp', __name__, template_folder='templates', static_folder='static')


@connected_bp.route('/')
def connected():
    return render_template('connected.html')
