"""Defineste """

from flask import Blueprint
from flask import render_template

index_bp = Blueprint('index_bp', __name__, template_folder='templates', static_folder='static')
connected_bp=Blueprint('connected_bp',__name__, template_folder='templates', static_folder='static')


@index_bp.route('/')
def home():
    return render_template('index.html')


