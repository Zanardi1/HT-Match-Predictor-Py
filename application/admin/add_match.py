from application.models import database, Matches


def add_a_match(ID: int, HTM: int, HTRD: int, HTCD: int, HTLD: int, HTRA: int, HTCA: int, HTLA: int, ATM: int,
                ATRD: int, ATCD: int, ATLD: int, ATRA: int, ATCA: int, ATLA: int, HTG: int, ATG: int) -> None:
    match = Matches(MatchID=ID, HomeTeamMidfield=HTM, HomeTeamRDefense=HTRD, HomeTeamCDefense=HTCD,
                    HomeTeamLDefense=HTLD,
                    HomeTeamRAttack=HTRA, HomeTeamCAttack=HTCA, HomeTeamLAttack=HTLA, AwayTeamMidfield=ATM,
                    AwayTeamRDefense=ATRD,
                    AwayTeamCDefense=ATCD, AwayTeamLDefense=ATLD, AwayTeamRAttack=ATRA, AwayTeamCAttack=ATCA,
                    AwayTeamLAttack=ATLA,
                    HomeTeamGoals=HTG, AwayTeamGoals=ATG)
    database.session.add(match)


def commit_to_database() -> None:
    database.session.commit()
