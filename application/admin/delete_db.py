from sqlalchemy_utils import drop_database
import os


def delete_database():
    os.chdir('..')
    drop_database('sqlite:///db/matches.db')