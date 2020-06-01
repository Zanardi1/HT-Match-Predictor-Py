# Subrutinele ce creaza URL-ul care va fi folosit pentru descarcarea unui fisier XML din Hattrick


def create_manager_compendium_string() -> dict:
    """Functia stabileste parametrii ce vor fi trimisi serverului Hattrick pentru a crea fisierul
    'managercompendium'.

    Algoritm:
    ----------
    E un singur fisier si un singur parametru, ambele constante. Deci se creaza dictionarul propriu-zis.

    Parametri:
    ----------
    Niciunul.

    Intoarce:
    ----------
    Un dictionar ce contine numele fisierului si versiunea acestuia."""

    # data = {'file': 'managercompendium', 'version': 1.3, 'userID': 9921303} #are o echipa
    # data = {'file': 'managercompendium', 'version': 1.3, 'userID': 2032078} #are doua echipe
    return {'file': 'managercompendium', 'version': 1.3}


def create_matches_string(team_id: int) -> dict:
    """Functia stabileste parametrii ce vor fi trimisi serverului Hattrick pentru a crea fisierul 'matches'.

    Algoritm:
    ----------
    Se creaza dictionarul care contine partile constante si care include numarul de identificare al echipei, transmis
    ca parametru.

    Parametri:
    ----------
    team_id: int
        numarul de identificare al echipei pentru care se creaza acest fisier.

    Intoarce:
    ----------
    Un dictionar ce contine numele fisierului, versiunea acestuia si numarul de identificare al echipei pentru care
    se doreste obtinerea datelor."""

    return {'file': 'matches', 'version': 2.8, 'teamID': team_id}


def create_match_details_string(match_id: int) -> dict:
    """Functia stabileste parametrii ce vor fi trimisi serverului Hattrick pentru a crea fisierul 'matchdetails'.

    Algoritm:
    ----------
    Se creaza dictionarul care contine partile constante si care include numarul de identificare al echipei, transmis
    ca parametru.

    Parametri:
    ----------
    match_id: int
        numarul de identificare al meciului pentru care se creaza acest fisier.

    Intoarce:
    ----------
    Un dictionar ce contine numele fisierului, versiunea acestuia, faptul ca nu se doreste includerea evenimentelor
    de meci, numarul de identificare al echipei pentru care se doreste obtinerea datelor si faptul ca se doreste
    meciul de la echipa de seniori care are acel numar de identificare."""

    return {'file': 'matchdetails', 'version': '3.0', 'matchEvents': 'false', 'matchID': match_id,
            'sourceSystem': 'hattrick'}


def create_match_orders_string(match_id: int, team_id: int) -> dict:
    """Functia stabileste parametrii ce vor fi trimisi serverului Hattrick pentru a crea fisierul 'matchorders'.

    Algoritm:
    ----------
    Se creaza dictionarul care contine partile constante si care include numarul de identificare al echipei si numarul
    de identificare al meciului, transmise ca parametri.

    Parametri:
    ----------
    team_id: int
        numarul de identificare al echipei pentru care se creaza acest fisier;
    match_id: int
        numarul de identificare al meciului pentru care se creaza acest fisier.

    Intoarce:
    ----------
    Un dictionar ce contine numele fisierului, versiunea acestuia, faptul ca se doreste scrierea evaluarilor echipei
    alese, numarul de identificare al meciului si numarul de identificare al echipei."""

    return {'file': 'matchorders', 'version': '3.0', 'actionType': 'predictratings', 'matchID': match_id,
            'teamId': team_id}
