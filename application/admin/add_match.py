from application.models import database, Matches


def add_a_match(id: int, htm: int, htrd: int, htcd: int, htld: int, htra: int, htca: int, htla: int, atm: int,
                atrd: int, atcd: int, atld: int, atra: int, atca: int, atla: int, htg: int, atg: int) -> None:
    match = Matches(MatchID=id, HomeTeamMidfield=htm, HomeTeamRDefense=htrd, HomeTeamCDefense=htcd,
                    HomeTeamLDefense=htld,
                    HomeTeamRAttack=htra, HomeTeamCAttack=htca, HomeTeamLAttack=htla, AwayTeamMidfield=atm,
                    AwayTeamRDefense=atrd,
                    AwayTeamCDefense=atcd, AwayTeamLDefense=atld, AwayTeamRAttack=atra, AwayTeamCAttack=atca,
                    AwayTeamLAttack=atla,
                    HomeTeamGoals=htg, AwayTeamGoals=atg)
    database.session.add(match)


def commit_to_database() -> None:
    database.session.commit()
