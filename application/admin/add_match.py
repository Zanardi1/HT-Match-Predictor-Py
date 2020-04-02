from application.models import db, Matches


def add_a_match():
    match = Matches(MatchID=2, HomeTeamMidfield=1, HomeTeamRDefense=1, HomeTeamCDefense=1, HomeTeamLDefense=1,
                    HomeTeamRAttack=1, HomeTeamCAttack=1, HomeTeamLAttack=1, AwayTeamMidfield=1, AwayTeamRDefense=1,
                    AwayTeamCDefense=1, AwayTeamLDefense=1, AwayTeamRAttack=1, AwayTeamCAttack=1, AwayTeamLAttack=1,
                    HomeTeamGoals=1, AwayTeamGoals=1)
    db.session.add(match)
    db.session.commit()
