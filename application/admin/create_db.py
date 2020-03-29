from sqlalchemy import create_engine

engine = create_engine('sqlite:///db/matches.db', echo=True)
