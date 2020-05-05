import os


def buildRatingsDictionary():
    dic = {}
    levels = ['Disastruos', 'Wretched', 'Poor', 'Weak', 'Inadequate', 'Passable', 'Solid', 'Excellent', 'Formidable',
              'Outstanding', 'Brilliant', 'Magnificent', 'World Class', 'Supernatural', 'Titanic', 'Extraterrestrial',
              'Mythical', 'Magical', 'Utopian', 'Divine']
    sublevels = ['very low', 'low', 'high', 'very high']
    i = 0
    for level in range(len(levels)):
        for sublevel in range(len(sublevels)):
            dic[i] = str(levels[level]) + ' (' + str(sublevels[sublevel]) + ')'
            i += 1
    return dic


ratings = buildRatingsDictionary()
positions = ['Midfield', 'Right defence', 'Central defence', 'Left defence', 'Right attack', 'Central attack',
             'Left attack']
statuses = ['Home', 'Away']
ans = {'Home wins': 0, 'Draws': 0, 'Away wins': 0, 'Home goals average': 0, 'Away goals average': 0}
configuration_file = os.path.abspath('application\connected\session_config.ini')
disconnect_savepath = os.path.abspath('application\\xml\\Disconnect.xml')
matches_savepath = os.path.abspath('application\\xml\\Matches.xml')
user_savepath = os.path.abspath('application\\xml\\User.xml')
orders_savepath = os.path.abspath('application\\xml\\Orders.xml')
default_match_orders = (-1, -1, -1, -1, -1, -1, -1)
