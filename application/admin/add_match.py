from application.models import database, Matches


def add_a_match(id: int, htm: int, htrd: int, htcd: int, htld: int, htra: int, htca: int, htla: int, atm: int,
                atrd: int, atcd: int, atld: int, atra: int, atca: int, atla: int, htg: int, atg: int) -> None:
    """Procedura adauga in baza de date informatiile necesare simularii, transmise prin parametri si
    preluate dintr-un fisier ce retine un singur meci de Hattrick.

    Algoritm:
    ----------
    Se creaza o noua instanta a clasei Matches, care cuprinde ca membri, evaluarile transmise ca parametri.
    Acea instanta este folosita la adaugarea in baza de date a membrilor acesteia.

    Parametri:
    ----------
    id: int
        numarul de identificare al meciului din Hattrick
    htm: int
        evaluarea mijlocului echipei gazda. E un numar intre 1 si 80. Numele parametrului vine de la
        Home Team Midfield
    htrd: int
        evaluarea apararii pe dreapta a echipei gazda. E un numar intre 1 si 80. Numele parametrului vine de la
        Home Team Right Defence
    htcd: int
        evaluarea apararii centrale a echipei gazda. E un numar intre 1 si 80. Numele parametrului vine de la
        Home Team Central Defence
    htld: int
        evaluarea apararii pe stanga a echipei gazda. E un numar intre 1 si 80. Numele parametrului vine de la
        Home Team Left Defence
    htra: int
        evaluarea atacului pe dreapta al echipei gazda. E un numar intre 1 si 80. Numele parametrului vine de la
        Home Team Right Attack
    htca: int
        evaluarea atacului pe centru al echipei gazda. E un numar intre 1 si 80. Numele parametrului vine de la
        Home Team Center Attack
    htla: int
        evaluarea atacului pe stanga al echipei gazda. E un numar intre 1 si 80. Numele parametrului vine de la
        Home Team Left Attack
    atm: int
        evaluarea mijlocului echipei oaspete. E un numar intre 1 si 80. Numele parametrului vine de la
        Away Team Midfield
    atrd: int
        evaluarea apararii pe dreapta a echipei oaspete. E un numar intre 1 si 80. Numele parametrului vine de la
        Away Team Right Defence
    atcd: int
        evaluarea apararii centrale a echipei oaspete. E un numar intre 1 si 80. Numele parametrului vine de la
        Away Team Central Defence
    atld: int
        evaluarea apararii pe stanga a echipei oaspete. E un numar intre 1 si 80. Numele parametrului vine de la
        Away Team Left Defence
    atra: int
        evaluarea atacului pe dreapta al echipei oaspete. E un numar intre 1 si 80. Numele parametrului vine de la
        Away Team Right Attack
    atca: int
        evaluarea atacului pe centru al echipei oaspete. E un numar intre 1 si 80. Numele parametrului vine de la
        Away Team Center Attack
    atla: int
        evaluarea atacului pe stanga al echipei oaspete. E un numar intre 1 si 80. Numele parametrului vine de la
        Away Team Left Attack

    Intoarce:
    ----------
        Nimic
    """
    match = Matches(MatchID=id, HomeTeamMidfield=htm, HomeTeamRDefense=htrd, HomeTeamCDefense=htcd,
                    HomeTeamLDefense=htld,
                    HomeTeamRAttack=htra, HomeTeamCAttack=htca, HomeTeamLAttack=htla, AwayTeamMidfield=atm,
                    AwayTeamRDefense=atrd,
                    AwayTeamCDefense=atcd, AwayTeamLDefense=atld, AwayTeamRAttack=atra, AwayTeamCAttack=atca,
                    AwayTeamLAttack=atla,
                    HomeTeamGoals=htg, AwayTeamGoals=atg)
    database.session.add(match)


def commit_to_database() -> None:
    """Procedura salveaza datele introduse in baza de date

    Parametri:
    ----------
    Niciunul

    Intoarce:
    ----------
    Nimic"""
    database.session.commit()
