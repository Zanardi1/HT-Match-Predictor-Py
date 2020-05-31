# Biblioteca citeste fisierele XML si intoarce datele necesare, sub forma de dictionar
import xml.etree.ElementTree as ET

import global_library


def parse_user_file() -> dict:
    """Algoritmul citeste fisierul user.xml si extrage din el datele necesare.

    Parametri:
    ----------
    Niciunul

    Intoarce:
    ----------
    Un dictionar cu datele cautate"""
    root = ET.parse(global_library.user_savepath).getroot()
    data = {'user name': root[4][1].text, 'user id': root[4][0].text, 'supporter': root[4][2].text,
            'country': root[4][4][1].text, 'country id': root[4][4][0].text, 'team 1 name': root[4][5][0][1].text,
            'team 1 id': root[4][5][0][0].text}
    if len(list(root[4][5])) == 1:  # len(list(root[4][5])) - numarul de echipe pe care le are utilizatorul
        data['team 2 name'] = 'None'
        data['team 2 id'] = '-'
        data['team 3 name'] = 'None'
        data['team 3 id'] = '-'
    elif len(list(root[4][5])) == 2:
        data['team 2 name'] = root[4][5][1][1].text
        data['team 2 id'] = root[4][5][1][0].text
        data['team 3 name'] = 'None'
        data['team 3 id'] = '-'
    else:
        data['team 2 name'] = root[4][5][1][1].text
        data['team 2 id'] = root[4][5][1][0].text
        data['team 3 name'] = root[4][5][2][1].text
        data['team 3 id'] = root[4][5][2][0].text
    return data


def parse_matches_file() -> list:
    """Algoritmul citeste fisierul Matches.xml si extrage din el datele necesare.

    Parametri:
    ----------
    Niciunul

    Intoarce:
    ----------
    O lista de tupluri. Un tuplu contine numarul de identificare al unui meci viitor si cele doua echipe care il
    vor juca"""
    data = []
    match_list = ET.parse(global_library.matches_savepath).getroot()[5][5]
    for match in match_list:
        for i in range(len(match)):
            if match[i].tag == 'MatchType' and match[i].text in ['1', '4', '8', '10', '12']:
                for j in range(i, len(match)):
                    if match[j].tag == 'Status' and match[j].text == 'UPCOMING':
                        data.append((match[0].text, match[1][1].text, match[2][1].text))
    return data


def parse_match_details_file(match_id: int) -> list:
    """Algoritmul citeste fisierul Details.xml si extrage din el datele necesare.

    Parametri:
    ----------
    match_id: int
        variabila ce retine numarul de identificare al meciului pentru care se obtin detaliile dorite

    Intoarce:
    ----------
    O lista ce contine evaluarile sectoriale ale celor doua echipe si numarul de goluri inscrise
    de catre acestea. In ordine, lista contine evaluarile mijlocului, apararilor pe dreapta, centru si stanga si
    atacurilor pe dreapta, centru si stanga pentru echipa de acasa, respectiv pentru echipa din deplasare,
    numarul de goluri inscrise de catre echipa de acasa si numarul de goluri inscrise de catre echipa din deplasare.
    """
    match_details = [match_id]
    root = ET.parse(global_library.details_savepath).getroot()
    for i in range(7, 14, 1):
        match_details = match_details + [root[6][9][i].text]  # evaluarile echipei de acasa
    for i in range(7, 14, 1):
        match_details = match_details + [root[6][10][i].text]  # evaluarile echipei din deplasare
    match_details = match_details + [root[6][9][4].text]  # numarul de goluri ale echipei de acasa
    match_details = match_details + [root[6][10][4].text]  # numarul de goluri ale echipei din deplasare
    return match_details


def parse_future_match_file() -> list:
    """Algoritmul citeste fisierul Orders.xml si extrage din el datele necesare.

    Parametri:
    ----------
    Niciunul

    Intoarce:
    ----------
    O lista cu evaluarile pe sectoare ale echipei tale din meciul scris in acest fisier."""
    match_data = ET.parse(global_library.orders_savepath).getroot()[6]
    return [match_data[i].text for i in range(2, 9, 1)]


def parse_connection_verification_file() -> bool:
    """Algoritmul citeste fisierul Check.xml si extrage din el datele necesare.

    Parametri:
    ----------
    Niciunul

    Intoarce:
    ----------
    True, daca fisierul contine jetonul de access. Altfel intoarce False, pentru ca acest fisier nici nu are
    formatul XML"""
    try:
        ET.parse(global_library.check_connection_savepath).getroot()[4].text
    except IndexError:  # asta inseamna ca fisierul cu extensia xml este, de fapt, un fisier HTML si acel nod nu exista.
        # Ar da mesajul de eroare: IndexError: child index out of range
        return False
    else:
        return True
