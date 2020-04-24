import os

import easygui
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from application.models import Matches


# select count(1), HomeTeamGoals, AwayTeamGoals, avg ("HomeTeamGoals"), avg ("AwayTeamGoals") from Matches where
# HomeTeamMidfield=2

def create_url():
    folder = os.getcwd()
    db_path = ''.join([folder, '\\application\\db\\matches.db'])
    return db_path


def create_uri(db_path):
    db_uri = 'sqlite:///{}'.format(db_path)
    return db_uri


def estimate(given_ratings):
    wins = 0
    draws = 0
    losses = 0
    sum_of_home_goals = 0
    sum_of_away_goals = 0
    engine = create_engine(create_uri(create_url()), echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    records = session.query(Matches.HomeTeamGoals, Matches.AwayTeamGoals).filter(
        Matches.HomeTeamMidfield == given_ratings[0]).filter(Matches.HomeTeamRDefense == given_ratings[1]).filter(
        Matches.HomeTeamCDefense == given_ratings[2]).filter(Matches.HomeTeamLDefense == given_ratings[3]).filter(
        Matches.HomeTeamRAttack == given_ratings[4]).filter(Matches.HomeTeamCAttack == given_ratings[5]).filter(
        Matches.HomeTeamLAttack == given_ratings[6]).filter(Matches.AwayTeamMidfield == given_ratings[7]).filter(
        Matches.AwayTeamRDefense == given_ratings[8]).filter(Matches.AwayTeamCDefense == given_ratings[9]).filter(
        Matches.AwayTeamLDefense == given_ratings[10]).filter(Matches.AwayTeamRAttack == given_ratings[11]).filter(
        Matches.AwayTeamCAttack == given_ratings[12]).filter(Matches.AwayTeamLAttack == given_ratings[13])
    number_of_matches = records.count()
    for record in records:
        sum_of_home_goals += record.HomeTeamGoals
        sum_of_away_goals += record.AwayTeamGoals
        if record.HomeTeamGoals > record.AwayTeamGoals:
            wins += 1
        elif record.HomeTeamGoals == record.AwayTeamGoals:
            draws += 1
        else:
            losses += 1
    home_goals_average = sum_of_home_goals / number_of_matches
    away_goals_average = sum_of_away_goals / number_of_matches
    easygui.msgbox(wins)
    easygui.msgbox(draws)
    easygui.msgbox(losses)
    easygui.msgbox(home_goals_average)
    easygui.msgbox(away_goals_average)
    session.close()
