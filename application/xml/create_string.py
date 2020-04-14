import configparser as c


class DownloadStringCreator:
    config = c.ConfigParser()
    config.read('session.config.ini')
    BaseUrl = config['DEFAULT']['PROTECTED_RESOURCE_PATH']
    DownloadedFile = ''
    FileParameters = ''

    def compose_final_string(self):
        string_parts = [self.BaseUrl, self.DownloadedFile, self.FileParameters]
        return ''.join(string_parts)

    def create_manager_compendium_string(self, team_id):
        string_parts = ['&version=2.8&teamID=', str(team_id)]
        self.DownloadedFile = '?file=matches'
        self.FileParameters = ''.join(string_parts)
        return self.compose_final_string()

    def create_match_details_string(self, match_id):
        string_parts = ['&version=3.0&matchEvents=false&matchID=', str(match_id), '&sourceSystem=hattrick']
        self.DownloadedFile = '?file=matchdetails'
        self.FileParameters = ''.join(string_parts)
        return self.compose_final_string()

    def create_match_orders_string(self, match_id, team_id):
        string_parts = ['&version=3.0&actionType=predictratings&matchID=', str(match_id), '&teamId=', str(team_id)]
        self.DownloadedFile = '?file=matchorders'
        self.FileParameters = ''.join(string_parts)
        return self.compose_final_string()
