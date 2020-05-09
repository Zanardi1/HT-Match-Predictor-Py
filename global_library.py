import os
import configparser as c


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


positions = ['Midfield', 'Right defence', 'Central defence', 'Left defence', 'Right attack', 'Central attack',
             'Left attack']
statuses = ['Home', 'Away']
ans = {'Home wins': 0, 'Draws': 0, 'Away wins': 0, 'Home goals average': 0, 'Away goals average': 0}
main_folder = os.getcwd()
configuration_file = os.path.join(main_folder, "application\\connected\\session_config.ini")
disconnect_savepath = os.path.join(main_folder, "application\\xml\\Disconnect.xml")
matches_savepath = os.path.join(main_folder, "application\\xml\\Matches.xml")
user_savepath = os.path.join(main_folder, "application\\xml\\User.xml")
orders_savepath = os.path.join(main_folder, "application\\xml\\Orders.xml")
details_savepath = os.path.join(main_folder, "application\\xml\\Details.xml")
check_connection_savepath = os.path.join(main_folder, "application\\xml\\Check.xml")
database_file_path = os.path.join(main_folder, "application\\db\\matches.db")
database_file_uri = 'sqlite:///{}'.format(database_file_path)
database_backup_path = os.path.join(main_folder, "application\\backup")
default_match_orders = (-1, -1, -1, -1, -1, -1, -1)
user_data = {}
team_id = 0
user_team_name = ''
user_matches = []

ratings = build_ratings_dictionary()
