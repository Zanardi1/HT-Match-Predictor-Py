from . import db
from sqlalchemy import PrimaryKeyConstraint


class Matches(db.Model):
    __tablename__ = 'Matches'
    __table_args__ = (PrimaryKeyConstraint('MatchID'),)
    MatchID = db.Column(db.Integer, unique=True)
    HomeTeamMidfield = db.Column(db.Integer)
    HomeTeamRDefense = db.Column(db.Integer)
    HomeTeamCDefense = db.Column(db.Integer)
    HomeTeamLDefense = db.Column(db.Integer)
    HomeTeamRAttack = db.Column(db.Integer)
    HomeTeamCAttack = db.Column(db.Integer)
    HomeTeamLAttack = db.Column(db.Integer)
    AwayTeamMidfield = db.Column(db.Integer)
    AwayTeamRDefense = db.Column(db.Integer)
    AwayTeamCDefense = db.Column(db.Integer)
    AwayTeamLDefense = db.Column(db.Integer)
    AwayTeamRAttack = db.Column(db.Integer)
    AwayTeamCAttack = db.Column(db.Integer)
    AwayTeamLAttack = db.Column(db.Integer)
    HomeTeamGoals = db.Column(db.Integer)
    AwayTeamGoals = db.Column(db.Integer)

    def __repr__(self):
        return '<Match: {}>'.format(self.MatchID)
