import os

import easygui
from sqlalchemy import create_engine, Column, Integer, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def create_url():
    folder = os.getcwd()
    db_path = ''.join([folder, '\\application\\db\\matches.db'])
    return db_path


def create_uri(db_path):
    db_uri = 'sqlite:///{}'.format(db_path)
    return db_uri


# TODO clasa Model de mai jos este foarte similara cu Model din models.py. Sa mut definitia clasei intr-un singur
#  fisier, care sa fie apelat de oriunde, la nevoie
class Model(Base):
    __tablename__ = 'Matches'
    __table_args__ = (PrimaryKeyConstraint('MatchID'),)
    MatchID = Column(Integer, unique=True)
    HomeTeamMidfield = Column(Integer)
    HomeTeamRDefense = Column(Integer)
    HomeTeamCDefense = Column(Integer)
    HomeTeamLDefense = Column(Integer)
    HomeTeamRAttack = Column(Integer)
    HomeTeamCAttack = Column(Integer)
    HomeTeamLAttack = Column(Integer)
    AwayTeamMidfield = Column(Integer)
    AwayTeamRDefense = Column(Integer)
    AwayTeamCDefense = Column(Integer)
    AwayTeamLDefense = Column(Integer)
    AwayTeamRAttack = Column(Integer)
    AwayTeamCAttack = Column(Integer)
    AwayTeamLAttack = Column(Integer)
    HomeTeamGoals = Column(Integer)
    AwayTeamGoals = Column(Integer)


def create_database():
    if os.path.exists(create_url()):
        easygui.msgbox('Baza de date deja exista')
    else:
        engine = create_engine(create_uri(create_url()), echo=True)
        Base.metadata.create_all(engine)
        easygui.msgbox('Am creat baza de date')
