import os
import configparser as c
from typing import List, Dict, Tuple, Any


def build_ratings_dictionary():
    dic = {}
    levels = ['Disastrous', 'Wretched', 'Poor', 'Weak', 'Inadequate', 'Passable', 'Solid', 'Excellent', 'Formidable',
              'Outstanding', 'Brilliant', 'Magnificent', 'World Class', 'Supernatural', 'Titanic', 'Extraterrestrial',
              'Mythical', 'Magical', 'Utopian', 'Divine']
    sublevels = ['very low', 'low', 'high', 'very high']
    i = 0
    for level in range(len(levels)):
        for sublevel in range(len(sublevels)):
            dic[i] = str(levels[level]) + ' (' + str(sublevels[sublevel]) + ')'
            i += 1
    return dic


def read_from_configuration_file():
    temp_config = c.ConfigParser()
    temp_config.read(configuration_file)
    return temp_config


positions: List[str] = ['Midfield', 'Right defence', 'Central defence', 'Left defence', 'Right attack',
                        'Central attack',
                        'Left attack']
statuses: List[str] = ['Home', 'Away']
ans: Dict[str, int] = {'Home wins': 0, 'Draws': 0, 'Away wins': 0, 'Home goals average': 0, 'Away goals average': 0}
main_folder: str = os.getcwd()
configuration_file: str = os.path.join(main_folder, "application\\connected\\session_config.ini")
disconnect_savepath: str = os.path.join(main_folder, "application\\xml\\Disconnect.xml")
matches_savepath: str = os.path.join(main_folder, "application\\xml\\Matches.xml")
user_savepath: str = os.path.join(main_folder, "application\\xml\\User.xml")
orders_savepath: str = os.path.join(main_folder, "application\\xml\\Orders.xml")
details_savepath: str = os.path.join(main_folder, "application\\xml\\Details.xml")
check_connection_savepath: str = os.path.join(main_folder, "application\\xml\\Check.xml")
database_file_path: str = os.path.join(main_folder, "application\\db\\matches.db")
database_file_uri: str = 'sqlite:///{}'.format(database_file_path)
database_backup_path: str = os.path.join(main_folder, "application\\backup")
default_match_orders: Tuple[int, int, int, int, int, int, int] = (-1, -1, -1, -1, -1, -1, -1)
user_data: dict = {}
team_id: int = 0
user_team_name: str = ''
user_matches: List[Any] = []

ratings = build_ratings_dictionary()
