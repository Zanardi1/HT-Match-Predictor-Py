# TODO: Optimizare de cod: sa scriu acelasi lucru cu cat mai putine linii posibil
# TODO: Sa tratez exceptiile care pot aparea in site
# TODO: Sa citesc documentatiile bibliotecilor pe care le folosesc, pentru a vedea daca am ceva de imbunatatit
# TODO: Sa inlocuiesc ferestrele de dialog cu altele, dintr-o alta biblioteca, astfel incat sa nu imi crape
#  interpretorul atunci cand le folosesc
# TODO: Sa scriu documentatii pentru fiecare functie din site.
# TODO: Sa mut constantele in global_library
# TODO: Sa completez documentatia din wiki-ul Github
# TODO: Sa fac o optiune prin care ia in calcul, pentru estimate, numai nivelele evaluarilor, nu si subnivelele
# TODO: Sa fac o optiune de backup la BD
# TODO: Sa fac o optiune prin care sa ti se permita sa iei in calcul pentru simulare numai anumite compartimente ale
#  celor doua echipe, compartimente alese de catre tine
# TODO: secventa de citire din fisierul de configurari, care se gaseste intr-un numar mare de fisiere, sa o
#  fac procedura si sa o mut in global_library
# TODO: sa scap de variabilele globale
# TODO: sa modific rutina de adaugare a unui meci in BD astfel incat sa nu se faca commit dupa fiecare meci,
#  ci o data, la final
# TODO: caile definite prin programe sa le construiesc si sa le atribui ca valori de variabile in global_library

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
