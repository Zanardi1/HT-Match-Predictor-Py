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
positions = ['Midfield', 'Left defence', 'Central defence', 'Right defence', 'Left attack', 'Central attack',
             'Right attack']
statuses = ['Home', 'Away']
