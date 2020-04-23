from application.models import database, Matches


def add_a_match(ID, HTM, HTRD, HTCD, HTLD, HTRA, HTCA, HTLA, ATM, ATRD, ATCD, ATLD, ATRA, ATCA, ATLA, HTG, ATG):
    match = Matches(MatchID=ID, HomeTeamMidfield=HTM, HomeTeamRDefense=HTRD, HomeTeamCDefense=HTCD,
                    HomeTeamLDefense=HTLD,
                    HomeTeamRAttack=HTRA, HomeTeamCAttack=HTCA, HomeTeamLAttack=HTLA, AwayTeamMidfield=ATM,
                    AwayTeamRDefense=ATRD,
                    AwayTeamCDefense=ATCD, AwayTeamLDefense=ATLD, AwayTeamRAttack=ATRA, AwayTeamCAttack=ATCA,
                    AwayTeamLAttack=ATLA,
                    HomeTeamGoals=HTG, AwayTeamGoals=ATG)
    database.session.add(match)
    database.session.commit()
