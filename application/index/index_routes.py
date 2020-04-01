"""Defineste rutele pentru pagina de index"""

from flask import Blueprint
from flask import render_template
import global_library
# from application.models import db, Matches


index_bp = Blueprint('index_bp', __name__, template_folder='templates', static_folder='static')
ratings = global_library.ratings
positions = global_library.positions
statuses = global_library.statuses


@index_bp.route('/')
def home():
    # match = Matches(MatchID=1, HomeTeamMidfield=1, HomeTeamRDefense=1, HomeTeamCDefense=1, HomeTeamLDefense=1,
    #                 HomeTeamRAttack=1, HomeTeamCAttack=1, HomeTeamLAttack=1, AwayMidfield=1, AwayTeamRDefense=1,
    #                 AwayTeamCDefense=1, AwayTeamLDefense=1, AwayTeamRAttack=1, AwayTeamCAttack=1, AwayTeamLAttack=1,
    #                 HomeTeamGoals=1, AwayTeamGoals=1)
    # db.session.add(match)
    # db.session.commit()
    return render_template('index.html', title="The Best Match Predictor", ratings=ratings, positions=positions,
                           statuses=statuses, from_index=True)
