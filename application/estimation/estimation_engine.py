from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import application.dialog_windows as dw
import global_library
from application.models import Matches


def estimate_results(given_ratings: tuple) -> dict:
    ans = {'Home wins': 0, 'Draws': 0, 'Away wins': 0, 'Home goals average': 0, 'Away goals average': 0,
           'Sum of home goals': 0, 'Sum of away goals': 0}
    engine = create_engine(global_library.database_file_uri, echo=True)
    session_class = sessionmaker(bind=engine)
    session = session_class()
    records = session.query(Matches.HomeTeamGoals, Matches.AwayTeamGoals).filter(
        Matches.HomeTeamMidfield == given_ratings[0]).filter(Matches.HomeTeamRDefense == given_ratings[1]).filter(
        Matches.HomeTeamCDefense == given_ratings[2]).filter(Matches.HomeTeamLDefense == given_ratings[3]).filter(
        Matches.HomeTeamRAttack == given_ratings[4]).filter(Matches.HomeTeamCAttack == given_ratings[5]).filter(
        Matches.HomeTeamLAttack == given_ratings[6]).filter(Matches.AwayTeamMidfield == given_ratings[7]).filter(
        Matches.AwayTeamRDefense == given_ratings[8]).filter(Matches.AwayTeamCDefense == given_ratings[9]).filter(
        Matches.AwayTeamLDefense == given_ratings[10]).filter(Matches.AwayTeamRAttack == given_ratings[11]).filter(
        Matches.AwayTeamCAttack == given_ratings[12]).filter(Matches.AwayTeamLAttack == given_ratings[13])
    session.close()
    if records.count() == 0:
        dw.show_error_window_in_thread(title='No match',
                                       message='No matches with those ratings were found in the database')
        return ans
    for record in records:
        ans['Sum of home goals'] += record.HomeTeamGoals
        ans['Sum of away goals'] += record.AwayTeamGoals
        if record.HomeTeamGoals > record.AwayTeamGoals:
            ans['Home wins'] += 1
        elif record.HomeTeamGoals == record.AwayTeamGoals:
            ans['Draws'] += 1
        else:
            ans['Away wins'] += 1
    ans['Home goals average'] = ans['Sum of home goals'] / records.count()
    ans['Away goals average'] = ans['Sum of away goals'] / records.count()
    return ans
