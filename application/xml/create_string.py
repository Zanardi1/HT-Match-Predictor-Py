# Subrutinele ce creaza URL-ul care va fi folosit pentru descarcarea unui fisier XML din Hattrick

import configparser as c
import os
import urllib

configuration_file = os.path.abspath('application\connected\session_config.ini')


class DownloadStringCreator:
    config = c.ConfigParser()
    config.read(configuration_file)
    BaseUrl = config['DEFAULT']['PROTECTED_RESOURCE_PATH']

    def compose_final_string(self, url_values):
        return ''.join([self.BaseUrl, '?', url_values])

    def create_manager_compendium_string(self):
        data = {'file': 'managercompendium', 'version': 1.3}
        url_values = urllib.parse.urlencode(data)
        return self.compose_final_string(url_values)

    def create_matches_string(self, team_id):
        data = {'file': 'matches', 'version': 2.8, 'teamID': team_id}
        url_values = urllib.parse.urlencode(data)
        return self.compose_final_string(url_values)

    def create_match_details_string(self, match_id):
        data = {'file': 'matchdetails', 'version': '3.0', 'matchEvents': 'false', 'matchID': match_id,
                'sourceSystem': 'hattrick'}
        url_values = urllib.parse.urlencode(data)
        return self.compose_final_string(url_values)

    def create_match_orders_string(self, match_id, team_id):
        data = {'file': 'matchorders', 'version': '3.0', 'actionType': 'predictratings', 'matchID': match_id,
                'teamId': team_id}
        url_values = urllib.parse.urlencode(data)
        return self.compose_final_string(url_values)
