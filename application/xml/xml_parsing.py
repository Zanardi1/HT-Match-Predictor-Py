# Biblioteca citeste fisierele XML si intoarce datele necesare, sub forma de dictionar
import os
import xml.etree.ElementTree as ET
import easygui


def parse_user_file():
    data = {}
    tree = ET.parse(os.path.abspath('application\\xml\\User.xml'))
    root = tree.getroot()
    data['user name'] = root[4][1].text
    data['user id'] = root[4][0].text
    data['supporter'] = root[4][2].text
    data['country'] = root[4][4][1].text
    data['country id'] = root[4][4][0].text
    data['team 1 name'] = root[4][5][0][1].text
    data['team 1 id'] = root[4][5][0][0].text
    number_of_user_teams = len(list(root[4][5]))
    if number_of_user_teams == 1:
        data['team 2 name'] = 'None'
        data['team 2 id'] = '-'
        data['team 3 name'] = 'None'
        data['team 3 id'] = '-'
    elif number_of_user_teams == 2:
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


def parse_matches_file():
    data = []
    tree = ET.parse(os.path.abspath('application\\xml\\Matches.xml'))
    root = tree.getroot()
    match_list = root[5][5]
    for match in match_list:
        if match[5].text in ['1', '4', '8', '10', '12'] and match[10].tag == 'Status' and match[10].text == 'UPCOMING':
            match_id = match[0].text
            home_team = match[1][1].text
            away_team = match[2][1].text
            data.append((match_id, home_team, away_team))
    return data
