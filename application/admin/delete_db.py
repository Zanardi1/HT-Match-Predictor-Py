from sqlalchemy_utils import drop_database
import os
import easygui


def delete_database():
    path = os.getcwd()
    easygui.msgbox(os.getcwd())
    easygui.msgbox(os.path.join(os.getcwd(), '\\db'))
    # os.chdir(os.path.join(os.getcwd(), '\\db'))
    os.chdir(path + '\\db')
    drop_database('sqlite:///db/matches.db')
    easygui.msgbox("Gata")


delete_database()
