from sqlalchemy_utils import drop_database
import os
import easygui


def delete_database():
    # TODO sa repar rutina astfel incat sa-mi stearga fisierul
    db_path = os.path.join(os.path.dirname(__file__), 'matches.db')
    db_uri = 'sqlite:///{}'.format(db_path)
    easygui.msgbox(db_uri)
    print(db_uri)
    drop_database(db_uri)
    easygui.msgbox("Gata")
