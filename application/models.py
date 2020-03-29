from . import db


class Matches(db.Model):
    __tablename__ = 'Matches'
    MatchID = db.Column(db.integer, unique=True)
    HomeTeamMidfield = db.Column(db.integer)
    HomeTeamRDefense = db.Column(db.integer)
    HomeTeamCDefense = db.Column(db.integer)
    HomeTeamLDefense = db.Column(db.integer)
    HomeTeamRAttack = db.Column(db.integer)
    HomeTeamCAttack = db.Column(db.integer)
    HomeTeamLAttack = db.Column(db.integer)
    AwayTeamMidfield = db.Column(db.integer)
    AwayTeamRDefense = db.Column(db.integer)
    AwayTeamCDefense = db.Column(db.integer)
    AwayTeamLDefense = db.Column(db.integer)
    AwayTeamRAttack = db.Column(db.integer)
    AwayTeamCAttack = db.Column(db.integer)
    AwayTeamLAttack = db.Column(db.integer)
    HomeTeamGoals = db.Column(db.integer)
    AwayTeamGoals = db.Column(db.integer)
