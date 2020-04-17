# Subrutinele ce creaza URL-ul care va fi folosit pentru descarcarea unui fisier XML din Hattrick


def create_manager_compendium_string():
    data = {'file': 'managercompendium', 'version': 1.3}
    return data


def create_matches_string(self, team_id):
    data = {'file': 'matches', 'version': 2.8, 'teamID': team_id}
    return data


def create_match_details_string(self, match_id):
    data = {'file': 'matchdetails', 'version': '3.0', 'matchEvents': 'false', 'matchID': match_id,
            'sourceSystem': 'hattrick'}
    return data


def create_match_orders_string(self, match_id, team_id):
    data = {'file': 'matchorders', 'version': '3.0', 'actionType': 'predictratings', 'matchID': match_id,
            'teamId': team_id}
    return data
