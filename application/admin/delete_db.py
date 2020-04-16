from sqlalchemy_utils import drop_database
import os
import easygui


def delete_database():
    folder = os.getcwd()
    db_path = ''.join([folder, '\\application\\db\\matches.db'])
    db_uri = 'sqlite:///{}'.format(db_path)
    if os.path.exists(db_path):
        drop_database(db_uri)
        easygui.msgbox("Gata")
    else:
        easygui.msgbox('Baza de date nu exista')
