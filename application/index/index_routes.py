"""Defineste rutele pentru pagina de index"""

from flask import Blueprint
from flask import render_template
import global_library

index_bp = Blueprint('index_bp', __name__, template_folder='templates', static_folder='static')
ratings = global_library.ratings
positions = global_library.positions
statuses = global_library.statuses


@index_bp.route('/')
def home():
    return render_template('index.html', title="The Best Match Predictor", ratings=ratings, positions=positions,
                           statuses=statuses)
