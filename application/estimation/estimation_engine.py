import easygui
from application.models import Matches


def estimate():
    result = Matches.query.filter_by(AwayTeamGoals='1').all()
    easygui.msgbox(result)
    return 0
