from sqlalchemy import PrimaryKeyConstraint

from . import database


class Matches(database.Model):
    __tablename__ = 'Matches'
    __table_args__ = (PrimaryKeyConstraint('MatchID'),)
    MatchID = database.Column(database.Integer, unique=True)
    HomeTeamMidfield = database.Column(database.Integer)
    HomeTeamRDefense = database.Column(database.Integer)
    HomeTeamCDefense = database.Column(database.Integer)
    HomeTeamLDefense = database.Column(database.Integer)
    HomeTeamRAttack = database.Column(database.Integer)
    HomeTeamCAttack = database.Column(database.Integer)
    HomeTeamLAttack = database.Column(database.Integer)
    AwayTeamMidfield = database.Column(database.Integer)
    AwayTeamRDefense = database.Column(database.Integer)
    AwayTeamCDefense = database.Column(database.Integer)
    AwayTeamLDefense = database.Column(database.Integer)
    AwayTeamRAttack = database.Column(database.Integer)
    AwayTeamCAttack = database.Column(database.Integer)
    AwayTeamLAttack = database.Column(database.Integer)
    HomeTeamGoals = database.Column(database.Integer)
    AwayTeamGoals = database.Column(database.Integer)

    def __repr__(self):
        return "Numarul de identificare al meciului: %d" % self.MatchID
