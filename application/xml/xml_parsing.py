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
    data['team 2 name'] = root[4][5][1][1].text
    data['team 2 id'] = root[4][5][1][0].text
    data['team 3 name'] = root[4][5][2][1].text
    data['team 3 id'] = root[4][5][2][0].text
    return data
