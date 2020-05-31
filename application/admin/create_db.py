import os

from sqlalchemy import create_engine, Column, Integer, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

import application.dialog_windows as dw
import global_library

Base = declarative_base()


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


def create_database() -> None:
    """Algoritmul de creare a bazei de date ce va retine informatiile despre meciurile din Hattrick,
    necesare simularii.

    Parametri:
    ---------
    Niciunul

    Intoarce:
    ---------
    Nimic"""

    if os.path.exists(global_library.database_file_path):
        dw.show_error_window_in_thread(title='Fisier existent', message='Baza de date deja exista.')
    else:
        Base.metadata.create_all(create_engine(global_library.database_file_uri, echo=True))
        dw.show_info_window_in_thread(title='Succes!', message='Baza de date a fost creata.')
