# Subrutinele ce creaza URL-ul care va fi folosit pentru descarcarea unui fisier XML din Hattrick


def create_manager_compendium_string():
    # data = {'file': 'managercompendium', 'version': 1.3, 'userID': 9921303} #are o echipa
    # data = {'file': 'managercompendium', 'version': 1.3, 'userID': 2032078} #are doua echipe
    return {'file': 'managercompendium', 'version': 1.3}


def create_matches_string(team_id):
    return {'file': 'matches', 'version': 2.8, 'teamID': team_id}


def create_match_details_string(match_id):
    return {'file': 'matchdetails', 'version': '3.0', 'matchEvents': 'false', 'matchID': match_id,
            'sourceSystem': 'hattrick'}


def create_match_orders_string(match_id, team_id):
    return {'file': 'matchorders', 'version': '3.0', 'actionType': 'predictratings', 'matchID': match_id,
            'teamId': team_id}
